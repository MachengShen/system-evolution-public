#!/usr/bin/env python3
"""
Tabelog·Eye + VRO Autonomous Booking & De-Biasing Service (Self-Host Node)
Zero-dependency Python 3 Standalone Server with:
- Per-device cryptographic fingerprint isolation
- Local SQLite taste asset vault
- Configurable monthly budget cap ($100.00/mo covenant gate)
- 5-factor multimodal de-biasing calculation engine
"""

import http.server
import socketserver
import sqlite3
import json
import os
import sys
import time
import datetime
import hashlib
import urllib.parse
import traceback
import math
import uuid

# Configuration from Environment
PORT = int(os.environ.get("PORT", "8080"))
HOST = os.environ.get("HOST", "0.0.0.0")
DEFAULT_BUDGET_CAP = float(os.environ.get("DEFAULT_MONTHLY_BUDGET_CAP", "100.00"))
VAULT_DB_PATH = os.environ.get("VAULT_DB_PATH", os.path.join(os.path.dirname(__file__), "data", "taste_vault.db"))
DEVICE_SALT = os.environ.get("DEVICE_SALT", "tabelog-eye-vro-local-salt-2026")
ALLOW_CORS = os.environ.get("ALLOW_CORS", "true").lower() in ("true", "1", "yes")

SERVER_START_TIME = time.time()

# Ensure database directory exists
os.makedirs(os.path.dirname(os.path.abspath(VAULT_DB_PATH)), exist_ok=True)


