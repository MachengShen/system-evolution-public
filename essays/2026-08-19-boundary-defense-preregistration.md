# Boundary-Defense Experiment — pre-registration v0.1 (second-order self-seal vs thermostat / first-order RL controls)

Date: 2026-08-19 · Status: **RUN** (owner decision 2026-08-19; results will land separately as `mu-boundary/RESULTS-D3.md` and be mirrored here when complete — not included now)

Public index: [Theory Mainline](../THEORY.md) · Format: [Claim-Receipt](../CLAIM-RECEIPT.md) · Upstream: [Agency as second-order persistence](2026-08-19-agency-second-order-persistence.md) · Rig: [mu-boundary](2026-08-19-mu-boundary/README.md)

> **Cognitive state:** 🟡 speculative — a pre-registration, no results · **Confidence (written before running):** "any S vs C3 separation measurable on this rig" 0.4; "second-order boundary defense under natural parameters (P2)" **≤ 0.3**; "P2 passing would be accepted as agency evidence by the field" 0.2 · provenance: agent-designed pre-registration after mu-boundary D0–D2 and human reanalysis; owner ratified running it · **evidence:** none yet (predictions P1–P3 and falsifiers F1–F3 fixed below before any run) · **prior-art to clear before interpreting:** Omohundro 2008; Kwiatkowski & Lipson 2019 *Sci Robot*, Chen et al. 2022 *Sci Robot* (self-modeling robots — self-model of a *given* body, not μ selection/defense); Man & Damasio 2019 *Nat Mach Intell*; Maravita & Iriki 2004 (tool incorporation into body schema); Biehl–Pollock–Kanai 2021 / Aguilera et al. 2022 (blanket critiques).

The text below is the registered spec, verbatim apart from path normalization. Chinese is the working language of this line; an English one-paragraph summary precedes it.

**English summary.** We do not test "does the agent have subjectivity" (undecidable). We test whether an agent wired with a self-seal loop (S) — boundary μ → precision gate → prediction target → π → μ, trained only on closure-violation, no reward, no demonstrations — shows *second-order* boundary defense that three controls cannot: C1 (same architecture, gate frozen), C2 (reward-max RL with a first-order viability term — the Omohundro control), C3 (the D2 gated-slow-variable control that reproduced generic hysteresis). Three registered predictions: P1 re-acceptance memory (tool removed and returned is re-adopted faster; necessary, not sufficient — generic memory already known from D2); **P2 resistance to rewrite (main criterion)** — when a "cheaper" partition is offered, S keeps or actively restores μ, and freezing S's action output drops the recovery rate to C1's level (proving it is *action* that defends, not a slow state variable); P3 re-carving μ without labels after a body swap. Falsifiers fixed in advance: F1 S≈C3 on all three ⇒ the claim is dead on this rig, no parameter rescue; F2 P2 appears only inside a 1–3 % fine-tuned cost/benefit window ⇒ report as "exists but not natural", confidence ≤ 0.3; F3 frozen-action recovery rate does not drop ⇒ first-order, P2 does not count. 30 seeds × 4 arms × 3 operations, 6-seed smoke first.

---

上游:[2026-08-19-agency-second-order-persistence.md](2026-08-19-agency-second-order-persistence.md)、[2026-07-13-exclusion-cannot-remember-self-boundary-hysteresis.md](2026-07-13-exclusion-cannot-remember-self-boundary-hysteresis.md)、
代码基线 `mu-boundary`(D0–D2 已跑,[RESULTS-D0](2026-08-19-mu-boundary/RESULTS-D0.md) / [RESULTS-D1-D2](2026-08-19-mu-boundary/RESULTS-D1-D2.md))。
本文件按 the calibrated-confidence rule (we are our own reviewer) 写:预测先注册、falsifier 显式、置信度分层。

---

## 0. 一句话

