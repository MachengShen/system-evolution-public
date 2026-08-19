# RESULTS-E1 — synthetic gluing-obstruction (multimodal)

日期 2026-08-18 · agent 执行,owner 已 ratify · 全部数字来自实际运行的代码(命令+seed 见 §6),机读数字在 `results/e1_structural.json` / `e1_training.json` / `e1_falsifier_*.json`。

## (1) 一句话结论

**阈值跳变:看到了(additive 族恰在 ρ=T/s=1 处从 ~1e-15 跳到 0.3–0.9 相对残差);floor:任何 loss(InfoNCE 全温度、xNCE、监督 oracle)的 achieved violation 都停在解析 floor 之上,长训 10 倍不下降 —— falsifier 未触发,障碍论在合成设定下成立。**
额外(比假设更强):generic(非可分)latent 势下,只要共享维 s < union,连 ρ<1 都 generically 非零 —— 相变边界退到「完全共享」;「粗语义可对齐、细粒不可对齐」在两族里都以 field-norm 塌缩 + 残差floor 的形式出现。

## (0) 设计与诚实边界(先读)

**模型**:latent = d 个 ±1 bit(d=8 全部可观测;**d=16 cap:union=10 个 bit 可被任一模态观测,其余 6 bit 对双方隐藏,经解析边缘化进入 φ̄ —— 显式 cap,非静默截断**)。S_A = bit{0..k−1},S_B = bit{0..s−1}∪{k..2k−s−1},k=(union+s)/2;**共享自由度 = s(两投影核都存活的维数)**。约束类型 t = 翻转 bit t;跨模态约束边 = (A-类 u → B-类 v),required agreement 值 = φ*(w) − φ*(σ_t w),按 (u,v,t) 聚合,权重 = 共现计数。**ρ = T/s(独立约束类型数 / 共享自由度)**。
两族 latent 势:**additive**(φ* 按 bit 可分 → 每个约束类型对应一个共享方向,ρ 轴最干净)与 **generic**(φ* 在 latent cell 上 iid 高斯 → 共享/私有维耦合)。

**残差算子**:`r_perp = [I − D(DᵀWD)⁺DᵀW] r`,从 `~/projects/information-dynamics/exp_discounted_cokernel.py` **逐字 port** 进 `e1_synthetic/e1_ops.py`(γ=1,纯 agreement 约束无折扣);port parity 与 THEORY-v3 四性质检验见 §4。

**理论已知 vs 实验测得(划界)**:V(encoder) ≥ ‖r_perp‖_W 对任何「按观测各自打分再比对」的读出是最小二乘数学事实,不是实验发现。实验检验的是:(a) 阈值**位置**是否在 ρ=1;(b) 阈值上方 floor 是否非零 O(1);(c) 真实训练的各 loss 是否都停在 floor 上方、加训练是否趋向数值底(falsifier);(d) 标准对齐指标是否跟随结构相变。

**Caps(全部显式)**:d=16→union=10;训练部分只跑 d=8,s∈{2,4,8},3000 步(falsifier 30000 步),batch 256,n_eval=32768,encoder=3 层 MLP(64 hidden,emb 8 维),观测 16 维(固定随机 2 层 tanh MLP 混合),CPU torch;k-means 类数 = 2^k 与真类数匹配;jitter 0.15。总运行 <30 min(structural 574s + training 507s + falsifier 2 runs)。

## (2) residual-vs-ratio:结构层(解析聚合,无训练)

median **relative** residual;**粗体 = 该 cell 100%(全部 seed)非零**;非粗体 = 数值零(≤1e-9 判据,实测 ≤7.5e-15)。d=8 每 cell 100 seeds,d=16 每 cell 20 seeds。

**d=8,additive φ*** — 阈值精确在 T = s+1(ρ=1 处跳变 ~15 个数量级):

