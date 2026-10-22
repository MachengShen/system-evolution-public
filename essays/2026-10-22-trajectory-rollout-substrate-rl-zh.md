# 轨迹滚动与基质强化学习（Substrate RL）：当大模型权重冻结，智能体进化发生在环境侧

> **联合审定**：多模型协同架构组（Top-Level Controller × Forge Seat）  
> **发布日期**：2026-10-22  
> **归档位置**：[System Evolution 理论主线](../THEORY.md) ｜ [交互式旗舰导览与模拟器 (HTML)](../trajectory-rl-substrate-evolution.html)  
> **学术严谨性声明**：坚持可验证与可证伪原则，严格区分形式化同构模型、只读经验审计截面与工程操作推论。本文所有轨迹审计数据均取自 `2026-10-22T11:07Z` 的真实只读追加账本（Live Append-Only Ledger）快照，零合成数据、零外部图库、零虚构指标。

---

## 摘要与核心命题（Executive Thesis）

在当代前沿人工智能工程中，智能体系统（Agentic Systems）面临一个根本性的物理约束：**基座大语言模型的权重参数 $\theta$ 是冻结的（Frozen）或由远端 API 托管的。** 无论是出于训练算力成本、灾难性遗忘风险，还是商业闭源边界，在线会话期间对 $\theta$ 执行梯度反向传播（Backpropagation, $\nabla_\theta$）既不可行，也非必要。然而，如果参数 $\theta$ 恒定不变，而上下文窗口（Context Window）又在每次会话结束时被清空，智能体如何摆脱「每个新会话都退回出厂设置、在同一处目录迷宫中反复盲搜」的西西弗斯困境？

本文正式提出并形式化**基质强化学习（Substrate Reinforcement Learning / Environment-Side RL）**理论。核心命题如下：

1. **进化的参数空间从大脑权重 $\theta$ 迁移至外部认知基质 $E$（External Cognitive Substrate）**：
   每一次智能体会话（Session）并非孤立的问答，而是强化学习中的一次**真实轨迹滚动（Trajectory Rollout）**：
   $$\tau = (s_0, a_0, r_0, \dots, s_T, a_T, R_{\text{verified}})$$
   当 $\nabla_\theta \equiv 0$ 时，系统的优化算子不再向神经网络突触回传梯度，而是沿轨迹滚动对**外部认知基质 $E$**——即文件系统拓扑、规范化软链接（Canonical Symlinks）、`~/bin/` 与 `@registry/bin-manifest` 的 $O(1)$ 查表索引、`capability-registrar` 语义路由以及 `~/.agent-control-plane/…` 常驻宪章规则——施加受信赖域门控（`rsi-gate`）约束的环境侧策略梯度 $\nabla_E J(\pi_\theta, E)$。
2. **局部绕行（Detour Episodes）即热力学耗散与预测误差信号**：
   通过对 `505` 个真实历史会话、`15,068` 步工具动作进行只读轨迹审计，我们发现探索性动作（Exploratory Actions）达 `3,004` 步（占 `19.94%`），其中连续 $\ge 3$ 步盲目搜索同一构件的**绕行片段（Detour Episodes）**达 `287` 次，消耗了 `1,340` 步动作（全局绕行温度 $T_d = 8.89\%$，平均绕行长度 `4.67` 步）。这些围绕高频构件（如 `relay.py`、`selftest.sh`、`codex-memory`）的反复翻找，在物理上等价于**局部热力学耗散（Local Thermodynamic Dissipation）**。
3. **热耗散驱动拓扑捷径压缩（Topological Shortcut Compression as Annealing）**：
   局部耗散精准标定了环境基质 $E$ 中信息阻抗过高的瓶颈。当某一路径或构件累积显著绕行热迹，且其修改提案通过三因子信用分配、MemRL 贝叶斯效用门槛 $Q(\text{path}) = \alpha/(\alpha+\beta)$ 与 `rsi-gate` 信赖域检验（$D(E_{\text{new}} \parallel E_{\text{old}}) \le \delta$）后，系统自动或半自动安装一条 $O(1)$ 规范化拓扑捷径，使后续滚动的期望搜寻代价从 $O(k)$ 探索探针坍缩为 $O(1)$ 直接查表，实现系统绕行温度 $T_d$ 的单调退火。

---

## 1. 五大前序理论谱系合流（Unification of the Five Prior Strands）

