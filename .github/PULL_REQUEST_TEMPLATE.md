## Summary of Contribution

- **Module / Surface**: (`app/index.html` / `app/dataset.json` / `self-host/` / `sgdao-fulfillment-proposal`)
- **What this PR improves**:

## Verification & Compliance Checklist

- [ ] Ran `python3 tabelog-eye-vro/tools/verify_tier1.py` locally and pasted the `[PASS]` output below.
- [ ] **§11 Anti-Fabrication Gate**: Zero stock photo URLs (`unsplash.com`, `pexels.com`, `pixabay.com`, `picsum.photos`); any venue lacking authentic photography is explicitly quarantined.
- [ ] **Kiro §0 Chain Cap**: Any `honest_chain` venue calibration remains within $|\Delta| \le 0.08$.
- [ ] **PCSE Cleanliness**: Zero private names, zero RFC1918/CGNAT IPs (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`, `100.64.0.0/10`), zero local `/home/` or `/Users/` paths, and zero automated third-party platform writes.

```text
# Paste output of `python3 tabelog-eye-vro/tools/verify_tier1.py` here:
```