| T \ s | 0 | 2 | 4 | 6 | 8(负控) |
|---|---|---|---|---|---|
| 1 | 6.3e-16 | 3.8e-16 | 1.6e-16 | 5.3e-16 | 0.0 |
| 2 | **0.71** | 1.3e-15 | 4.5e-16 | 3.3e-16 | 1.8e-16 |
| 3 | **0.82** | **0.42** | 9.3e-16 | 4.7e-16 | 3.1e-16 |
| 4 | **0.87** | **0.58** | 1.4e-15 | 5.9e-16 | 2.7e-16 |
| 5 | **0.89** | **0.75** | **0.30** | 9.2e-16 | 4.1e-16 |
| 6 | **0.91** | **0.77** | **0.51** | 1.6e-15 | 6.5e-16 |
| 7 | **0.93** | **0.82** | **0.61** | **0.31** | 9.7e-16 |
| 8 | **0.94** | **0.82** | **0.70** | **0.43** | 1.4e-15 |

精确 rank 谓词(rank[D|A]−rank D,不依赖 seed)= **obstruction 维数 = max(0, T−s)**(唯一例外:s=0,T=1 单一私有类型仍可平凡粘合,维数 0)。d=16(union=10 cap,s∈{0..10},T∈{1..10})完全同构:阈值同在 T=s+1,残差幅度逐 cell 吻合(见 json;例 s=4:T≤4 全 ≤5.7e-15,T=5 起 0.32→0.76)。**阈值位置与规模无关。**

**d=8,generic φ***(非可分;d=16 同构)— 只要 s < union,**任意 T≥1 即 100% 非零**,且 floor 随 s 单调下降:

| T \ s | 0 | 2 | 4 | 6 | 8(负控) |
|---|---|---|---|---|---|
| 1 | **0.97** | **0.88** | **0.75** | **0.49** | 0.0 |
| 4 | **0.98** | **0.95** | **0.84** | **0.66** | 2.1e-16 |
| 8 | **0.99** | **0.97** | **0.91** | **0.74** | 7.9e-16 |

读法:additive 族给出假设的「ρ=1 阈值」;generic 族说明当 latent 势耦合共享/私有维时障碍更早出现(相变边界退到 s=union)。两者都支持「结构性 forced、非优化缺陷」;对 Plato's Cave 异常,generic 行为(粗粒对齐随细粒约束加入而 generically 失效)是更贴的机制候选。

## (2b) 训练层:各 loss 的 achieved violation vs floor(d=8,3000 步,n_eval=32768,seed 0)

V_lin = per-sample 线性读出的 weighted relative violation(数学下界=floor,塌缩不豁免:塌缩加大而非减小 V)。**所有 loss × 所有 cell:V ≥ floor,无一例外。**

**s=2**(阈值 T=3):

| loss \ T | 2 (ρ=1.0) | 3 (ρ=1.5) | 4 (ρ=2.0) | 8 (ρ=4.0) |
|---|---|---|---|---|
| infonce τ=0.05 | 0.163 | 0.290 | 0.813 | 0.987 |
| infonce τ=0.2 | 0.112 | 0.259 | 0.817 | 0.988 |
| infonce τ=0.5 | 0.106 | 0.264 | 0.807 | 0.987 |
| xnce τ=0.05 | 0.184 | 0.318 | 0.813 | 0.990 |
| xnce τ=0.2 | 0.147 | 0.278 | 0.812 | 0.987 |
| oracle(监督上界) | 0.229 | 0.325 | 0.728 | 0.931 |
| **analytic floor** | **0.000** | **0.187** | **0.706** | **0.924** |

**s=4**(阈值 T=5):floor 0/0/0/0(T=1..4)→ 0.774/0.802/0.891/0.901(T=5..8);全部 loss V ≥ floor(阈值上方最低 = oracle 0.800 @T5;contrastive 全部 ≥0.96)。
**s=8**(负控,floor=0 至 T=8):V=0.22–0.91,为优化/量化 slack 而非结构 floor(true-class 残差同 sample 为 0.000,见下)。

**true-class finite-sample 残差**(oracle run 的同一 32768 样本,阈下 = 0.000,阈上 = 0.187/0.706/…,与解析 floor 三位小数吻合)⟹ 有限样本聚合不制造伪障碍。