基质强化学习并非凭空杜撰的新词，而是对本仓库 2026 年 5 月至 10 月五条核心研究脉络在环境拓扑层面的自然收束与严格统一（不重新发明轮子，直接建立结构映射）：

### 1.1 Strand 1（2026-05）：信用输运与通用学习机（Credit Transport & General Learning Machine）
在 [《Credit Transport and the General Learning Machine》](2026-05-19-credit-transport-general-learning-machine.md) 与 [《Agent-Readable Credit Transport Packet》](2026-05-26-agent-readable-credit-transport-packet.md) 中，通用学习机被定义为：*未来的误差、惊讶、价值、摩擦或存续压力，沿着导致某结果的因果结构向后输运，并直接改变那些结构本身。*
- **在 Substrate RL 中的落点**：当基础模型权重 $\theta$ 冻结时，承载「向后信用输运」的物理载体不再是浮点权重矩阵，而是外部环境结构 $E$。一次会话末尾的验证回执与中途的搜索摩擦，沿着会话调用栈逆向定位到缺失的软链、未登记的脚本或含混的路由表，并在该节点处雕刻新的持久结构。

### 1.2 Strand 2（2026-10）：非反向传播三因子信用分配（Non-Backprop Three-Factor Credit Assignment）
在 [《脑启发非反向传播（Non-Backprop）AI 架构：历史复盘、理论重构与三大战略转向》](2026-10-16-non-backprop-brain-inspired-pivot-zh.md) 中，我们证明了在离散、跨模块、不可微的介观网络（$10^1 \sim 10^3$ 节点）中，标准反向传播（BP）在数学上不可微，必须转向**门控三因子法则**：
$$\Delta w \propto (\text{局部滚动资格迹}) \times (\text{协调器/谱隙门控信号}) \times (\text{确定性验证标量反馈 } R_{\text{verified}})$$
- **在 Substrate RL 中的落点**：文件系统与工具注册表正是典型的 $10^2 \sim 10^3$ 节点离散不可微图。局部资格迹对应智能体在会话中真实走过的绕行探测路径；门控信号对应顶层协调器与 `rsi-gate` 的准入裁决；标量反馈严格绑定至独立验证器（`surface-verify`、自检脚本与契约断言）输出的 $R_{\text{verified}}$。

### 1.3 Strand 3（MemRL）：从记忆效用到路径与工具的 Beta-Bernoulli 后验推广
在早期 MemRL 框架中，每条记忆条目 $m$ 维护一个基于成功/失败计数的 Beta-Bernoulli 后验均值效用 $Q(m) = \frac{\alpha}{\alpha + \beta}$，用于淘汰陈旧或误导性记忆。
- **在 Substrate RL 中的落点**：我们将 $Q$ 函数从纯文本记忆推广至**工具（Tools）、`capability-registrar` 注册表项以及文件系统路径（Filesystem Paths / Symlinks）**。每一条规范化路径 $\text{path} \in E$ 都携带自己的 $(\alpha_{\text{path}}, \beta_{\text{path}})$ 状态：当智能体调用该路径并顺利达成 $R_{\text{verified}}$ 时，$\alpha_{\text{path}} \leftarrow \alpha_{\text{path}} + 1$；当智能体因路径缺失、失效或歧义而陷入 $\ge 3$ 步探索绕行（Detour/Miss）时，$\beta_{\text{path}} \leftarrow \beta_{\text{path}} + 1$。

### 1.4 Strand 4（SkillProx / RRSI）：信赖域复杂度门控（`rsi-gate`）
在强化学习的策略优化（如 TRPO / PPO）中，过大的单步参数更新会导致策略崩溃，因此必须引入 KL 散度信赖域或裁剪步长。同理，在自演进智能体系统中，不受约束的自我修改会导致规则膨胀、死循环或偏离系统 Owner 的宪章边界。
- **在 Substrate RL 中的落点**：`rsi-gate` 充当环境侧的 **SkillProx / RRSI 信赖域门控器**。任何对基质 $E$ 的结构更新 $\Delta E$（新增软链、修改 `bin-manifest`、剪枝规则），当且仅当其诱导的行为偏移与复杂度距离满足 $D(E_{\text{new}} \parallel E_{\text{old}}) \le \delta$ 且不破坏硬性红线不变量时才予以放行；一旦超限，一律默认拒绝（Fail-Closed）。

