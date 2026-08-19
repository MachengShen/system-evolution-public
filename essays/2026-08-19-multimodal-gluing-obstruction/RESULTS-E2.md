# RESULTS-E2 — real-model gluing-obstruction test (CLIP × Plato's Cave protocol)

STATUS: COMPLETE — 2026-08-19. Registered CLIP analyses (§2-§8) + SigLIP robustness (§11) + registered unimodal extension / D3 closure (§12, coordinator-directed) all done. Consolidated verdict at end of §12.

## 1. Verdict (one sentence)

**On co-trained towers (CLIP, SigLIP) the registered obstruction explanation of the Plato's-Cave alignment decay FAILS outright (r_perp falls with scale, P1 falsified; no differential stratum decay, P2 falsified); on the independently-trained pair (DINOv2 × mpnet — the regime the paper actually measured, §12) the residual rises early with the predicted sign and a strong registered correlation (partial r = −0.94) before plateauing, making independent carvings the surviving regime for a weakened P1, while P2 fails everywhere and the coarse-glueable/fine-irreducible granularity curve passes in all three model pairs.**

## 2. Alignment vs scale (reproduction of their decay)

Setup: open_clip ViT-B-32 (laion2b_s34b_b79k), MS-COCO 2017; fixed 1024-query set from val2017 (query_seed=42), growing gallery sampled from train2017 (118,287 pairs, first caption per image); mutual-kNN alignment exactly per Huh et al. as re-examined by arXiv:2604.18572; 3 gallery seeds per scale (1 at max).

| gallery N | align k=10 | align k=1 | align k=n/100 | r_perp | noise floor | excess r_perp | overdet ratio |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1,000 | 0.3034 | 0.0895 | 0.3034 | 0.02464 | 0.00936 | 0.02265 | 2.8 |
| 2,000 | 0.2292 | 0.0703 | 0.3014 | 0.02223 | 0.01242 | 0.01840 | 4.0 |
| 5,000 | 0.1556 | 0.0485 | 0.3036 | 0.01928 | 0.01302 | 0.01420 | 6.2 |
| 10,000 | 0.1150 | 0.0394 | 0.3042 | 0.01726 | 0.01163 | 0.01274 | 8.3 |
| 20,000 | 0.0819 | 0.0290 | 0.3034 | 0.01481 | 0.01052 | 0.01042 | 10.7 |
| 50,000 | 0.0527 | 0.0225 | 0.3039 | 0.01195 | 0.00828 | 0.00861 | 14.2 |
| 100,000 | 0.0382 | 0.0202 | 0.3044 | 0.01026 | 0.00683 | 0.00766 | 16.4 |
| 118,287 | 0.0354 | 0.0186 | 0.3043 | 0.00983 | 0.00638 | 0.00748 | 16.8 |

- **Their decay reproduces cleanly on co-trained CLIP towers**: k=10 alignment falls 0.303 -> 0.035 (8.6x) from 1K -> 118K. (Their DINOv2×OpenLlama: 0.135 -> 0.008 over 1K -> 15M.)
- **Their coarse-structure survival also reproduces**: k=n/100 alignment is flat (~0.304) across the entire sweep — the metric's effective resolution, not the shared coarse structure, drives the decay.
- Levels are ~2.2x higher than their unimodal pairs at matched scale, as expected for contrastively co-trained towers (deviation D3 in §7).

## 3. r_perp vs scale + correlation (registered P1)

Constraint graph at fixed k_c=64 clusters/modality (registered): nodes = per-modality k-means clusters, edges = observed cross-modal pairs aggregated per (img-cluster, txt-cluster), edge field = mean pair discrepancy 1−cos(img,txt), W = pair counts; r_perp from the THEORY-v3 cokernel operator (gamma=1), ported from exp_discounted_cokernel.py.

**P1 predicted r_perp RISES with scale and tracks the alignment decay (negative correlation with alignment). Observed: r_perp FALLS with scale** — 0.0246 -> 0.0098 raw; the split-half noise floor also falls (0.0094 -> 0.0064); noise-corrected excess residual falls too (0.0227 -> 0.0075). The overdetermination ratio (edges/dof) grows 2.9 -> 16.8 while the residual still falls.