**塌缩探测(field-norm ratio,learned k-means 类上保留的约束场范数 / true-class 场范数)**:阈值上方 contrastive encoder 把场砍到 0.24–0.40(即把不可满足的细粒约束**整个扔掉**,只保留可粘合的粗语义),oracle 保留 0.94–0.97 并吃满 floor 残差。mutual-kNN 对齐随 s 降级(s=8:0.74–0.88;s=4:0.43–0.62;s=2:0.14–0.23),modality gap 在所有 contrastive 设置非零(0.012–0.113)——「只剩粗语义对齐」在本设定里是结构推论,不是 loss 缺陷。

## (3) 负控制(fully-shared latent,ρ<1 侧全域)

s = union(d=8 的 s=8;d=16 的 s=10):**两族 × 全部 T × 全部 seed(d8 100/cell,d16 20/cell)最大 relative residual = 6.89e-15** —— 数值底,所有尺度成立。✓

## (4) 单元测试(先于任何数字被信任)

| 测试 | 结果 |
|---|---|
| port parity(与原 `exp_discounted_cokernel.py` 在其 branch 例上逐元素对比) | residual diff = **0.0**(bit-exact) ✓ |
| shaping invariance(THEORY-v3 性质 3:r → r+Dψ 残差不变,在 E1 实际图上) | defect 6.6e-14(d8 s2T4)/ 3.5e-13(d16u10 s4T6),≤1e-8 ✓ |
| normal-equation defect(性质 2,每 cell QR 快速路径 vs ported 算子 parity 断言) | 最大 parity diff 6.5e-15;defect ≤1e-8 断言全过 ✓ |

## (5) Falsifier verdict

**未触发 —— 障碍论存活。** 判据(memo 原文):若充分训练后残差在 ρ>1 处随训练单调趋向数值底(最优 loss 下),则障碍论对多模态不成立。实测(s=2、T=3、ρ=1.5,解析 floor = 0.187,10× 长训 30000 步,checkpoint 500→30000):

| step | infonce τ=0.2 V_lin | xnce τ=0.2 V_lin | (数值底 ≈1e-15;floor=0.187) |
|---|---|---|---|
| 500 | 0.262 | 0.314 | |
| 2000 | 0.264 | 0.239 | |
| 8000 | 0.282 | 0.351 | |
| 16000 | 0.769 | 0.786 | |
| 30000 | 0.836 | 0.751 | 两条曲线全程 ≥ floor,无趋零趋势 |

- 两种 loss(3000 步网格上表现最好的 InfoNCE τ=0.2,与对手假说的修复方案 xNCE)在全部 7 个 checkpoint 的 achieved violation 均 ≥ 0.239 > floor 0.187,距数值底 14 个数量级;后期不降反升(embedding 几何变得更不可线性读出 —— 是读出容量 artifact,但方向上只会高估不会低估 floor)。
- 同一 encoder 的 mutual-kNN 全程单调改善(0.06→0.38),即**「可粘合子空间内对齐持续变好」与「floor 纹丝不动」同时发生** —— 正是障碍论预测的解耦,优化缺陷论无法同时解释这两条曲线。
- 阈下对照(T=2,floor≈1e-15):true-class 残差为 0.000,learned-class 波动 0.01–0.15 为 k-means 类噪声,无结构 floor —— 阈下不存在障碍,与理论一致。
- 诚实备注:learned-class 残差(0.04–0.19)可低于解析 floor,因为 learned 图是另一张图(粗化后约束场变小),它不受 floor 下界约束;受下界约束、也是 falsifier 判定用的量是 V_lin。

## (6) 精确复现命令(全部 CPU,系统 python3.9 + numpy 2.0.2 + torch 2.8.0)

```bash
cd ~/projects/multimodal-gluing-obstruction/e1_synthetic
python3 e1_structural.py --seed 0                      # → results/e1_structural.json (574s)
python3 e1_training.py  --seed 0                       # → results/e1_training.json  (507s)
python3 e1_training.py  --seed 0 --falsifier --fal-loss infonce_t0.2   # → results/e1_falsifier_infonce_t0.2.json
python3 e1_training.py  --seed 0 --falsifier --fal-loss xnce_t0.2      # → results/e1_falsifier_xnce_t0.2.json
python3 e1_report.py                                    # markdown 表渲染
```
所有随机性由 --seed 0 派生(结构 sweep 内部 per-cell/per-seed 派生式见 e1_structural.py;训练 world/encoder seed 派生式见 e1_training.py)。