### 1.5 Strand 5（2026-10-22）：真实会话轨迹绕行审计（Empirical Trajectory Detour Audit）
理论唯有接触真实系统的摩擦账本才有生命力。通过对本地持久化的 `505` 个智能体会话（`15,068` 步动作）进行只读轨迹解析，我们首次在生产环境中定量测出了环境侧的「热耗散率」与高频摩擦靶点，为上述四条理论谱系提供了坚实的实证闭环。

---

## 2. 数学形式化体系（Formal Mathematical Framework）

本节给出基质强化学习的五个核心形式化数学对象。

### 2.1 轨迹滚动与环境侧策略梯度目标（Rollout & Substrate Objective）

设智能体所依托的基座模型具有冻结参数 $\theta \in \Theta_{\text{frozen}}$（即 $\frac{\partial}{\partial \theta} \equiv 0$）。智能体交互的外部认知基质记为有向带权图与规则集合 $E = (\mathcal{V}_E, \mathcal{E}_E, \mathcal{R}_E) \in \mathcal{E}$，其中节点 $\mathcal{V}_E$ 表示可执行脚本、配置文件、数据构件与规则文档，有向边 $\mathcal{E}_E$ 表示目录包含关系、`~/bin/` 软链接、`@registry/bin-manifest` 索引条目及 `capability-registrar` 语义映射。

在单次会话中，给定初始任务状态 $s_0$，智能体在基质 $E$ 提供的观测与工具可见性下，生成一条长度为 $T$ 的轨迹滚动（Rollout）：
$$\tau = (s_t, a_t, r_t)_{t=0}^{T}, \quad s_{t+1} \sim \mathcal{T}(\cdot \mid s_t, a_t; E), \quad a_t \sim \pi_\theta(a_t \mid s_t, E)$$
会话结束时，独立确定性验证器（Deterministic Verifier）根据客观回执输出终端验证奖励 $R_{\text{verified}}(\tau) \in \mathbb{R}$。系统的全局优化目标是最大化关于基质 $E$ 的期望验证回报：
$$J(\pi_\theta, E) = \mathbb{E}_{\tau \sim p(\tau \mid \pi_\theta, E)}\big[R_{\text{verified}}(\tau)\big]$$

由于模型权重 $\theta$ 冻结，优化算子作用在环境基质参数 $E$ 上。应用对数导数技巧（Score-Function Identity）于环境条件化的策略与转移核，得到**基质策略梯度（Substrate Gradient）**：
$$\nabla_E J(\pi_\theta, E) \approx \mathbb{E}_{\tau} \left[ \sum_{t=0}^{T} \nabla_E \log \pi_\theta(a_t \mid s_t, E) \cdot \big(R_{\text{verified}}(\tau) - b\big) \right]$$
其中 $b = \mathbb{E}[R_{\text{verified}}]$ 为降低方差的移动平均基线（Baseline）。上式清晰表明：**即便不触碰大模型内部的任何一个浮点数权重 $\theta$，只要改变基质 $E$（例如将一个深藏在多级子目录中的高频脚本通过软链暴露在首跳可见的 `~/bin/` 或 `@registry/bin-manifest` 中），就能直接改变条件策略分布 $\pi_\theta(a_t \mid s_t, E)$，使智能体以接近 1 的概率在第一步直接选中目标工具。**

---

### 2.2 非反向传播三因子基质更新法则（Three-Factor Substrate Update Rule）

由于文件系统路径与注册表路由是离散图结构，上述连续梯度在工程执行中映射为非反向传播**三因子局部基质更新算子**。对于基质中的任意候选路径或拓扑捷径 $\text{path} \in E$，其结构权重更新量 $\Delta E_{\text{path}}$ 满足：
$$\Delta E_{\text{path}} \propto \underbrace{e_{\text{path}}(\tau)}_{\text{Factor 1: 局部资格迹}} \cdot \underbrace{g_{\text{coord}} \in \{0, 1\}}_{\text{Factor 2: rsi-gate 准入门}} \cdot \underbrace{\big(R_{\text{verified}}(\tau) - b\big)}_{\text{Factor 3: 验证标量反馈}}$$