Correlation stats (22 (N,seed) points):
- Pearson(align_k10, r_perp) = **+0.969** (p=1.4e-13); Spearman = +0.975. Alignment and residual **co-decline** — the SIGN is opposite to the registered prediction.
- Partial Pearson controlling log10(N): raw r_perp **+0.271** (p=0.22, n.s.); excess r_perp **+0.991** marginal / **+0.865** partial (p=2.0e-07) — significant but POSITIVE: wherever the residual is higher, alignment is higher too, again opposite to the obstruction story.

**P1 verdict: FALSIFIED.** The consistency field becomes MORE potential-fittable as data grows at fixed granularity (better-estimated cluster-level field), while alignment keeps decaying. The decay is therefore not explained by a growing shaping-irreducible residual at fixed carving.

## 4. Stratification (registered P2 — the discriminating test)

Queries assigned to graph edges by nearest centroids; per-scale median split on |r_perp,e|; ~800-1020 of 1024 queries fall on populated edges (rest excluded, counts in JSON).

| gallery N | align k=10 (low-residual half) | align k=10 (high-residual half) | ratio low/high |
|---:|---:|---:|---:|
| 1,000 | 0.4017 | 0.2818 | 1.43 |
| 2,000 | 0.2875 | 0.2062 | 1.39 |
| 5,000 | 0.1762 | 0.1507 | 1.17 |
| 10,000 | 0.1284 | 0.1067 | 1.20 |
| 20,000 | 0.0881 | 0.0768 | 1.15 |
| 50,000 | 0.0539 | 0.0515 | 1.05 |
| 100,000 | 0.0397 | 0.0366 | 1.08 |
| 118,287 | 0.0376 | 0.0329 | 1.14 |

**P2 predicted the low-residual stratum does NOT decay while the high-residual stratum decays strongly. Observed: BOTH strata decay ~8-10x in parallel**; the low stratum sits persistently higher (ratio 1.1-1.4, shrinking with scale). The per-edge residual is a real (if modest) correlate of pair alignability, but there is **no differential decay**. **P2 verdict: FALSIFIED as registered.**

## 5. Granularity (coarse vs fine) curve — at N=118,287

| k_c per modality | r_perp | r_perp / ||centered field|| | edges | overdet ratio |
|---:|---:|---:|---:|---:|
| 4 | 0.00260 | 0.3713 | 16 | 2.0 |
| 8 | 0.00411 | 0.4270 | 64 | 4.0 |
| 16 | 0.00527 | 0.4197 | 225 | 7.0 |
| 32 | 0.00745 | 0.4735 | 766 | 12.0 |
| 64 | 0.00980 | 0.5014 | 2115 | 16.5 |
| 128 | 0.01352 | 0.5887 | 5284 | 20.6 |
| 256 | 0.01743 | 0.6570 | 11019 | 21.5 |
| 512 | 0.02115 | 0.7038 | 19371 | 18.9 |

Monotone ~8x rise raw (0.0026 -> 0.0212), relative residual 0.37 -> 0.70: at coarse carving the cross-modal discrepancy field is largely potential-fittable (glueable); at fine carving most of it is shaping-irreducible. **This is the predicted coarse/fine signature and it PASSES** — consistent with 「粗语义能对齐、细粒不能」 and with the k=n/100 flatness in §2. But note it is a granularity statement, not a scale statement; it cannot by itself rescue P1.

## 6. Falsifier verdict (prominent, as registered)

Registered falsifier: "if r_perp does not rise with scale, or rises but is uncorrelated with the alignment decay, or the stratification shows no differential decay — the obstruction explanation fails for real models."

**The falsifier FIRES on both clauses that were tested: r_perp does not rise with scale (it falls), and stratification shows no differential decay. The overdetermination-obstruction explanation of the alignment-vs-scale decay is DEAD for real models in this operationalization.** No metric was switched mid-run; the one pre-registered amendment (noise-corrected excess residual, added before the main run) points the same way. What survives: (a) the granularity-axis obstruction curve (§5), (b) r_perp as a weak per-pair alignability correlate (§4 level offset). The wedge memo's sharpest sell — "the decay curve is our residual curve" — should be retired; the honest surviving claim is the carving-resolution dose-response, which does not distinguish our account from mundane 'fine structure is modality-specific' accounts without further discriminating work.

## 7. Caps and deviations

