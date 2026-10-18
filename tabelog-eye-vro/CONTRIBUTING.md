# Contributing to Tabelog·Eye + SGDO/VRO

Welcome! We invite systems architects, mechanism designers, culinary researchers, and open-source builders to iterate on the **Tabelog·Eye** de-biasing engine, regional booking adapters, and the **SGDO / VRO** fulfillment mechanism proposal.

This guide outlines our **Fork → Feature Iteration → Local `verify_tier1.py` Gate → Pull Request → Maintainer Cross-Model Review (`C-Gate`) → Upstream Merge** workflow.

---

## 🏛️ Core Principles, License Scope & Invariants

1. **License Scope (Code MIT · Third-Party Dish Photography Excluded)**:
   - All source code, HTML/CSS/JS, mathematical specifications, and schemas in this repository are licensed under the **MIT License**.
   - Restaurant dish photographs displayed on the live preview surface remain copyright of their respective merchants/photographers (HotPepper, TableCheck, and individual reviewers as attributed in `dataset.json` `photo_provenance`) and are **excluded from public git redistribution** via `.gitignore`.
2. **Authenticity Gate & Zero Stock Photos (Iron Law §11)**:
   - Every restaurant, dish, and craft entity in `dataset.json` MUST reflect authentic physical reality.
   - **Strictly Prohibited**: Never insert placeholder or stock imagery (`unsplash.com`, `pexels.com`, `pixabay.com`, `picsum.photos`) to mask HTTP 403 or anti-scraping failures.
   - **Fail-Closed Policy**: If authentic photography cannot be obtained, tag the entry as `QUARANTINED_MISSING_AUTHENTIC_ASSET` / `[待补真图 · 拒绝假图充数]`.
3. **Honest Chain-Store Calibration Discipline (Kiro §0)**:
   - Mass-market chain izakayas/restaurants (`honest_chain` archetype) must be capped within $|\Delta| \le 0.08$ of their raw score.
4. **PCSE Compliance & Privacy Boundaries**:
   - Zero private real names, zero private financial accounts, zero RFC1918 (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`) or CGNAT/Tailscale (`100.64.0.0/10`) IPs, and zero local filesystem paths (`/home/...`, `/Users/...`).
   - Zero automated write actions against third-party booking or social platforms (`PCSE (f)`).
   - Client-side isolation uses a privacy-preserving **per-browser `localStorage` sandbox** (`$100.00` virtual guest sandbox budget).

---

## 🔄 Step-by-Step Contribution Workflow

### Step 1: Fork & Clone

```bash
git clone https://github.com/<your-username>/system-evolution-public.git
cd system-evolution-public
git checkout -b feat/tabelog-eye-your-feature
```

### Step 2: Run the Open-Source Tier-1 Gate Locally

Before opening a Pull Request, run the included zero-dependency verification script:

```bash
python3 tabelog-eye-vro/tools/verify_tier1.py
```

This verifies:
- ✅ Valid JSON in `dataset.json`
- ✅ Zero stock photography domains (`unsplash.com`, `pexels.com`, `pixabay.com`, `picsum.photos`)
- ✅ Honest chain-store calibration cap ($|\Delta| \le 0.08$)
- ✅ Zero leaked private/CGNAT IPs or local home paths

### Step 3: Submit a Pull Request

Push your branch to your fork and open a Pull Request against `MachengShen/system-evolution-public:main` using `.github/PULL_REQUEST_TEMPLATE.md`.

---

## 🛡️ Maintainer Review (`C-Gate`) & Contributor Recognition

When you submit a Pull Request, project maintainers execute the `C-Gate` verification workflow on the staging environment:
1. **Tier-1 & Headless Browser Verification**: Maintainers run `verify_tier1.py` and `surface-verify` (DOM & ServiceWorker check).
2. **Cross-Model-Family Review**: Architectural or mathematical changes are reviewed by a model family distinct from the maintainer pipeline that drafted the target module (e.g., Claude Opus 5.5 reviewing Gemini-authored changes) plus human maintainer sign-off.
3. **Upstream Merge & Attribution**: Merged contributors are recorded in git history and `CONTRIBUTORS.md` (and eligible for Soulbound Track-Record $W_i(t)$ attribution as the proposed VRO ledger layer matures).