三个因子的物理定义如下：
1. **局部绕行资格迹 $e_{\text{path}}(\tau)$**：
   $$e_{\text{path}}(\tau) = \sum_{t=0}^{T} \gamma^{T-t} \, \mathbb{I}\big[a_t \in \mathcal{A}_{\text{explore}}(\text{path})\big]$$
   其中 $\gamma \in (0,1]$ 为时间衰减因子，$\mathcal{A}_{\text{explore}}(\text{path})$ 为当前滚动中针对目标构件执行的探索动作集合（如 `find`、`ls`、`grep`、`read`）。只有在实际会话中被反复探针触及的真实路径，才会积累非零资格迹 $e_{\text{path}}(\tau) > 0$。
2. **协调器与信赖域门控 $g_{\text{coord}} \in \{0, 1\}$**：
   由顶层控制器（Coordinator）与 `rsi-gate` 联合给出的二值准入信号。当系统处于混沌态、缺乏验证凭证或修改超出信赖域时，$g_{\text{coord}} = 0$，强制阻断基质写入。
3. **验证标量反馈 $(R_{\text{verified}}(\tau) - b)$**：
   由独立验证器给出的带符号优劣幅度。严禁使用智能体自身的口头总结（`Language != State`）替代验证器回执。

---

### 2.3 路径与注册表项的 Beta 后验效用（Extended MemRL Beta Utility on Paths）

为了在多次会话之间持久追踪每一条文件系统路径、规范化软链与 `capability-registrar` 路由的真实效用，我们将 MemRL 的 Beta-Bernoulli 共轭模型扩展到基质图的所有寻址边 $\text{path} \in E$。每条路径维护先验计数 $(\alpha_{\text{path}}, \beta_{\text{path}})$（初始弱先验设为 $\alpha_0 = 1, \beta_0 = 1$），其后验期望效用为：
$$Q(\text{path}) = \mathbb{E}\big[\mathrm{Beta}(\alpha_{\text{path}}, \beta_{\text{path}})\big] = \frac{\alpha_{\text{path}}}{\alpha_{\text{path}} + \beta_{\text{path}}}$$

在每次轨迹滚动 $\tau$ 结算时，状态转移规则为：
$$\begin{cases}
\alpha_{\text{path}} \leftarrow \alpha_{\text{path}} + 1, & \text{若 } \text{path} \text{ 被直接命中调用且会话取得 } R_{\text{verified}}(\tau) = 1 \text{（Verified-Useful）} \\
\beta_{\text{path}} \leftarrow \beta_{\text{path}} + 1, & \text{若围绕该构件发生 } \ge 3 \text{ 步连续探索绕行或路径查找失败（Detour / Miss）}
\end{cases}$$

当候选构件的绕行摩擦频次突破热点阈值，且为之构建的规范化捷径在验证回放中使后验效用满足准入门槛：
$$Q(\text{path}) \ge \tau_Q \quad (\text{典型工程阈值 } \tau_Q = 0.65)$$
同时通过下方信赖域门控检验时，该捷径被正式固化为常驻基质的一部分；反之，若某条既有软链长期失效导致 $Q(\text{path}) < \tau_{\text{prune}}$，则在睡眠巩固周期中被自动剪枝。

---

### 2.4 信赖域复杂度门控（SkillProx / RRSI Trust-Region Gate）

无约束地向 `~/bin/`、注册表或常驻规则文件追加内容，会导致「基质熵增（Substrate Entropy Bloat）」——即规则越来越多，智能体反而需要花费更多 Token 去阅读规则本身。为此，`rsi-gate` 引入与 PPO / TRPO 同构的**单步信赖域约束（Trust-Region Constraint）**：
$$\text{Admit}(E_{\text{new}} \leftarrow E_{\text{old}} + \Delta E) \iff D(E_{\text{new}} \parallel E_{\text{old}}) \le \delta \;\land\; \mathcal{C}_{\text{brightline}}(E_{\text{new}}) = 1$$
其中：
- $D(E_{\text{new}} \parallel E_{\text{old}}) = D_{\mathrm{KL}}\big(\pi_\theta(\cdot \mid E_{\text{new}}) \parallel \pi_\theta(\cdot \mid E_{\text{old}})\big) + \lambda_{\mathrm{MDL}} \cdot \max\big(0, |E_{\text{new}}| - |E_{\text{old}}|\big)$ 综合度量了新旧基质诱导的策略分布偏移与最小描述长度（MDL）复杂度增量；
- $\delta > 0$ 为信赖域半径上限；
- $\mathcal{C}_{\text{brightline}}(E_{\text{new}}) \in \{0, 1\}$ 为硬性红线校验（零私人信息泄露、零未授权外部写操作、回归自检通过）。
- **Fail-Closed 铁律**：凡是 $D(E_{\text{new}} \parallel E_{\text{old}}) > \delta$ 的激进大改或整文件重写，门控器一律自动驳回（Reject），迫使演化保持小步、可审计、可逆的单调推进。