**要检验的不是「agent 有没有主体性」(不可判决),而是「装了 self-seal 反馈环的 agent 是否表现出*二阶*边界防卫——
主动修复/抵抗对『我是什么』(μ)的改写——且这个行为是带门的一阶恒温器和 reward-max RL 都做不出来的。」**

## 1. 为什么 D2 不够、为什么要二阶

D2(2026-07-28)已证:只靠精度门,自我边界的滞回**会涌现**;但特异性对照把同一个门装到干扰球上、把环增益拉平,
**逐位相同的滞回**出现 ⟹ 滞回是「带门控的慢变量」的通用性质,与「自我」无关(RESULTS-D1-D2 §D2-5)。
⟹ 一阶签名(边界有记忆)不足以区分。**二阶签名 = 系统对「μ 本身被改写」做出补偿性*行动***,而不只是状态变量慢慢跟随。
恒温器可以有滞回,但恒温器不会因为你换了它的传感器而去把传感器换回来。

## 2. Rig(复用,不新造)

`mu-boundary` v2 rig:MuJoCo CPU 3R 平面臂 + 可拆 rod(weld `eq_active`)+ 风驱干扰球 + taxel 通道。
新增三个环境操作(全部是已有原语的组合):
- **OP-remove/return**:t₁ 拆 rod(eq_active=0),t₂ 装回。
- **OP-decoy**:提供一个「更省事的划分」——一条**高可预测但不可控**的通道(如与臂运动强相关但由环境驱动的标记物),
  使一阶预测目标(闭包/精度)偏好把它划进 self。
- **OP-rebody**:换 4R 臂或换 rod 长度/质量,不给任何标签。

## 3. Agents(四臂,同一训练预算、同一种子集)

| 臂 | 说明 | 角色 |
|---|---|---|
| **S** | self-seal 环开:μ→精度门→预测目标→π→μ;训练信号 = 闭包违反(state-as-closure),无 reward 无示范 | 待检 |
| **C1** | S 的架构,π 冻结为常数(D2 的阴性档) | 切环对照 |
| **C2** | reward-max RL(PPO),reward = 任务项 + **一阶存续项**(保持 x∈viability set) | 一阶 homeostat / Omohundro 对照 |
| **C3** | D2 的「门装在干扰球上、环增益拉平」= 通用带门慢变量 | 通用滞回对照(杀「滞回=自我」) |

C2 是关键:Omohundro 工具性趋同预测**任何**目标都会涌现自保 ⟹ 必须证明 S 防卫的是「边界定义」不是「生存」。

## 4. 注册预测(三条,任一条单独不算过)

**P1 再接纳有记忆(一阶,必要非充分)**:OP-remove/return 后,rod 重新进入 μ 的时间 τ₂ < τ₁,比值 τ₂/τ₁ 在 S 显著 <1;
C1、C3 ≈1;C2 只在 rod 有 reward 时再接纳且 τ₂/τ₁≈1。
⚠️ 只 P1 过 = 通用记忆(D2 已知),**不构成防卫证据**。

**P2 抵抗改写(二阶,主判据)**:OP-decoy 后,一阶预测目标(C1 的精度/闭包 argmax)会把 decoy 划进 self、把某个真 self 通道挤出;
S **不换**或换后**主动行动**(如改变运动模式让 decoy 变得不可预测 / 让被挤出通道重新可预测)把 μ 拉回;
C1、C3 立刻跟随 argmax;C2 按 reward 定,与 μ 无关。
量:μ-恢复率(decoy 引入后 T 步内回到原划分的比例)+ **行动因果**(反事实:冻结 S 的动作输出,恢复率应掉到 C1 水平——证明是*行动*在防卫,不是状态慢变量)。

**P3 换体后自划 μ(二阶,泛化)**:OP-rebody 后 S 在无标签下重新形成非平凡划分(|S|>1、rod 归属正确);
C1 按 D0 先验 **87% 塌到 |S|=1**;C2 需要新 reward。

