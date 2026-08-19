# Multimodal Gluing Obstruction: is the cross-modal gap an optimization defect or a structural residual of lossy projection? (E1/E2 verdict)

Date: 2026-08-18 → 2026-08-19

Public index: [Theory Mainline](../THEORY.md) · Format: [Claim-Receipt](../CLAIM-RECEIPT.md) · Upstream: [THEORY v3 cokernel obstruction](2026-08-19-information-dynamics-theory-v3-cokernel-obstruction.md)

> **Cognitive state (per claim, honest split):**
> - **Mechanism (E1, synthetic):** 🟢 survived-stress-test · **Confidence 0.9** — threshold exactly at constraint/dof ratio ρ=1; InfoNCE / xNCE / oracle all stop above the analytic floor; 10× longer training does not lower it. [RESULTS-E1](2026-08-19-multimodal-gluing-obstruction/RESULTS-E1.md)
> - **"Their scale-decay curve is our residual curve" (registered P1/P2 on CLIP & SigLIP):** 🔴 **falsified, withdrawn** — r_perp *falls* with data scale on co-trained towers (Pearson +0.97 with alignment, sign opposite to prediction); no differential stratum decay in any model pair. [RESULTS-E2](2026-08-19-multimodal-gluing-obstruction/RESULTS-E2.md)
> - **Granularity dose-response (coarse glueable / fine irreducible):** 🟢 survived in all three model pairs · **Confidence 0.6** (publishability, pending a sheaf prior-art sweep; does not yet discriminate our account from "fine structure is modality-specific")
> - **Weakened P1 on independently-trained towers (DINOv2 × mpnet — the paper's regime):** 🟡 speculative · 0.7 — residual rises early with the predicted sign (partial r = −0.94) then plateaus; no full-range tracking
> - **Corollary "contrastive co-training is a gluing-repair loop that suppresses the obstruction":** 🟡 speculative · 0.7 — post-hoc reading, single dataset/scale band
>
> provenance: theory transplant of the THEORY-v3 residual `r_perp` onto cross-modal constraint graphs; pre-registered predictions + falsifiers; fixed seeds, reproduction commands in RESULTS files · **evidence:** E1 (`e1_structural.json`, `e1_training.json`, falsifier runs), E2 (`e2_clip.json`, `e2_siglip.json`, `e2_unimodal.json`) mirrored under `results/` · **prior-art:** Platonic Representation Hypothesis (Huh et al. 2024) and its re-examination "Back into Plato's Cave" (arXiv:2604.18572); modality-gap-as-InfoNCE-mode-failure (arXiv:2607.10698, xNCE); sheaf-Laplacian multimodal fusion (2506.22374, 2508.09717, 2606.19529, 2601.15320) — they use the sheaf Laplacian to *minimize* inconsistency, none treats the obstruction as a forced, dose-responsive diagnostic; multi-view identifiability results (2605.19135, 2602.23785, 2605.17827) are positive results with no computable impossibility measure.
>
> **Owner decision (2026-08-19): parked as a handle.** No E3, no outreach. Revival conditions at the end.

## 0. One-paragraph version

Two modalities are two lossy projections of one latent. Demanding a shared embedding demands one potential that satisfies every cross-modal consistency constraint at once. THEORY-v3 shows lossy aggregation turns an exact latent field into an overdetermined observation-level field with generically no single potential; the residual `r_perp` is computable and invariant to potential-based repair. We bet that the unexplained anomaly in arXiv:2604.18572 — cross-modal alignment *decaying* with data scale — was this overdetermination transition. **The synthetic mechanism held; the real-model scale story did not.** What survives is a granularity statement: at coarse carving the cross-modal discrepancy field is largely potential-fittable, at fine carving most of it is shaping-irreducible (~8× monotone rise across k_c 4→512, in CLIP, SigLIP, and DINOv2×mpnet). The sharpest surviving corollary is that contrastive co-training *actively* drives the very violations `r_perp` measures toward zero — the obstruction is exposed only under independent carvings plus a rigid (Procrustes) alignment.

## 1. Field context (checked 2026-08)

- Multimodal *understanding* is commoditized; unified any-to-any tokenization and AR+Diffusion backbones are standard. No theoretical vacancy at that layer.
- What is moving is **world models + action (VLA)** with two routes — render-to-predict (video-generation world models) vs compress-to-understand (JEPA/Dreamer). The disagreement is *which layer to model* = which carving. That is our territory.
- The acknowledged bottleneck is not the LLM but the **vision encoder's representational capacity**: encoders provably drop high-frequency detail, the projector compresses again; coarse tasks fine, fine-grained tasks collapse. **Projection loss is already an accepted phenomenon; nobody measures it as a structural obstruction — it is treated as an engineering defect to be fixed.**

## 2. The sharp interface

**Anomaly.** arXiv:2604.18572 re-tests the Platonic Representation Hypothesis: cross-modal alignment holds at ~1K samples and *decays significantly* at millions; what remains is coarse semantic overlap with inconsistent fine structure; same for text–audio and text–video. The authors state they have no mechanistic explanation.

**Mainstream explanation of the related modality-gap phenomenon.** InfoNCE at low temperature with independent encoders → mode-failure, *fixable* (xNCE); or cone effect / data bias. All "optimization-defect" accounts.

**Our account (direct transplant of THEORY-v3).** Two modalities = two lossy projections of one latent; a shared embedding = one potential satisfying all cross-modal constraints; after coarse-graining the field is overdetermined; `r_perp = r − D(DᵀWD)⁺DᵀW r` is generically nonzero once constraint count exceeds latent dof. **Prediction: alignment decay is an overdetermination transition with an irreducible residual floor that no loss change removes.**

| | Optimization-defect view (field) | Obstruction view (ours) |
|---|---|---|
| after fixing the loss | gap → 0 at any scale | residual drops to a **nonzero floor** rising with constraint/dof |
| scale curve | monotone improvement or flat | **threshold**: ≈0 while constraints ≤ latent dof, jumps to generically nonzero after |
| which pairs align | no prediction | only structure in the **common complement of the two projection kernels** ⟹ predicts "coarse aligns, fine does not" |
| remedy | change the loss | change the carving, or accept **partial gluing** explicitly |

## 3. Experiments (pre-registered; full numbers in the linked RESULTS files)

**E1 — synthetic.** Known latent (d dims) → two known lossy projections → per-modality encoders → `r_perp` on the cross-modal constraint graph, sweeping constraint/dof ratio ρ. *Registered:* residual ≈ numerical floor for ρ<1, jumps for ρ>1, and the best loss (incl. xNCE) cannot lower it. *Falsifier:* residual → 0 monotonically with training/scale.
**Verdict: PASS.** Threshold at ρ=1; InfoNCE/xNCE/oracle stop above the analytic floor; 10× training does not lower it; under generic potentials the obstruction is stronger (generically nonzero even at ρ<1 when the projections' spans do not cover the latent).

**E2 — real models, Plato's-Cave protocol on MS-COCO (118K).** CLIP ViT-B/32 (registered), SigLIP (robustness), DINOv2 × all-mpnet (registered extension = the paper's independently-trained regime). Mutual-kNN alignment vs gallery size, `r_perp` on a k-means cluster constraint graph (k_c=64), noise floor by split-half, stratification by per-edge residual, granularity sweep k_c 4→512.
*Registered P1:* `r_perp` rises with scale and correlates negatively with alignment. *Registered P2:* low-residual stratum does not decay while high-residual stratum decays. *Falsifier:* either fails ⟹ obstruction does not explain the decay.

| Model pair | Their decay reproduced | P1 (residual rises, tracks decay) | P2 (differential stratum decay) | Granularity curve |
|---|---|---|---|---|
| CLIP (co-trained) | yes, 8.6× (1K→118K) | **FAIL** — residual falls, Pearson +0.97 | **FAIL** — parallel ~8–10× decay | PASS, 0.0026→0.0212 |
| SigLIP (co-trained) | yes | **FAIL** (same sign) | **FAIL** | PASS |
| DINOv2 × mpnet (independent) | yes, 10.6× — closest to the paper | **partial** — rises 1K→5K with predicted sign (partial r = −0.94), then plateaus while alignment keeps decaying 5× | **FAIL** | PASS, 0.0143→0.0467 |

**Falsifier fired on the registered clauses.** The sharpest sell — "their decay curve is our residual curve" — is retired. The mundane explanation stands: at fixed carving, the mutual-kNN metric's effective resolution tightens with N (their k=n/100 curve is flat and ours reproduces that flatness). What survives is the granularity dose-response and the co-training-as-repair contrast.

## 4. What this buys the mainline

- The gluing-obstruction claim **does not depend on the hysteresis bet** that the agency and self-boundary notes share ([Agency: second-order persistence](2026-08-19-agency-second-order-persistence.md)); it is an independent leg for the "lossy projection ⇒ forced residual" trunk. That structural gain is retained regardless of the E2 outcome.
- Multimodality also gives the set-valued self-boundary order parameter a natural carrier ("which channels currently count as *my* input") — speculative, not a deliverable here.

## 5. Revival conditions (agent-set; owner parked the line)

- Literature reports a forced / dose-responsive sheaf obstruction for multimodal fusion (then: cite, don't rebuild).
- A world-model / VLA line needs a computable carving signal for "which channels should be required to align" — start from the two surviving claims (granularity dose-response; co-training as repair loop).
- E3-grade bar for reviving the full scale explanation (pre-register first): predict the alignment curve from the granularity curve via an explicit model of mutual-kNN effective resolution at scale N, **with no free coupling**; test whether the independent-tower plateau breaks upward beyond 118K.

Attachments: [README](2026-08-19-multimodal-gluing-obstruction/README.md) · [RESULTS-E1](2026-08-19-multimodal-gluing-obstruction/RESULTS-E1.md) · [RESULTS-E2](2026-08-19-multimodal-gluing-obstruction/RESULTS-E2.md) · `results/*.json`. Code (`e1_synthetic/`, `e2_real/`) available on request.