---

### 2.5 局部热耗散与拓扑捷径退火（Dissipation $\to$ Topological Shortcut Compression）

在非平衡态统计物理中，系统克服环境阻力所做的无用功以焦耳热的形式耗散。在智能体的轨迹滚动中，什么是「热」？

当智能体需要调用一个既存脚本（例如 `relay.py` 或 `selftest.sh`），但由于外部基质 $E$ 缺乏显式索引，不得不连续执行：
$$\texttt{find . -name "*relay*"} \;\to\; \texttt{ls -la} \;\to\; \texttt{grep "main"} \;\to\; \texttt{read file}$$
这连续 $\ge 3$ 步的探索性探针并未直接推进业务状态转变，而是纯粹为了克服环境拓扑的信息不透明性而付出的**局部热力学耗散（Local Thermodynamic Dissipation）**。

我们将单个绕行片段定义为同一会话内长度 $k \ge 3$ 的极大连续探索动作子序列 $d = (a_{t_1}, \dots, a_{t_k}) \subset \tau$。据此定义整个智能体舰队在基质 $E$ 下的**轨迹绕行温度（Detour Temperature）** $T_d(E)$：
$$T_d(E) = \frac{N_{\text{actions\_in\_detours}}(E)}{N_{\text{total\_actions}}(E)} = \frac{\sum_{\tau} \sum_{d \in \mathcal{D}(\tau)} |d|}{\sum_{\tau} |\tau|}$$

**拓扑捷径压缩定理（Topological Shortcut Compression）**：
设构件 $v^* \in \mathcal{V}_E$ 在审计周期内被绕行片段命中 $M(v^*)$ 次，每次平均探索步长为 $\bar{k}(v^*) = \mathbb{E}[|\text{detour}(v^*)|] > 3$。若在基质中安装一条从起始工作空间直接指向 $v^*$ 的规范化 $O(1)$ 边 $e^* = (s_0 \to v^*)$（例如在 `~/bin/` 建立软链、写入 `@registry/bin-manifest` 或注册 `capability-registrar` 路由），则对于后续访问 $v^*$ 的轨迹，其定位路径复杂度发生相变坍缩：
$$\text{PathCost}(v^* \mid E_{\text{old}}) = O\big(\bar{k}(v^*)\big) \quad \xrightarrow{\; E_{\text{new}} = E_{\text{old}} \cup \{e^*\} \;} \quad \text{PathCost}(v^* \mid E_{\text{new}}) = O(1)$$
同时，系统的全局绕行温度获得确定性退火降幅：
$$\Delta T_d = T_d(E_{\text{new}}) - T_d(E_{\text{old}}) \approx -\frac{M(v^*) \cdot \big(\bar{k}(v^*) - 1\big)}{N_{\text{total\_actions}}} < 0$$
因此，**绕行热耗散不仅不是无意义的日志垃圾，反而是指引外部认知基质在何处修路架桥的最精确梯度信号。**

---

## 3. 真实会话轨迹审计（Empirical Trajectory Detour Audit）

> **只读追加账本截面声明（Live Append-Only Ledger Caveat）**：  
> 以下实证数据系于 **`2026-10-22T11:07Z`** 对生产环境中的智能体会话日志执行只读解析所得的真实快照。由于底层会话账本为实时追加写入（Live Append-Only Ledger），随着会话持续产生新日志，任何后续时刻重跑审计脚本都会观测到个位数的自然漂移。本文严格固定 `2026-10-22T11:07Z` 冻结截面，绝不捏造或修饰任何数字。

### 3.1 全局与分席位轨迹指标（Global & Per-Source Metrics）

本次审计完整解析了 **`505` 个真实会话**（涵盖交互式前台 `antigravity` 席位 `257` 个会话，以及顶层控制器 `kiro` 席位 `248` 个会话），核心统计量汇总如下：