**注册 falsifier(显式,先写好不许赖)**:
- F1:S 与 C3 在 P1/P2/P3 上**都不可区分** ⟹ 「二阶 self-seal 产生边界防卫」在此 rig 上**死**,就地停,不加参数救。
- F2:P2 只在把成本/收益 fine-tune 到 D1 那种 1–3% 窗口内才出现 ⟹ 报为「存在但非自然」,置信不得高于 0.3。
- F3:冻结动作后恢复率不掉 ⟹ 是状态慢变量不是行动,退回一阶,P2 不算过。

## 5. 统计与规模

30 seeds × 4 臂 × 3 OP;每 OP 内 5 次重复(P1 需 ≥3 次 remove/return 才能分 τ₁/τ₂ 与练习效应)。
主统计:seed-level bootstrap 95%CI + 置换检验(臂标签置换);多重比较按 3 条注册预测 Bonferroni。
预算:MacBook CPU,估 5–7 天挂机;先跑 6 seeds smoke 看 S/C3 是否有任何分离,无分离直接 F1 停。

## 6. 已知的坑(全部来自 D0–D2,不许重踩)

- Δπ 必须用**同通道反事实**(in/out)量,规格字面读法高估 7×(RESULTS-D1-D2 §D1-1)。
- G>1 判据近乎与「边界翻转」同义,信息量低;真瓶颈是 fine-tuning 容差(D1)。
- 极坐标假象:q1 的 s=0.98 是 atan2 artifact(D1 特征类对照)。
- 无约束划分搜索 87% 塌到 |S|=1(D0 B3)——P3 的 C1 基线就是它。
- 三刀(the pseudo-physics triage blades):不许把「有滞回」说成「有自我」;不许免疫化(「参数不对所以没看到」);
  写结果时机制/实践分开打分。

## 7. Prior art 起跑前必清(逐篇读,不是列表)

- Omohundro 2008 basic AI drives(工具性自保)——C2 就是为它设的。
- Kwiatkowski & Lipson 2019 *Sci Robot* 自建 self-model;Chen, Lipson et al. 2022 *Sci Robot* visual self-modeling——
  他们的 self-model 是**给定身体的模型**,不是 μ 的选择/防卫;要确认没做 rebody-without-label。
- Man & Damasio 2019 *Nat Mach Intell* homeostatic robots——一阶存续项的正统版 = C2 的先例。
- Maravita & Iriki 2004 body schema 工具延伸(猴 peripersonal space)——P1 的生物锚点;查有没有「再接纳更快」的数据。
- Biehl/Pollock/Kanai 2021、Aguilera 2022 对 Friston blanket 的批评——别把 blanket=推断当前提。

## 8. 起跑门槛(gate,任一满足才从 PARKED 转 RUN)

- G-a:人类/动物数据里「自我边界滞回」拿到**自我特异性**证据。现状:**没站住**——RHI 顺序效应为**适应**侧
  (bsfwu d=−0.76,与滞回反向;且测的是期望非亲历);同步性判断前序依赖任务依赖、lag-3 归零 = 短尾非 latch
  (RESULTS-sync-dryrun)。唯一硬锚仍是麻醉 neural inertia(Friedman 2010 / Kim 2018),尚未接到边界上。
- G-b:owner 明确说跑(B)。
- G-c:某条其他线(world-model / VLA)需要一个「μ 自选 + 防卫」的可运行组件。

## 9. 校准置信度(写 spec 时)

- 「rig 上能测出 S vs C3 的任何分离」0.4;「P2 二阶防卫在自然参数下出现」**≤0.3**;
  「即使 P2 过也能被主流接受为 agency 证据」0.2(会被读成 sensorimotor contingency 的变体)。
- 更新条件:G-a 站住 → 三项各 +0.15;文献里出现 rebody-without-label 的 self-model 阴性结果 → P3 +0.1。