- **D1 Scale cap**: max gallery = 118,287 (all of COCO train2017) vs their 15M (LAION). Implication: we only probe 2 decades of the ~4-decade sweep. Their decay is monotone throughout, ours reproduces over the probed range; the P1 falsification is about the SIGN of the r_perp trend, which extra decades are unlikely to flip (residual fell 2.5x over our 2 decades with no upturn anywhere).
- **D2 Data**: MS-COCO 2017 (not WIT/LAION): only no-credential direct-download option practical today. COCO captions are cleaner/denser than WIT; this affects levels, not trends.
- **D3 Models**: co-trained CLIP towers (per the owner-ratified E2 spec), NOT their independently-trained unimodal pairs (DINOv2×OpenLlama). This is the strongest deviation: co-training actively minimizes the very inconsistency r_perp measures. A falsification under co-trained towers is thus conservative for P1's sign claim (the residual has even less reason to rise), but a rise might in principle exist for unimodal pairs — NOT tested here. SigLIP (also co-trained) robustness run appended below.
- **D4 Queries disjoint from gallery** (val vs train) at all scales; their smallest scale has query ⊂ gallery. Affects small-N levels marginally.
- **D5 Layer selection**: we use final embeddings (CLIP's contract); they sweep layer pairs at 1024 samples. N/A for co-trained towers.
- **D6 Bijective setting**: first caption per image, mirroring the main protocol they re-examine (their many-to-many appendix C not reproduced).
- Compute: Apple M5, MPS; embedding 118,287 images = 858s; full registered analysis = 137s. Wall clock dominated by a ~19GB download over a ~2MB/s uplink (incidents logged below).

## 8. Repro commands (exact)

```bash
cd ~/projects/multimodal-gluing-obstruction/e2_real
# venv: python3.12 -m venv venv; pip install torch torchvision open_clip_torch numpy scipy scikit-learn pillow tqdm
# data: COCO 2017 — annotations_trainval2017.zip, val2017.zip, train2017.zip from http://images.cocodataset.org
./venv/bin/python embed_coco.py --split val   --tag clip   # ViT-B-32 laion2b_s34b_b79k
./venv/bin/python embed_coco.py --split train --tag clip
./venv/bin/python e2_analysis.py --tag clip              # all seeds fixed inside: query_seed=42, gallery seeds 10000+i, kmeans seeds = seed/seed+1, granularity gallery seed 777
# outputs: ../results/e2_clip.json
# exploratory (post-hoc, labeled): ./venv/bin/python e2_exploratory_kc_scaled.py
# siglip robustness: ./run_siglip.sh  (ViT-B-16-SigLIP webli)
```

Machine-readable: `results/e2_clip.json` (registered), `results/e2_clip_exploratory_kc_scaled.json` (exploratory), `results/e2_siglip.json` (robustness, when done).

## 9. Pending at time of writing

- SigLIP robustness sweep — DONE, §11
- Post-hoc exploratory scale-matched-granularity sweep — DONE, §10
- Registered unimodal extension (D3 closure) — DONE, §12

---
## Progress log (incremental, newest last)
- 2026-08-18 17:45 skeleton written; venv (python3.12) created in e2_real/venv; torch 2.13.0 + open_clip installed; MPS available (Apple M5).
- 17:50 arXiv:2604.18572 fetched (abs + full HTML). Protocol extracted: mutual-kNN (Huh et al. metric), fixed 1024-sample query set, growing gallery (1024 -> WIT-1M -> LAION-15M), k=10 primary (k=1, k=n/100 secondary). Their headline: k=10 alignment 0.135 (1K gallery) -> 0.008 (15M gallery). Their models: unimodal DINOv2 (vision) x OpenLlama (text) — NOT contrastively co-trained.
- 17:55 Data pick: **MS-COCO 2017** (no-credential direct download). Gallery = train2017 (118,287 imgs), queries = 1024 pairs from val2017. Caption = first caption per image (bijective setting, mirrors the main protocol they re-examine).
- 18:00 Network is the binding constraint: images.cocodataset.org ~2.4MB/s aggregate (parallel ranged download plateau). train2017.zip 19.3GB => ~2.5h download. Running in background. open_clip ViT-B-32 laion2b_s34b_b79k checkpoint downloaded + smoke-tested.
- Scale cap: max gallery = 118K (COCO train). Their sweep reaches 15M. Implication stated in §7.
- 18:15 Analysis pipeline written (e2_real/e2_analysis.py): ports weighted_cokernel_residual from exp_discounted_cokernel.py at gamma=1; adds split-half noise-floor control. Registered pre-run choices logged in the script docstring (primary r_perp stat = ||r_perp||_W with sum W = 1; P1 decisive stat = partial Pearson controlling log10 N; P2 = per-scale median split by |r_perp,e|).
- 18:20 Paper protocol confirmed from full text: fixed query set + growing gallery; k=10 primary; their A.1 control shows within-modality mutual-kNN does NOT collapse at scale (so decay is cross-modal specific); their k=n/100 variant stays ~stable ("coarse structural agreement" survives). Both mirrored in our run (k=1/k=10/k=n/100).
- 18:25 Downloads in flight (val ~15 min out, train ~2.3h out at measured ~2.4MB/s). Embedding chain armed to fire when val lands.
- 18:40 Pipeline smoke-tested end-to-end on synthetic shared-latent embeddings (results_smoke/, will be deleted). Key falsifiability check PASSED: on synthetic well-glued data, mutual-kNN alignment decays with N (metric strictness) while r_perp FALLS and converges to the split-half noise floor. So "alignment decays" does NOT mechanically force "r_perp rises" — P1 is a real test, not circular.
- 18:55 val embeddings done (5000 pairs, 92s total on MPS). Interim val-only preview (gallery<=3.9K, disjoint 1024 queries): align_k10 0.295 -> 0.223 -> 0.169 for N=1K/2K/3.9K — CLIP towers align ~2.2x higher than their DINOv2xOpenLlama (0.135 at 1K), expected for co-trained towers; decay shape reproduces. Raw r_perp at tiny N is noise-dominated (fewer pairs/edge => bigger sampling noise) and slightly falls (0.0234->0.0194).
- 18:58 **Pre-registration amendment (before main run, motivated by the val preview — logged per honesty rule):** added derived quantity excess_rperp = sqrt(max(r_perp^2 - noise_floor^2, 0)) (split-half noise-corrected structural residual). P1 will be reported for BOTH raw r_perp (original registration) and excess_rperp (amended), each with partial correlation controlling log10(N). If they disagree, both are shown; no post-hoc selection.
- 19:40 Download incident + fix (tested evidence): 10-connection parallel pull self-congested the ~2.2MB/s uplink (cloudflare speedtest 229KB/s WITH our curls running vs 2.17MB/s with them SIGSTOPped; fresh COCO conn 9.5KB/s during congestion). Not server throttling. Restarted with chunk-pool downloader, 3 workers + slow-connection eviction (curl --speed-limit 300000 --speed-time 20). 1.9GB of 19.3GB banked and resumable.
- 20:55 Second download incident (tested evidence): `curl -C - -r START-END` double-appends on resume -> chunks overshoot target size -> sanity check deletes them -> observed data volume oscillation (8.8GB -> 5.0GB). Fixed: manual remaining-range request + shell append. Audit kept 13 valid partial chunks (1.4GB), dropped 5 oversize. Restarted.
- 23:20 Download completed byte-exact (19,336,861,798). Unzip revealed content corruption in chunks 6-17 (legacy of the -C-/-r double-append era: size-exact but content-shifted). CRC-tested all 118,288 members: 4,647 bad, byte span 1.21-3.44GB. Targeted repair running: re-download only affected chunk ranges, patch zip in place, re-verify CRC.

## 10. Post-hoc exploratory: r_perp at scale-matched granularity (k_c = max(8, N/500))

**LABEL: exploratory, designed AFTER seeing the registered results. Not evidence for P1; recorded per the no-post-hoc-rescue rule.**

| gallery N | k_c | r_perp | excess r_perp | relative (centered) | overdet ratio |
|---:|---:|---:|---:|---:|---:|
| 1,000 | 8 | 0.00975 | 0.00676 | 0.713 | 3.0 |
| 2,000 | 8 | 0.00668 | 0.00329 | 0.500 | 3.3 |
| 5,000 | 10 | 0.00727 | 0.00404 | 0.539 | 4.3 |
| 10,000 | 20 | 0.00952 | 0.00647 | 0.579 | 6.6 |
| 20,000 | 40 | 0.01172 | 0.00798 | 0.607 | 9.8 |
| 50,000 | 100 | 0.01459 | 0.01098 | 0.627 | 15.0 |
| 100,000 | 200 | 0.01665 | 0.01255 | 0.649 | 20.8 |
| 118,287 | 236 | 0.01682 | 0.01259 | 0.647 | 21.5 |

When the carving resolution is scaled with gallery density, the residual RISES with N (excess 2x over the sweep) — but the registered fixed-k_c sweep (§3) shows the N-at-fixed-carving factor pushes the residual DOWN; the rise here is attributable to the k_c factor, i.e., it is the §5 granularity curve re-parameterized along the scale axis. This says a composite story ("the metric probes finer structure as data densifies, and fine structure carries irreducible residual") is CONSISTENT with the data, but the discriminating content of P1 — that the obstruction grows with the constraint set at fixed carving — is what was falsified. Any revival must pre-register an operationalization of "effective resolution of the mutual-kNN metric at scale N" and predict the alignment curve from the granularity curve WITHOUT free coupling — that is E3-grade work, not a footnote.

## Progress log 2 (extension)
- 2026-08-19 00:20 Coordinator-directed REGISTERED EXTENSION (D3 closure): unimodal pair DINOv2 ViT-B/14 (torch.hub) x all-mpnet-base-v2 (sentence-transformers), same COCO data/seeds/stats, P1/P2 predictions and falsifier clauses identical. Pre-registered cross-space discrepancy for the unimodal pair (embeddings live in different spaces): orthogonal Procrustes map img->txt fit on the SAME gallery subset per (N, seed), d_i = 1 - cos(R img_i, txt_i). Alignment metric itself is space-independent (within-modality kNN) and unchanged. Queued behind SigLIP run for MPS.

## 11. Robustness: SigLIP (ViT-B-16-SigLIP, webli) — same registered analyses

| gallery N | align k=10 | align k=n/100 | r_perp | excess r_perp | low-stratum a10 | high-stratum a10 |
|---:|---:|---:|---:|---:|---:|---:|
| 1,000 | 0.2549 | 0.2549 | 0.01839 | 0.01600 | 0.3317 | 0.2403 |
| 2,000 | 0.2129 | 0.2598 | 0.01657 | 0.01327 | 0.2584 | 0.1987 |
| 5,000 | 0.1445 | 0.2568 | 0.01442 | 0.01040 | 0.1665 | 0.1331 |
| 10,000 | 0.1126 | 0.2587 | 0.01218 | 0.00846 | 0.1251 | 0.1042 |
| 20,000 | 0.0848 | 0.2592 | 0.01020 | 0.00665 | 0.0912 | 0.0801 |
| 50,000 | 0.0549 | 0.2589 | 0.00825 | 0.00581 | 0.0538 | 0.0564 |
| 100,000 | 0.0403 | 0.2590 | 0.00706 | 0.00515 | 0.0394 | 0.0414 |
| 118,287 | 0.0372 | 0.2588 | 0.00681 | 0.00514 | 0.0333 | 0.0413 |

- Replicates every CLIP finding: alignment decays 6.9x (k=n/100 flat ~0.259); **r_perp again FALLS with scale** (0.0184 -> 0.0068); Pearson(align, r_perp) = +0.985, partial controlling log10N = +0.523 (p=0.012) — positive again, opposite sign to P1.
- Stratification: low>high differential at small N (0.33 vs 0.24) **reverses at large N** (0.033 vs 0.041 at 118K) — even weaker than CLIP for P2.
- Granularity curve monotone again: r_perp 0.00212 (k_c=4) -> 0.01454 (k_c=512), relative 0.17 -> 0.63.
- Machine-readable: results/e2_siglip.json. **P1/P2 falsification is model-robust across both co-trained pairs.**

## 12. Registered extension: independently-trained unimodal pair (D3 closure)

**Coordinator-directed registered extension (requested as §11; numbered §12 because the SigLIP robustness section landed first). Models: DINOv2 ViT-B/14 (torch.hub, CLS token) × all-mpnet-base-v2 (sentence-transformers) — NOT contrastively co-trained; this mirrors the actual regime of arXiv:2604.18572 (DINOv2 × OpenLlama). Same COCO data, same seeds, same registered stats and falsifier clauses. Cross-space discrepancy pre-registered before the run (Progress log 2): per-subset orthogonal Procrustes img→txt, d_i = 1 − cos(R img_i, txt_i).**

| gallery N | align k=10 | align k=n/100 | r_perp | noise floor | excess r_perp | low-stratum a10 | high-stratum a10 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1,000 | 0.3255 | 0.3255 | 0.03084 | 0.01203 | 0.02836 | 0.4005 | 0.3091 |
| 2,000 | 0.2431 | 0.3275 | 0.03434 | 0.01395 | 0.03137 | 0.2808 | 0.2320 |
| 5,000 | 0.1525 | 0.3275 | 0.03862 | 0.01674 | 0.03480 | 0.1610 | 0.1555 |
| 10,000 | 0.1088 | 0.3276 | 0.03834 | 0.01547 | 0.03507 | 0.1122 | 0.1103 |
| 20,000 | 0.0739 | 0.3283 | 0.03886 | 0.01570 | 0.03555 | 0.0735 | 0.0773 |
| 50,000 | 0.0479 | 0.3285 | 0.03796 | 0.01305 | 0.03564 | 0.0476 | 0.0488 |
| 100,000 | 0.0331 | 0.3290 | 0.03709 | 0.01064 | 0.03553 | 0.0333 | 0.0331 |
| 118,287 | 0.0307 | 0.3288 | 0.03665 | 0.01026 | 0.03518 | 0.0328 | 0.0285 |

**One-line verdict: on independently-trained towers the obstruction signal APPEARS with the predicted sign — this is the surviving regime — but it rises only early (1K→5K) then plateaus, so it cannot quantitatively account for the full decay range; P2 still fails.**

- **r_perp RISES with scale here** (raw 0.0308 → 0.0386 by N=5K, settling ≈0.037; noise-corrected excess 0.0284 → 0.0348 → 0.0352), while the noise floor FALLS (0.0120 → 0.0103) — the rise is structural, not sampling noise. Contrast: CLIP/SigLIP residuals fell monotonically. Coherent mechanistic reading (post-hoc interpretation, labeled): contrastive co-training IS a gluing-repair loop that drives the very violations r_perp measures toward zero; with independent carvings and only a rigid (Procrustes) alignment, the overdetermined residual is exposed.
- **P1 correlation stats (registered): the predicted NEGATIVE sign, strongly** — Pearson(align, r_perp) = -0.812 (p=4.5e-06); partial controlling log10N = **-0.936** (p=1.7e-10); excess: -0.919 / partial -0.881. (Spearman -0.37, p=0.09 — weaker, reflecting the plateau: the relation is not monotone across the whole range.)
- **Honest cap on P1 support**: alignment keeps decaying 5K→118K (0.153→0.031) while excess r_perp is flat (0.0348→0.0352). A rising-then-flat residual does not track a 5x continuing decay point-for-point; the strong partial correlation is carried by the early joint movement and opposite curvatures. P1 here = **partially supported: sign and early dose-response yes, full-range quantitative tracking no.**
- **P2 still FAILS**: low/high strata decay in parallel (~10x each); differential (1.30 at 1K) vanishes by 20K (≈1.0 throughout 20K–100K). No scale-stable low-residual subset exists in any tested model pair.
- **Granularity curve passes again** (third model pair): r_perp 0.01434 (k_c=4) → 0.04673 (k_c=512), relative 0.22 → 0.41; levels ~3-5x higher than CLIP at every granularity.
- Machine-readable: results/e2_unimodal.json. Alignment levels (0.326 at 1K, k=10) are close to CLIP's despite no co-training, and decay 10.6x — the strongest reproduction of the paper's phenomenon in this study.

### Consolidated final verdict across all three model pairs

1. Co-trained towers (CLIP, SigLIP): **obstruction-as-scale-explanation DEAD** — r_perp falls with scale, positive partials. No escape hatch there.
2. Independently-trained towers (DINOv2×mpnet — the paper's regime): **surviving regime** — residual rises early with the predicted sign and strong registered correlation (partial −0.94), but plateaus while alignment keeps decaying, and stratification shows no differential decay anywhere.
3. Granularity dose-response (coarse glueable → fine irreducible): **passes in all three pairs** — the robust surviving claim, now with the co-training-as-repair-loop contrast as its sharpest corollary: the obstruction is real, exposed in independent carvings, and suppressed (not just hidden) by co-training.

Follow-up bar for any revival of the full scale-explanation (E3-grade, pre-register first): predict the alignment curve from the granularity curve via an explicit model of the mutual-kNN metric's effective resolution at scale N, with no free coupling; and test whether the unimodal plateau breaks upward at scales beyond 118K.