| 审计指标维度 | 全局汇总 (Total Fleet) | `antigravity` 席位 | `kiro` 席位 | 物理与架构解释 |
|---|---|---|---|---|
| **解析会话数 (Sessions Parsed)** | **505** | 257 (50.89%) | 248 (49.11%) | 双核心席位样本量高度均衡 |
| **总动作数 (Total Actions)** | **15,068** | 12,150 | 2,916 | 含 2 条账本元数据头记录 |
| **探索性动作数 (Exploratory Actions)** | **3,004 (19.94%)** | 1,934 (15.92%) | 1,069 (36.66%) | 每 5 步动作即有 1 步用于读取/搜索/探路 |
| **绕行片段数 (Detour Episodes, $\ge 3$ 步)** | **287** | — | — | 连续 $\ge 3$ 步纯探索动作构成的局部摩擦簇 |
| **绕行内部动作数 (Actions in Detours)** | **1,340** | 840 | 500 | 落在连续绕行片段内的浪费步数 |
| **绕行温度 $T_d$ (Detour Rate)** | **8.89%** | **6.91%** | **17.15%** | `kiro` 作为顶层拆解与验收控制器，承担了更高比例的跨目录发现任务 |
| **平均绕行步长 $\mathbb{E}[|\text{detour}|]$** | **4.67 步** | — | — | 一旦陷入盲搜，平均需连续试探近 5 步才能定位目标 |

**关键实证发现**：
1. **近五分之一的算力消耗在环境探路上**：在 `15,068` 次工具调用中，高达 `3,004` 次（`19.94%`）属于探索性动作；而其中 `1,340` 次（占全部动作的 `8.89%`，占探索动作的 `44.61%`）集中在连续 $\ge 3$ 步的绕行片段内。
2. **角色分工导致的耗散梯度差**：`kiro` 席位的探索率（`36.66%`）与绕行温度（`17.15%`）均显著高于 `antigravity` 席位（`15.92%` 与 `6.91%`）。这是因为顶层控制器在拆解多步任务与执行独立验收时，经常需要在未知子目录中寻找校验脚本与状态账本——这也证明**为顶层控制器建立 `@registry/bin-manifest` 与 `capability-registrar` $O(1)$ 索引具有最高的边际收益**。

---

### 3.2 探索性动作的 15 类工具分布（Exploratory Action Breakdown）

对全部 `3,004` 步探索性动作按具体工具与命令模式进行细粒度归类（15 类明细总和 `3,003` 步，外加 1 步复合探针）：

| 排名 | 探索动作类型 (Action Type) | 真实频次 (Count) | 占探索动作比例 | 典型触发场景与耗散特征 |
|---|---|---|---|---|
| 1 | `read` | **1,386** | 46.14% | 读取候选文件确认接口、路径或配置内容 |
| 2 | `"\| grep"` | **799** | 26.60% | 在 Shell 管道中通过关键词过滤命令或目录输出 |
| 3 | `search` | **299** | 9.95% | 调用代码库全文或符号检索工具定位定义 |
| 4 | `"-name"` | **255** | 8.49% | 调用 `find ... -name` 按文件名通配符在目录树中盲搜 |
| 5 | `ls` | **73** | 2.43% | 逐层列举目录内容以摸索文件结构 |
| 6 | `grep(tool)` | **68** | 2.26% | 调用结构化 grep 工具检索正则模式 |
| 7 | `cat` | **51** | 1.70% | 在命令行直接打印文件全文查看配置 |
| 8 | `grep(cmd)` | **26** | 0.87% | 裸调命令行 `grep` 扫描文本 |
| 9 | `glob` | **20** | 0.67% | 路径通配符枚举匹配 |
| 10 | `which` | **8** | 0.27% | 探测二进制或脚本是否在 `PATH` 中 |
| 11 | `find` | **8** | 0.27% | 广义目录树遍历查找 |
| 12 | `head` | **4** | 0.13% | 读取文件头部数行探查格式 |
| 13 | `stat` | **3** | 0.10% | 检查文件存在性、权限或修改时间戳 |
| 14 | `tail` | **2** | 0.07% | 查看日志或账本尾部记录 |
| 15 | `fd` | **1** | 0.03% | 快速文件名检索工具调用 |

可以清晰看到：前四项（`read` 1,386、`"| grep"` 799、`search` 299、`"-name"` 255）合计达 **`2,739` 次（占 `91.18%`）**。其中 `"-name"`（255 次）与 `"| grep"`（799 次）的大量出现，直接暴露出智能体「知道构件叫什么名字或含什么关键词，但不知道它放在哪个规范路径下」的拓扑缺失。

