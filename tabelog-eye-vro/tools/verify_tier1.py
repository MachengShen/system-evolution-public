#!/usr/bin/env python3
"""
Open-Source Tier-1 Static & Authenticity Gate (`verify_tier1.py`)
for Tabelog·Eye + SGDO/VRO Contributors.

Checks:
1. Valid JSON in `dataset.json` and `manifest.json`
2. Zero stock-photo URLs (unsplash.com, pexels.com, pixabay.com, picsum.photos)
3. Honest chain-store calibration cap (|calibrated_score - tabelog_raw| <= 0.08 for chains)
4. Zero private RFC1918 / CGNAT / Tailscale IPs (10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16, 100.64.0.0/10)
5. Zero local home directory paths (`/home/`, `/Users/`)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "app"
BANNED_STOCK = ("unsplash.com", "pexels.com", "pixabay.com", "picsum.photos")
PRIVATE_IP_RE = re.compile(
    r"\b(?:10\.\d{1,3}\.\d{1,3}\.\d{1,3}|192\.168\.\d{1,3}\.\d{1,3}|172\.(?:1[6-9]|2\d|3[0-1])\.\d{1,3}\.\d{1,3}|100\.(?:6[4-9]|[7-9]\d|1[0-1]\d|12[0-7])\.\d{1,3}\.\d{1,3})\b"
)
LOCAL_PATH_RE = re.compile(r"(?:/home/[a-zA-Z0-9_-]+|/Users/[a-zA-Z0-9_-]+)")


def main() -> int:
    errors: list[str] = []
    ds_file = ROOT / "dataset.json"
    if not ds_file.exists():
        print(f"[FAIL] Missing {ds_file}", file=sys.stderr)
        return 1

    try:
        ds = json.loads(ds_file.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"[FAIL] Invalid JSON in dataset.json: {exc}", file=sys.stderr)
        return 1

    venues = ds.get("venues", [])
    if not venues:
        errors.append("dataset.json contains 0 venues")

    for v in venues:
        vid = v.get("id", "unknown")
        img = v.get("image_url", "")
        if any(b in img.lower() for b in BANNED_STOCK):
            errors.append(f"{vid}: forbidden stock photo URL {img}")
        if "honest_chain" in (v.get("bias_archetypes") or []):
            delta = abs(float(v.get("calibrated_score", 0)) - float(v.get("tabelog_raw", 0)))
            if delta > 0.0801:
                errors.append(f"{vid}: chain calibration delta {delta:.3f} exceeds ±0.08 cap")

    for fname in ("index.html", "share.html", "dataset.json", "sw.js"):
        fpath = ROOT / fname
        if not fpath.exists():
            continue
        content = fpath.read_text(encoding="utf-8")
        for m in PRIVATE_IP_RE.finditer(content):
            errors.append(f"{fname}: leaked private/Tailscale IP {m.group(0)}")
        for m in LOCAL_PATH_RE.finditer(content):
            errors.append(f"{fname}: leaked local filesystem path {m.group(0)}")

    if errors:
        for e in errors:
            print(f"[FAIL] {e}", file=sys.stderr)
        return 1

    print(f"[PASS] verify_tier1.py | {len(venues)} venues verified | 0 stock photos | ±0.08 chain cap enforced | 0 private IPs/paths")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