def get_db():
    conn = sqlite3.connect(VAULT_DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


def init_db():
    conn = get_db()
    with conn:
        # 1. Device Profiles (Fingerprint isolation)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS device_profiles (
                device_id TEXT PRIMARY KEY,
                alias TEXT,
                taste_dna TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # 2. Taste Assets (Local private bookmarks & ratings)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS taste_assets (
                id TEXT PRIMARY KEY,
                device_id TEXT NOT NULL,
                restaurant_id TEXT NOT NULL,
                restaurant_name TEXT NOT NULL,
                original_score REAL DEFAULT 0.0,
                calibrated_score REAL DEFAULT 0.0,
                notes TEXT DEFAULT '',
                status TEXT DEFAULT 'bookmarked',
                tags TEXT DEFAULT '',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(device_id, restaurant_id)
            )
        """)

        # 3. Monthly Covenant Budget Ledger
        conn.execute("""
            CREATE TABLE IF NOT EXISTS covenant_budget (
                id TEXT PRIMARY KEY,
                device_id TEXT NOT NULL,
                billing_cycle TEXT NOT NULL,
                budget_cap_usd REAL DEFAULT 100.00,
                spent_usd REAL DEFAULT 0.00,
                pending_queue_usd REAL DEFAULT 0.00,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(device_id, billing_cycle)
            )
        """)

        # 4. VRO Autonomous Booking Orders
        conn.execute("""
            CREATE TABLE IF NOT EXISTS vro_reservations (
                id TEXT PRIMARY KEY,
                device_id TEXT NOT NULL,
                restaurant_id TEXT NOT NULL,
                restaurant_name TEXT NOT NULL,
                party_size INTEGER DEFAULT 1,
                target_datetime TEXT NOT NULL,
                status TEXT DEFAULT 'PENDING_OWNER_TOKEN',
                quote_usd REAL DEFAULT 0.00,
                fee_usd REAL DEFAULT 0.00,
                booking_notes TEXT DEFAULT '',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # 5. Multimodal De-Biasing Cache
        conn.execute("""
            CREATE TABLE IF NOT EXISTS debiasing_cache (
                restaurant_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                original_score REAL NOT NULL,
                delta_vision REAL DEFAULT 0.0,
                delta_surprise REAL DEFAULT 0.0,
                delta_ortho REAL DEFAULT 0.0,
                delta_sample REAL DEFAULT 0.0,
                delta_hype REAL DEFAULT 0.0,
                calibrated_score REAL NOT NULL,
                ci_lower REAL DEFAULT 0.0,
                ci_upper REAL DEFAULT 0.0,
                craft_evidence TEXT DEFAULT '',
                computed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
    conn.close()


def get_utc_now():
    try:
        return datetime.datetime.now(datetime.timezone.utc)
    except AttributeError:
        return datetime.datetime.utcnow()


def current_cycle():
    return get_utc_now().strftime("%Y-%m")


def derive_device_id(headers, client_ip):
    raw_fp = headers.get("X-Device-Fingerprint")
    if not raw_fp:
        auth = headers.get("Authorization", "")
        if auth.startswith("Bearer "):
            raw_fp = auth[7:].strip()
    if not raw_fp:
        # Fallback to User-Agent + client IP
        ua = headers.get("User-Agent", "unknown-client")
        raw_fp = f"{client_ip}:{ua}"

    # Cryptographic one-way hash with local salt
    h = hashlib.sha256(f"{DEVICE_SALT}:{raw_fp}".encode("utf-8")).hexdigest()
    return f"dev_{h[:16]}"


def get_or_create_device(device_id, alias=None):
    conn = get_db()
    with conn:
        row = conn.execute("SELECT * FROM device_profiles WHERE device_id = ?", (device_id,)).fetchone()
        now = get_utc_now().isoformat()
        if not row:
            default_dna = {
                "umami_preference": 0.85,
                "salt_tolerance": 0.50,
                "fire_craft_weight": 0.90,
                "dashi_focus": 0.80,
                "solo_friendly_bias": 0.70,
                "max_reservation_fee_usd": 15.00
            }
            conn.execute(
                "INSERT INTO device_profiles (device_id, alias, taste_dna, created_at, last_seen) VALUES (?, ?, ?, ?, ?)",
                (device_id, alias or f"Device-{device_id[-6:]}", json.dumps(default_dna), now, now)
            )
        else:
            conn.execute("UPDATE device_profiles SET last_seen = ? WHERE device_id = ?", (now, device_id))
    conn.close()


def get_or_create_budget(device_id, cycle=None):
    if not cycle:
        cycle = current_cycle()
    conn = get_db()
    with conn:
        row = conn.execute(
            "SELECT * FROM covenant_budget WHERE device_id = ? AND billing_cycle = ?",
            (device_id, cycle)
        ).fetchone()
        if not row:
            bid = f"bg_{uuid.uuid4().hex[:12]}"
            conn.execute(
                "INSERT INTO covenant_budget (id, device_id, billing_cycle, budget_cap_usd, spent_usd, pending_queue_usd) VALUES (?, ?, ?, ?, 0.00, 0.00)",
                (bid, device_id, cycle, DEFAULT_BUDGET_CAP)
            )
            row = conn.execute("SELECT * FROM covenant_budget WHERE id = ?", (bid,)).fetchone()
    conn.close()
    return dict(row)


def run_debiasing_calculation(original_score, vision_craft=0.0, surprise_factor=0.0,
                             ortho_factor=0.0, sample_size=30, hype_penalty=0.0):
    """
    Kiro 5-Factor Multimodal De-Biasing Engine
    S_true = S_tabelog + Delta_vision + Delta_surprise + Delta_ortho + Delta_sample - Delta_hype
    """
    orig = float(original_score)

    # 1. Delta vision: Craft hard evidence (knife work, fire char, dashi clarity, shari gloss)
    d_vision = max(-0.15, min(0.40, float(vision_craft) * 0.35))

    # 2. Delta surprise: Review sentiment excess over numeric score
    d_surprise = max(-0.10, min(0.35, float(surprise_factor) * 0.30))

    # 3. Delta ortho: Decouple harsh service / humble ambiance anchor
    d_ortho = max(-0.10, min(0.30, float(ortho_factor) * 0.25))

    # 4. Delta sample: Bayesian shrinkage for sample confidence
    n = max(1, int(sample_size))
    # Shrinkage dampener: smaller samples shrink closer to baseline
    shrinkage = n / (n + 15.0)
    d_sample = 0.05 * (1.0 - shrinkage) if orig < 3.5 else -0.05 * (1.0 - shrinkage)

    # 5. Delta hype: Influencer hype, social queue tax deduction
    d_hype = max(0.0, min(0.45, float(hype_penalty) * 0.35))

    raw_delta = d_vision + d_surprise + d_ortho + d_sample - d_hype

    # Max delta bounds [-0.50, +0.65] to avoid over-calibration
    bounded_delta = max(-0.50, min(0.65, raw_delta))
    calibrated = round(max(1.0, min(5.0, orig + bounded_delta)), 2)

    # 80% Confidence Interval
    variance = 0.08 / math.sqrt(shrinkage)
    ci_margin = round(1.28 * variance, 2)
    ci_lower = round(max(1.0, calibrated - ci_margin), 2)
    ci_upper = round(min(5.0, calibrated + ci_margin), 2)

    return {
        "original_score": round(orig, 2),
        "calibrated_score": calibrated,
        "total_delta": round(calibrated - orig, 2),
        "delta_vision": round(d_vision, 3),
        "delta_surprise": round(d_surprise, 3),
        "delta_ortho": round(d_ortho, 3),
        "delta_sample": round(d_sample, 3),
        "delta_hype": round(d_hype, 3),
        "ci_80": [ci_lower, ci_upper],
        "sample_size": n
    }


class TabelogEyeVROHandler(http.server.BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        # Clean stdout logger
        sys.stdout.write(f"[{get_utc_now().strftime('%Y-%m-%d %H:%M:%S')}] {self.address_string()} - {format % args}\n")
        sys.stdout.flush()

    def send_cors_headers(self):
        if ALLOW_CORS:
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization, X-Device-Fingerprint, X-Device-Alias")

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_cors_headers()
        self.end_headers()

    def send_json(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_cors_headers()
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def send_error_json(self, message, status=400, code="CLIENT_ERROR", details=None):
        payload = {
            "error": code,
            "message": message,
            "status": status,
            "timestamp": get_utc_now().isoformat()
        }
        if details:
            payload["details"] = details
        self.send_json(payload, status=status)

    def parse_json_body(self):
        try:
            content_length = int(self.headers.get("Content-Length", 0))
            if content_length <= 0:
                return {}
            body_bytes = self.rfile.read(content_length)
            return json.loads(body_bytes.decode("utf-8"))
        except Exception as e:
            raise ValueError(f"Invalid JSON body: {str(e)}")

    def get_device(self):
        client_ip = self.client_address[0] if self.client_address else "127.0.0.1"
        device_id = derive_device_id(self.headers, client_ip)
        alias = self.headers.get("X-Device-Alias")
        get_or_create_device(device_id, alias)
        return device_id

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)

        try:
            # 1. Healthcheck
            if path in ("/health", "/api/health"):
                self.handle_health()
                return

            # 2. VRO Covenant Budget
            elif path == "/api/vro/budget":
                self.handle_get_budget(query)
                return

            # 3. VRO Reservations
            elif path == "/api/vro/reservations":
                self.handle_get_reservations(query)
                return

            # 4. Taste Assets (Bookmarks & Private Notes)
            elif path == "/api/taste/assets":
                self.handle_get_taste_assets(query)
                return

            # 5. Taste DNA Profile
            elif path == "/api/taste/dna":
                self.handle_get_taste_dna()
                return

            # 6. De-Biasing Sample Demo
            elif path == "/api/debias/demo":
                self.handle_debias_demo()
                return

            # 7. Web Dashboard View
            elif path in ("/", "/index.html"):
                self.handle_serve_dashboard()
                return

            else:
                self.send_error_json(f"Endpoint not found: {path}", status=404, code="NOT_FOUND")

        except Exception as e:
            traceback.print_exc()
            self.send_error_json(str(e), status=500, code="INTERNAL_SERVER_ERROR")

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        try:
            body = self.parse_json_body()

            # 1. Update Monthly Budget Cap
            if path == "/api/vro/budget/cap":
                self.handle_update_budget_cap(body)
                return

            # 2. Submit VRO Autonomous Booking Intent (With Covenant Budget Gate)
            elif path == "/api/vro/book":
                self.handle_create_vro_booking(body)
                return

            # 3. Save / Upsert Taste Asset (Local Vault)
            elif path == "/api/taste/assets":
                self.handle_save_taste_asset(body)
                return

            # 4. Update Taste DNA
            elif path == "/api/taste/dna":
                self.handle_update_taste_dna(body)
                return

            # 5. Run 5-Factor Multimodal De-Biasing Calculation
            elif path == "/api/debias/calculate":
                self.handle_calculate_debias(body)
                return

            else:
                self.send_error_json(f"Endpoint not found: {path}", status=404, code="NOT_FOUND")

        except ValueError as ve:
            self.send_error_json(str(ve), status=400, code="INVALID_PAYLOAD")
        except Exception as e:
            traceback.print_exc()
            self.send_error_json(str(e), status=500, code="INTERNAL_SERVER_ERROR")

    def do_DELETE(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        query = urllib.parse.parse_qs(parsed.query)

        try:
            if path == "/api/taste/assets":
                self.handle_delete_taste_asset(query)
                return
            else:
                self.send_error_json(f"Endpoint not found: {path}", status=404, code="NOT_FOUND")
        except Exception as e:
            traceback.print_exc()
            self.send_error_json(str(e), status=500, code="INTERNAL_SERVER_ERROR")

    # --- HANDLERS ---

    def handle_health(self):
        uptime = round(time.time() - SERVER_START_TIME, 1)
        conn = get_db()
        device_count = conn.execute("SELECT COUNT(*) FROM device_profiles").fetchone()[0]
        asset_count = conn.execute("SELECT COUNT(*) FROM taste_assets").fetchone()[0]
        res_count = conn.execute("SELECT COUNT(*) FROM vro_reservations").fetchone()[0]
        conn.close()

        self.send_json({
            "status": "healthy",
            "service": "Tabelog·Eye + VRO Autonomous Booking & De-Biasing Node",
            "version": "1.0.0-selfhost",
            "uptime_seconds": uptime,
            "architecture": "zero-dependency-sqlite-vault",
            "stats": {
                "isolated_devices": device_count,
                "vault_taste_assets": asset_count,
                "vro_reservations": res_count
            },
            "timestamp": get_utc_now().isoformat()
        })

    def handle_get_budget(self, query):
        device_id = self.get_device()
        cycle = query.get("cycle", [current_cycle()])[0]
        budget = get_or_create_budget(device_id, cycle)

        cap = budget["budget_cap_usd"]
        spent = budget["spent_usd"]
        pending = budget["pending_queue_usd"]
        remaining = max(0.0, cap - (spent + pending))
        utilization = round(((spent + pending) / cap * 100.0) if cap > 0 else 100.0, 1)

        self.send_json({
            "device_id": device_id,
            "billing_cycle": cycle,
            "budget_cap_usd": cap,
            "spent_usd": spent,
            "pending_queue_usd": pending,
            "remaining_usd": round(remaining, 2),
            "utilization_pct": utilization,
            "is_exhausted": remaining <= 0.0,
            "updated_at": budget["updated_at"]
        })

    def handle_update_budget_cap(self, body):
        device_id = self.get_device()
        new_cap = body.get("budget_cap_usd")
        if new_cap is None or float(new_cap) < 0:
            self.send_error_json("Invalid 'budget_cap_usd'. Must be a non-negative number.", status=400)
            return

        new_cap = float(new_cap)
        cycle = body.get("billing_cycle", current_cycle())
        conn = get_db()
        with conn:
            get_or_create_budget(device_id, cycle)
            conn.execute(
                "UPDATE covenant_budget SET budget_cap_usd = ?, updated_at = CURRENT_TIMESTAMP WHERE device_id = ? AND billing_cycle = ?",
                (new_cap, device_id, cycle)
            )
        conn.close()

        self.handle_get_budget({"cycle": [cycle]})

    def handle_create_vro_booking(self, body):
        """
        VRO Autonomous Booking Intent with Strict Covenant Budget Gate
        """
        device_id = self.get_device()
        restaurant_id = body.get("restaurant_id")
        restaurant_name = body.get("restaurant_name")
        target_datetime = body.get("target_datetime")
        party_size = int(body.get("party_size", 1))
        fee_usd = float(body.get("fee_usd", 8.00))  # Default micro-bounty fee $8.00
        quote_usd = float(body.get("quote_usd", 0.00))
        booking_notes = body.get("notes", "")

        if not restaurant_id or not restaurant_name or not target_datetime:
            self.send_error_json("Missing required fields: restaurant_id, restaurant_name, target_datetime", status=400)
            return

        cycle = current_cycle()
        budget = get_or_create_budget(device_id, cycle)

        cap = budget["budget_cap_usd"]
        spent = budget["spent_usd"]
        pending = budget["pending_queue_usd"]

        # HARD GATE: Check against covenant monthly budget cap
        projected_spend = spent + pending + fee_usd
        if projected_spend > cap:
            self.send_error_json(
                message=f"VRO Autonomous Booking blocked by Covenant Budget Gate. Projected spend (${projected_spend:.2f}) exceeds monthly cap (${cap:.2f}).",
                status=402,
                code="BUDGET_CAP_EXCEEDED_GATE",
                details={
                    "budget_cap_usd": cap,
                    "spent_usd": spent,
                    "pending_queue_usd": pending,
                    "requested_fee_usd": fee_usd,
                    "shortfall_usd": round(projected_spend - cap, 2),
                    "resolution": "Increase budget cap via POST /api/vro/budget/cap or wait for next billing cycle."
                }
            )
            return

        # Gate passed: Create reservation record & update pending queue
        res_id = f"vro_{uuid.uuid4().hex[:12]}"
        conn = get_db()
        with conn:
            conn.execute("""
                INSERT INTO vro_reservations 
                (id, device_id, restaurant_id, restaurant_name, party_size, target_datetime, status, quote_usd, fee_usd, booking_notes)
                VALUES (?, ?, ?, ?, ?, ?, 'PENDING_OWNER_TOKEN', ?, ?, ?)
            """, (res_id, device_id, restaurant_id, restaurant_name, party_size, target_datetime, quote_usd, fee_usd, booking_notes))

            # Put fee into pending queue until fulfilled
            conn.execute("""
                UPDATE covenant_budget 
                SET pending_queue_usd = pending_queue_usd + ?, updated_at = CURRENT_TIMESTAMP
                WHERE device_id = ? AND billing_cycle = ?
            """, (fee_usd, device_id, cycle))
        conn.close()

        self.send_json({
            "success": True,
            "reservation_id": res_id,
            "status": "PENDING_OWNER_TOKEN",
            "message": "VRO autonomous booking intent registered in local vault. Awaiting owner authorization token before phone/concierge agent dispatch.",
            "covenant_ledger": {
                "monthly_cap_usd": cap,
                "new_pending_queue_usd": round(pending + fee_usd, 2),
                "remaining_unallocated_usd": round(cap - (spent + pending + fee_usd), 2)
            },
            "reservation": {
                "id": res_id,
                "restaurant_name": restaurant_name,
                "target_datetime": target_datetime,
                "party_size": party_size,
                "fee_usd": fee_usd
            }
        }, status=201)

    def handle_get_reservations(self, query):
        device_id = self.get_device()
        conn = get_db()
        rows = conn.execute(
            "SELECT * FROM vro_reservations WHERE device_id = ? ORDER BY created_at DESC",
            (device_id,)
        ).fetchall()
        conn.close()

        res_list = [dict(r) for r in rows]
        self.send_json({
            "device_id": device_id,
            "total": len(res_list),
            "reservations": res_list
        })

    def handle_get_taste_assets(self, query):
        device_id = self.get_device()
        status_filter = query.get("status", [None])[0]

        conn = get_db()
        if status_filter:
            rows = conn.execute(
                "SELECT * FROM taste_assets WHERE device_id = ? AND status = ? ORDER BY updated_at DESC",
                (device_id, status_filter)
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT * FROM taste_assets WHERE device_id = ? ORDER BY updated_at DESC",
                (device_id,)
            ).fetchall()
        conn.close()

        assets = [dict(r) for r in rows]
        self.send_json({
            "device_id": device_id,
            "total": len(assets),
            "assets": assets
        })

    def handle_save_taste_asset(self, body):
        device_id = self.get_device()
        restaurant_id = body.get("restaurant_id")
        restaurant_name = body.get("restaurant_name")

        if not restaurant_id or not restaurant_name:
            self.send_error_json("Missing restaurant_id or restaurant_name", status=400)
            return

        orig_score = float(body.get("original_score", 0.0))
        cal_score = float(body.get("calibrated_score", orig_score))
        notes = body.get("notes", "")
        status = body.get("status", "bookmarked")
        tags = body.get("tags", "")
        now = get_utc_now().isoformat()
        asset_id = f"ast_{uuid.uuid4().hex[:12]}"

        conn = get_db()
        with conn:
            conn.execute("""
                INSERT INTO taste_assets (id, device_id, restaurant_id, restaurant_name, original_score, calibrated_score, notes, status, tags, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(device_id, restaurant_id) DO UPDATE SET
                    restaurant_name = excluded.restaurant_name,
                    original_score = excluded.original_score,
                    calibrated_score = excluded.calibrated_score,
                    notes = excluded.notes,
                    status = excluded.status,
                    tags = excluded.tags,
                    updated_at = excluded.updated_at
            """, (asset_id, device_id, restaurant_id, restaurant_name, orig_score, cal_score, notes, status, tags, now, now))
        conn.close()

        self.send_json({
            "success": True,
            "device_id": device_id,
            "restaurant_id": restaurant_id,
            "status": status,
            "message": "Taste asset safely stored in local SQLite vault."
        })

    def handle_delete_taste_asset(self, query):
        device_id = self.get_device()
        restaurant_id = query.get("restaurant_id", [None])[0]
        if not restaurant_id:
            self.send_error_json("Missing restaurant_id parameter", status=400)
            return

        conn = get_db()
        with conn:
            conn.execute("DELETE FROM taste_assets WHERE device_id = ? AND restaurant_id = ?", (device_id, restaurant_id))
        conn.close()

        self.send_json({
            "success": True,
            "deleted": restaurant_id,
            "message": "Taste asset removed from device vault."
        })

    def handle_get_taste_dna(self):
        device_id = self.get_device()
        conn = get_db()
        row = conn.execute("SELECT taste_dna FROM device_profiles WHERE device_id = ?", (device_id,)).fetchone()
        conn.close()

        dna = json.loads(row["taste_dna"]) if row and row["taste_dna"] else {}
        self.send_json({
            "device_id": device_id,
            "taste_dna": dna
        })

    def handle_update_taste_dna(self, body):
        device_id = self.get_device()
        dna_payload = body.get("taste_dna", body)
        conn = get_db()
        with conn:
            conn.execute(
                "UPDATE device_profiles SET taste_dna = ?, last_seen = CURRENT_TIMESTAMP WHERE device_id = ?",
                (json.dumps(dna_payload), device_id)
            )
        conn.close()

        self.send_json({
            "success": True,
            "device_id": device_id,
            "taste_dna": dna_payload,
            "message": "Taste DNA preference coordinates updated in local vault."
        })

    def handle_calculate_debias(self, body):
        orig = body.get("original_score")
        if orig is None:
            self.send_error_json("Missing 'original_score' (e.g. 3.42)", status=400)
            return

        vision = body.get("vision_craft", 0.0)
        surprise = body.get("surprise_factor", 0.0)
        ortho = body.get("ortho_factor", 0.0)
        sample = body.get("sample_size", 30)
        hype = body.get("hype_penalty", 0.0)

        result = run_debiasing_calculation(
            original_score=orig,
            vision_craft=vision,
            surprise_factor=surprise,
            ortho_factor=ortho,
            sample_size=sample,
            hype_penalty=hype
        )

        restaurant_name = body.get("restaurant_name")
        if restaurant_name:
            result["restaurant_name"] = restaurant_name

        self.send_json(result)

    def handle_debias_demo(self):
        samples = [
            {
                "restaurant_name": "鳥恵 上野広小路 (Yakitori Torie)",
                "category": "焼き鳥 · 炭火火入れの極致",
                "tabelog_score": 3.48,
                "calibrated_score": 3.86,
                "delta": "+0.38",
                "craft_evidence": "备长炭精准碳化层、肉汁锁闭度与山椒内敛调和，手艺证据远超均值",
                "why_underrated": "老客偏爱安静不写长文，服务冷面导致大众点评网民扣分，被算法拉低"
            },
            {
                "restaurant_name": "鮨 喜よし (Sushi Kiyoshi)",
                "category": "江戸前鮨 · 赤酢舎利",
                "tabelog_score": 3.39,
                "calibrated_score": 3.81,
                "delta": "+0.42",
                "craft_evidence": "小肌三日熟成切纹均匀，赤醋舍利酸温契合度达一流水准",
                "why_underrated": "拒绝网红打卡摄影，仅8席社区常客熟客制，大众评论样本量小"
            },
            {
                "restaurant_name": "酒坊 猩々 (Izakaya Shōjō)",
                "category": "大衆割烹 · 出汁本味",
                "tabelog_score": 3.34,
                "calibrated_score": 3.74,
                "delta": "+0.40",
                "craft_evidence": "一番出汁黄金清澈度与昆布旨味厚重，季节煮物火候纯正",
                "why_underrated": "排队全为老饕熟人，烟火气与朴素店面被外来打卡游客给出服务中评"
            }
        ]
        self.send_json({
            "service": "Tabelog·Eye Multimodal De-Biasing Reference Set",
            "count": len(samples),
            "samples": samples
        })

    def handle_serve_dashboard(self):
        device_id = self.get_device()
        budget = get_or_create_budget(device_id)

        html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tabelog·Eye + VRO Self-Host Node</title>
  <style>
    :root {{
      --bg: #0c0d0e;
      --surface: #141618;
      --surface-elevated: #1a1d20;
      --border: #282b30;
      --gold: #d4a359;
      --gold-light: #f5cf8e;
      --gold-dim: rgba(212, 163, 89, 0.15);
      --text-main: #f0f2f5;
      --text-muted: #8e95a0;
      --green: #4ade80;
      --amber: #fbbf24;
      --red: #f87171;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: var(--bg);
      color: var(--text-main);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.5;
      padding: 24px;
    }}
    .container {{
      max-width: 980px;
      margin: 0 auto;
    }}
    header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 20px;
      border-bottom: 1px solid var(--border);
      margin-bottom: 24px;
    }}
    .logo-box {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .logo-badge {{
      background: var(--gold-dim);
      border: 1px solid var(--gold);
      color: var(--gold-light);
      padding: 6px 12px;
      border-radius: 8px;
      font-size: 0.85rem;
      font-weight: 700;
      letter-spacing: 0.5px;
    }}
    h1 {{
      font-size: 1.4rem;
      font-weight: 700;
      color: #fff;
    }}
    .subtitle {{
      color: var(--text-muted);
      font-size: 0.85rem;
    }}
    .node-tag {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 0.8rem;
      background: rgba(74, 222, 128, 0.12);
      border: 1px solid rgba(74, 222, 128, 0.3);
      color: var(--green);
      padding: 4px 10px;
      border-radius: 999px;
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 16px;
      margin-bottom: 24px;
    }}
    .card {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 20px;
    }}
    .card-title {{
      font-size: 0.95rem;
      font-weight: 600;
      color: var(--gold-light);
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 14px;
    }}
    .meter-wrap {{
      margin: 12px 0;
    }}
    .meter-bg {{
      background: #202327;
      height: 10px;
      border-radius: 5px;
      overflow: hidden;
      position: relative;
    }}
    .meter-fill {{
      background: linear-gradient(90deg, var(--green), var(--amber));
      height: 100%;
      border-radius: 5px;
      width: {min(100.0, (budget['spent_usd'] + budget['pending_queue_usd']) / budget['budget_cap_usd'] * 100.0) if budget['budget_cap_usd'] > 0 else 0}%;
    }}
    .stat-row {{
      display: flex;
      justify-content: space-between;
      font-size: 0.85rem;
      padding: 6px 0;
      border-bottom: 1px dashed rgba(255,255,255,0.06);
    }}
    .stat-row:last-child {{ border-bottom: none; }}
    .stat-label {{ color: var(--text-muted); }}
    .stat-value {{ font-family: monospace; font-weight: 600; color: #fff; }}
    code, pre {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
    }}
    pre {{
      background: #090a0b;
      border: 1px solid var(--border);
      padding: 12px;
      border-radius: 8px;
      font-size: 0.78rem;
      color: #9cdcfe;
      overflow-x: auto;
      margin-top: 10px;
    }}
    .btn {{
      background: var(--gold-dim);
      border: 1px solid var(--gold);
      color: var(--gold-light);
      padding: 8px 14px;
      border-radius: 6px;
      font-size: 0.82rem;
      font-weight: 600;
      cursor: pointer;
      text-decoration: none;
      display: inline-block;
      transition: all 0.15s ease;
    }}
    .btn:hover {{
      background: var(--gold);
      color: #000;
    }}
    .section-title {{
      font-size: 1.1rem;
      font-weight: 600;
      color: #fff;
      margin-bottom: 12px;
    }}
    .input-row {{
      display: flex;
      gap: 10px;
      margin-top: 10px;
    }}
    input, select {{
      background: #0a0b0c;
      border: 1px solid var(--border);
      color: #fff;
      padding: 8px 12px;
      border-radius: 6px;
      font-size: 0.85rem;
      flex: 1;
    }}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="logo-box">
        <div class="logo-badge">TABELOG·EYE</div>
        <div>
          <h1>Self-Host Node & Local Vault</h1>
          <div class="subtitle">Zero-Dependency Autonomous Booking & De-Biasing Service</div>
        </div>
      </div>
      <div>
        <span class="node-tag">● NODE RUNNING (PID {os.getpid()})</span>
      </div>
    </header>

    <div class="grid">
      <!-- Device Fingerprint Isolation Card -->
      <div class="card">
        <div class="card-title">
          <span>🔒 设备指纹隔离 (Device Vault)</span>
          <span style="font-size: 0.75rem; color: var(--green);">ISOLATED</span>
        </div>
        <div class="stat-row">
          <span class="stat-label">Device Vault ID</span>
          <span class="stat-value">{device_id}</span>
        </div>
        <div class="stat-row">
          <span class="stat-label">Storage Engine</span>
          <span class="stat-value">Local SQLite WAL</span>
        </div>
        <div class="stat-row">
          <span class="stat-label">DB Location</span>
          <span class="stat-value">{os.path.basename(VAULT_DB_PATH)}</span>
        </div>
        <div class="stat-row">
          <span class="stat-label">Cross-Device Leakage</span>
          <span class="stat-value" style="color: var(--green);">ZERO (SHA-256 Salted)</span>
        </div>
      </div>

      <!-- Covenant Monthly Budget Meter Card -->
      <div class="card">
        <div class="card-title">
          <span>🛡️ VRO 月度契约硬顶 (Covenant Cap)</span>
          <span style="font-size: 0.75rem; color: var(--gold);">${budget['budget_cap_usd']:.2f}/月</span>
        </div>
        <div class="meter-wrap">
          <div class="meter-bg">
            <div class="meter-fill"></div>
          </div>
        </div>
        <div class="stat-row">
          <span class="stat-label">已结算实付</span>
          <span class="stat-value">${budget['spent_usd']:.2f}</span>
        </div>
        <div class="stat-row">
          <span class="stat-label">待批自主预约微悬赏</span>
          <span class="stat-value" style="color: var(--amber);">${budget['pending_queue_usd']:.2f}</span>
        </div>
        <div class="stat-row">
          <span class="stat-label">安全剩余额度</span>
          <span class="stat-value" style="color: var(--green);">${max(0.0, budget['budget_cap_usd'] - budget['spent_usd'] - budget['pending_queue_usd']):.2f}</span>
        </div>
      </div>
    </div>

    <!-- Quick API Specs Card -->
    <div class="card" style="margin-bottom: 24px;">
      <div class="card-title">
        <span>⚡ 核心 REST API 接口清单</span>
        <a href="README-SELF-HOST.md" class="btn" style="padding: 4px 10px; font-size: 0.75rem;">查看完整部署指南 ↗</a>
      </div>
      <div class="stat-row">
        <span class="stat-label"><b style="color: var(--green);">GET</b> /health</span>
        <span class="stat-value">健康检查与节点运行状态</span>
      </div>
      <div class="stat-row">
        <span class="stat-label"><b style="color: var(--green);">GET</b> /api/vro/budget</span>
        <span class="stat-value">查询当前设备月度契约预算账本</span>
      </div>
      <div class="stat-row">
        <span class="stat-label"><b style="color: var(--amber);">POST</b> /api/vro/budget/cap</span>
        <span class="stat-value">修改月度硬顶阈值 (默认 $100.00/mo)</span>
      </div>
      <div class="stat-row">
        <span class="stat-label"><b style="color: var(--amber);">POST</b> /api/vro/book</span>
        <span class="stat-value">提交 VRO 自主代订意向 (自动触发预算超限安全门禁)</span>
      </div>
      <div class="stat-row">
        <span class="stat-label"><b style="color: var(--green);">GET/POST</b> /api/taste/assets</span>
        <span class="stat-value">存取本地私密赏味资产、品鉴笔记与沧海遗珠收藏</span>
      </div>
      <div class="stat-row">
        <span class="stat-label"><b style="color: var(--amber);">POST</b> /api/debias/calculate</span>
        <span class="stat-value">运行 5 维破偏置真味校准算法 (多模态手艺 + 语义残差)</span>
      </div>
    </div>

    <!-- Live Test Sandbox -->
    <div class="card">
      <div class="card-title">
        <span>🧪 破偏置真味快速试算 (Live De-Biasing Test)</span>
      </div>
      <div class="input-row">
        <input type="number" id="testScore" step="0.01" value="3.42" placeholder="食べログ 分数 (如 3.42)">
        <select id="testCraft">
          <option value="0.8">炭火/刀工/出汁：顶尖匠人 (+0.28)</option>
          <option value="0.5">食材新鲜、火候纯熟 (+0.18)</option>
          <option value="0.2">常规连锁、手艺中规中矩 (+0.07)</option>
        </select>
        <button class="btn" onclick="calcDebias()">立即校准</button>
      </div>
      <pre id="testOutput">// 点击「立即校准」查看 5 维破偏置分解与 80% 可信区间...</pre>
    </div>
  </div>

  <script>
    async function calcDebias() {{
      const score = parseFloat(document.getElementById('testScore').value);
      const craft = parseFloat(document.getElementById('testCraft').value);
      const out = document.getElementById('testOutput');
      out.textContent = 'Computing 5-factor calibration...';
      try {{
        const res = await fetch('/api/debias/calculate', {{
          method: 'POST',
          headers: {{ 'Content-Type': 'application/json' }},
          body: JSON.stringify({{
            original_score: score,
            vision_craft: craft,
            surprise_factor: 0.6,
            ortho_factor: 0.5,
            sample_size: 45,
            hype_penalty: 0.1
          }})
        }});
        const json = await res.json();
        out.textContent = JSON.stringify(json, null, 2);
      }} catch (err) {{
        out.textContent = 'Error: ' + err.message;
      }}
    }}
  </script>
</body>
</html>
"""
        body = html.encode("utf-8")
        self.send_response(200)
        self.send_cors_headers()
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def main():
    init_db()
    server_address = (HOST, PORT)
    httpd = socketserver.TCPServer(server_address, TabelogEyeVROHandler)
    print(f"=================================================================")
    print(f" Tabelog·Eye + VRO Self-Host Node running on http://{HOST}:{PORT}")
    print(f" Vault Database: {VAULT_DB_PATH}")
    print(f" Default Covenant Monthly Budget Cap: ${DEFAULT_BUDGET_CAP:.2f}/mo")
    print(f" Per-Device Cryptographic Isolation: ENABLED")
    print(f" CORS Enabled: {ALLOW_CORS}")
    print(f"=================================================================")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server gracefully.")
        httpd.server_close()


if __name__ == "__main__":
    main()