---

### 3.3 Top 8 高频摩擦热点构件（Top Friction Hotspots & Shortcut Prescription）

审计进一步聚合了被探索探针与绕行片段反复命中的具体构件基名（Basenames）。排名前 8 的热点构件及其真实摩擦指标如下：

| 热点排名 | 构件基名 (Basename) | 总探索频次 (Frequency) | 绕行片段命中 (Detour Hits) | 独立会话数 (Distinct Sessions) | 拓扑耗散诊断与 $O(1)$ 压缩处方 |
|---|---|---|---|---|---|
| **#1** | `relay.py` | **118** | **24** | **13** | 跨 13 个会话被搜寻 118 次、引发 24 次连续绕行。处方：写入 `@registry/bin-manifest` 并建立规范化软链。 |
| **#2** | `selftest.sh` | **77** | **20** | **9** | 自检脚本散落在不同子项目中，导致验收阶段频繁 `find -name selftest.sh`。处方：在 `capability-registrar` 中按模块注册标准自检入口。 |
| **#3** | `codex-memory` | **69** | **11** | **35** | **波及面最广（横跨 35 个独立会话）**的核心记忆桥接工具。处方：固化 `~/bin/codex-memory` 规范路径并写入会话起手常驻规则。 |
| **#4** | `backfill-20261020` | **47** | **21** | **7** | 绕行命中率极高（21/47），智能体反复翻找特定日期回填批次。处方：纳入 `@registry/ledger-index` 归档清单。 |
| **#5** | `relay` | **46** | **12** | **11** | 与 `relay.py` 形成同名无后缀歧义，诱发额外消歧探测。处方：待固化一条规范化入口（例如 `~/bin/relay` 符号链接，当前尚未安装），把两个同名目标合并为单一 O(1) 查找。 |
| **#6** | `apply.sh` | **43** | **10** | **13** | 跨 13 个会话的部署/应用脚本探针。处方：在 `capability-registrar` 中建立显式语义路由。 |
| **#7** | `intake_broker.py` | **37** | **8** | **11** | 队列分派核心组件，跨 11 个会话被反复定位。处方：登记入 `@registry/bin-manifest` 常驻查表。 |
| **#8** | `SHA256SUMS` | **37** | **14** | **7** | 校验和清单文件，在 7 个会话中引发 14 次绕行。处方：在 `surface-verify` 流水线中绑定固定相对路径约定。 |

仅这 Top 8 热点构件就累计消耗了 **`474` 次探索动作**与 **`120` 次绕行片段命中**。按照平均绕行步长 `4.67` 步计算，只要将这 8 个构件通过软链与注册表压缩为 $O(1)$ 直达，即可在同等工作负载下直接消除超过 `350` 步无效探测动作，使相关任务的局部绕行温度下降超过三分之一。

---

## 4. 配套三大交互式验证模拟器说明（Companion Interactive Simulators）

在配套的旗舰交互网页 [`trajectory-rl-substrate-evolution.html`](../trajectory-rl-substrate-evolution.html) 中，我们将上述数学方程与冻结审计数据实例化为三个纯 Canvas / SVG 实时计算的交互沙盒：

1. **模拟器 S1 · 轨迹滚动绕行热耗散与退火可视化器（Trajectory Rollout Detour Heat Dissipation Visualizer）**：
   在二维网络拓扑上动态渲染智能体从 `s₀` 出发寻找目标构件的过程。未安装捷径时，智能体在 `find -name`、`"| grep"`、`ls`、`read` 节点间随机游走并点亮红色热耗散光晕；点击「热力学退火（安装捷径）」后，系统在高频通道上架设蓝色 $O(1)$ 直达弧，直观呈现期望绕行步长从 `4.67` 步向 `1.00` 步收敛、绕行温度 $T_d$ 从 `8.89%` 逐步退火的物理过程。
2. **模拟器 S2 · 散乱基质 vs 规范化压缩基质对比器（Before/After Graph Shortcut Compressor）**：
   左右双联 SVG 拓扑图，严格绑定 Top 8 真实热点频次权重（`relay.py` 118、`selftest.sh` 77、`codex-memory` 69 等）。支持按构件单独检视或拖动全局压缩率滑块（0/8 至 8/8），实时计算路径复杂度 $O(k) \to O(1)$ 跃迁与累计节省步数。
3. **模拟器 S3 · 三因子信用分配与信赖域门控检验器（3-Factor Credit Assignment & Trust-Region Inspector）**：
   提供局部资格迹 $e_{\text{path}}$、协调器门控 $g_{\text{coord}} \in \{0,1\}$、验证标量反馈 $(R_{\text{verified}} - b)$ 与信赖域半径 $\delta$ 四组滑块，以及「验证有效调用（$\alpha+1$）」与「绕行未命中（$\beta+1$）」交互按钮。基于连续伽马函数数值近似实时绘制连续 $\mathrm{Beta}(\alpha, \beta)$ 概率密度曲线与 `rsi-gate` 径向信赖域表盘，严格演示何时准予刻入基质（GREEN `SHORTCUT ADMITTED`）、何时触发 Fail-Closed 拦截（RED `REJECTED`）。

---

## 5. 可证伪性与四大反信号（Falsifiability & Anti-Signals）

根据科学哲学中的可证伪性原则（Falsifiability Principle）以及本仓库 `THEORY.md` 的一贯纪律，如果一项架构宣称「实现了环境侧强化学习」，但无法通过客观指标检验，那它就只是修辞装饰。我们为 Substrate RL 设定以下四条硬性**判伪反信号（Anti-Signals）**：

1. **反信号 I：基质体积膨胀但期望绕行步长 $\mathbb{E}[|\text{detour}|]$ 不降（Bloat Without Annealing）**
   若向 `~/bin/`、`@registry/bin-manifest` 与常驻宪章写入新捷径后，在后续同等规模（$N \approx 500$ 会话）的只读轨迹审计中，全局绕行温度 $T_d$ 未显著低于 `8.89%`，或者目标热点（如 `relay.py`、`codex-memory`）的平均绕行步长依然停留在 `4.67` 步附近，则说明新增的基质结构未被条件策略 $\pi_\theta(a_t \mid s_t, E)$ 有效读取，该类写入判为无效噪声并立即回滚。
2. **反信号 II：路径 Beta 效用 $Q(\text{path})$ 与真实 $R_{\text{verified}}$ 脱钩（Reward-Metric Miscalibration）**
   若高 $Q(\text{path}) = \alpha / (\alpha + \beta)$ 评级的路径在实际任务中并未对应更低的失败率或更短的定位步数，说明 $\alpha$ 的累加混入了未经独立验证器核验的虚假成功信号，必须立即切断自报更新通道，重绑确定性回执。
3. **反信号 III：信赖域半径 $\delta$ 失调导致「零学习僵死」或「规则漂移」（Trust-Region Collapse）**
   若 `rsi-gate` 的复杂度阈值 $\delta$ 过严导致所有经过实证的高频热点捷径均被拦截（学习率归零），或 $\delta$ 过宽导致常驻规则在多次自动代谢后发生前后矛盾与行为漂移，则判定复杂度度量函数 $D(E_{\text{new}} \parallel E_{\text{old}})$ 失效。
4. **反信号 IV：捷径自身沦为新的命名污染源（Shortcut Proliferation Loops）**
   若为消除绕行而创建的软链或别名数量过多，导致智能体在 `~/bin/` 下需要花费额外的 `ls / grep / read` 步数去区分近义软链（如同名异构的 `relay` 与 `relay.py`），使得净探索步数反升（$\Delta T_d > 0$），则触发睡眠期强制合并且冻结同类新软链准入。

---

## 6. 结论（Conclusion）

当基础大模型的参数 $\theta$ 被冻结在云端或只读权重文件中时，智能体的持续演化并未终结——它只是从不可见的微观浮点矩阵，转移到了完全可审计、可版本化、可回滚的**外部认知基质 $E$** 之中。

通过将每一次会话视为轨迹滚动 $\tau$，将连续盲搜识别为局部热力学耗散 $T_d$，并用非反向传播三因子法则、扩展版 MemRL 路径效用 $Q(\text{path})$ 以及 `rsi-gate` 信赖域门控来驱动 $O(k) \to O(1)$ 的拓扑捷径压缩，我们不仅在理论上闭合了 2026 年 5 月至 10 月的五条演化主线，更在 `505` 个真实会话、`15,068` 步动作的实证账本上给出了精确到具体文件名的工程退火路线图。
