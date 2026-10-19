# Tabelog·Eye + VRO: Decentralized Autonomous Taste De-Biasing & Physical Fulfillment Mesh

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Verification: verify_tier1.py PASS](https://img.shields.io/badge/verify_tier1.py-PASS-emerald.svg)](https://github.com/MachengShen/system-evolution-public)
[![Tokens: Zero Speculative Tokens](https://img.shields.io/badge/Governance-Zero%20Tokens%20%7C%20Soulbound%20Track--Record-gold.svg)](https://theory.clawishmacheng.com/system-evolution-public/sgdao-fulfillment-proposal-en.html)
[![Anti-Fabrication: Enforced](https://img.shields.io/badge/Anti--Fabrication-Strict%20Authentic%20Assets-success.svg)](https://github.com/MachengShen/system-evolution-public)

> **English First | 中文在后**  
> Companion Proposal: [SGDO / VRO Mechanism Design Proposal (English)](https://theory.clawishmacheng.com/system-evolution-public/sgdao-fulfillment-proposal-en.html) · [提案中文版](https://theory.clawishmacheng.com/system-evolution-public/sgdao-fulfillment-proposal-zh.html) · [Live PWA Prototype](https://future.clawishmacheng.com/preview/tabelog-eye/)

---

## English Edition

### 1. Vision & Architecture

When someone encounters something they truly crave—a covert 8-seat Tokyo sushi counter accepting only local landline reservations, or an unlisted artisan ceramic teapot in Kyoto sold strictly offline in cash—why do pure LLM agents fail upon hitting the physical world, while traditional buying agents (*daigou*) and freelance boards degenerate into Akerlof lemon markets plagued by illustrative 30%–50% hidden markups and unverified claims?

**Tabelog·Eye + VRO** addresses this structural trilemma (*Long-Tail Physical Reach* vs. *Zero Principal-Agent Moral Hazard* vs. *Zero Frontend Cognitive Load*) via a clean, two-sided architecture:

1. **Frontend (Zero Cognitive Load)**: A pure, image-first swipe interface capturing irreducible personal aesthetic appetite $v_{\text{eye}}$ alongside an all-inclusive maximum ceiling budget $B_{\max}$. No review fatigue, no score manipulation.
2. **Backend 4-Cell Autonomous Mesh (SGDO)**:
   - `C-Res` (Resource Sourcing): Resolves candidates, identifies physical bottlenecks ($\kappa_{\text{API}} = \infty$).
   - `C-Pred` (Calibration & Pricing): Executes the **5-Factor Logit-Shapley De-Biasing Engine** to recover counterfactual culinary craft $\widehat{S}_i^\star$, setting fair-value caps $P_{\text{fair}}$ and aborting scalper channels.
   - `C-Eng` (Engineering & Decomposition): Operates the hybrid decomposition operator $\mathcal{D}(I)$ with an illustrative target split (~95% / ~5%), absorbing ~95% of digital friction via $\$0$-marginal-cost compute and dispatching only the irreducible ~5% physical last mile as $\$5\text{–}\$25$ standardized micro-bounties to trusted local human nodes.
   - `C-Gate` (Verification Gate): Enforces three orthogonal verification paths ($\rho_{ab} < 0.2$) before triggering non-token staged escrow settlement.
3. **Double-Circuit Capital Metabolism**:
   - *Circuit 1 (Exploration & Calibration)*: Bootstrapped by a strict $\$100/\text{mo}$ seed pool buying only high-EIG human ground-truth calibration signals.
   - *Circuit 2 (Order Fulfillment)*: Per-order self-funded escrow funded by buyer's $B_{\max}$. No-fulfillment = zero fees ($\phi = 0$); successful verified fulfillments contribute a 3%–8% reality royalty back into the open public ledger.

```
+-------------------------------------------------------------------------+
|                  FRONTEND: TABELOG·EYE PWA                              |
|   Irreducible Taste Signal v_eye  +  All-Inclusive Ceiling Budget B_max |
+-------------------------------------------------------------------------+
                                    |
                                    v
+-------------------------------------------------------------------------+
|                  SGDO 4-CELL AUTONOMOUS MESH                            |
|                                                                         |
|  [C-Res] Source Resolution  -->  [C-Pred] 5-Factor Logit-Shapley        |
|  Identify API bottlenecks        De-biasing & Scalper Guard P_fair      |
|                                                                         |
|  [C-Eng] Hybrid Operator D(I) --> [C-Gate] 3-Path Orthogonal Gate       |
|  ~95% machine digital friction   Path A: Independent Store Receipt      |
|  ~5% physical micro-bounty       Path B: Nonce Macro Live Probe         |
|  (illustrative target split)     Path C: Carrier Weigh-in / Handshake   |
+-------------------------------------------------------------------------+
               |                                      |
               v                                      v
   [Local Human Micro-Bounty]               [Non-Token Staged Escrow]
   $5–$25 for call / line / probe           Atomic Release + Reality Royalty
```

---

### 2. The 5-Factor Logit-Shapley De-Biasing Formula

Public review scores $S_{i,\text{pub}} \in [3.00, 5.00]$ on rating platforms are severely contaminated by sampling skew, service halo penalties, hype loops, and platform shrinkage. We map scores into unbounded logit log-odds $\eta_i = \log\frac{S_i - 2.80}{5.00 - S_i}$ and compute Shapley values across 5 orthogonal structural factors to isolate the true culinary craft score $\widehat{S}_i^\star$:

$$\widehat{S}_i^{\star} = S_{i,\text{pub}} + \Delta_i^{\text{sample}} + \Delta_i^{\text{ortho}} + \Delta_i^{\text{surprise}} + \Delta_i^{\text{vision}} - \Delta_i^{\text{hype}}$$

1. **$\Delta_i^{\text{sample}}$ (Connoisseur $z$-Score Normalization)**: Standardizes ratings by reviewer historical mean $\mu_u$ and standard deviation $\sigma_u$, separating lunch sets from dinner counter omakase.
2. **$\Delta_i^{\text{ortho}}$ (Orthogonal Flavor-Service Decoupling)**: Double-ML decoupling for blunt artisan chefs (*頑固大将*), strict house etiquette (*私語厳禁*), and cramped Showa interiors (only triggered when $r^{\text{food}} - r^{\text{service}} \ge 0.4$ to avoid subsidizing poor dining).
3. **$\Delta_i^{\text{surprise}}$ (Semantic Text Residual)**: Extracts conditional surprise from authentic reviews (rewarding *「穴場 / 3.3台なのが不思議」* and penalizing *「写真映えだけ / 期待外れ」*).
4. **$\Delta_i^{\text{vision}}$ (Multimodal Physical Craft Metric)**: Strictly measures objective physical indicators (knife-cut angular sharpness, Binchotan Maillard sear uniformity, shari rice integrity) while rejecting gold leaf / dry-ice gimmicks.
5. **$-\Delta_i^{\text{hype}}$ (Social Hype & Loop Filtering)**: Detects reviewer clique graph radius and 5.0-star uninformative praise bubbles, enforcing strict moderation on mass chain izakayas ($\le \pm 0.08$ quantile calibration only).

**Fair-Value & Scalper Guard**:

$$P_{\text{fair}} = g(\widehat{S}_j^{\star}, c, \text{loc}, \text{season}), \qquad \text{flag}_{\text{scalper}} = \mathbb{1}\!\Big[P_{\text{quote}} > P_{\text{fair}}(1+\epsilon) \;\lor\; \text{channel} \notin \text{FirstParty}\Big]$$

Channels triggering $\text{flag}_{\text{scalper}} = 1$ are immediately pruned from dispatch.

---

### 3. Package Layout

```text
tabelog-eye-vro/
├── README.md                  # This comprehensive bilingual documentation
├── CONTRIBUTING.md            # Fork, development & PR submission guidelines
├── CONTRIBUTORS.md            # Verified open-source contributors & attestation log
├── tools/
│   └── verify_tier1.py        # Self-contained Tier-1 AST & asset integrity verifier
├── app/                       # Tabelog·Eye PWA Client
│   ├── index.html             # Pixel 10 Pro Dark-Gold Shell & Swipe Interface
│   ├── dataset.json           # 31 authentic venues with 5-factor calibrated vectors
│   ├── manifest.json          # PWA web manifest
│   ├── sw.js                  # Offline Service Worker (CacheStorage v3)
│   ├── photos/                # 31 authentic food & counter photos (Zero Stock Photos!)
│   ├── curation_feedback_ledger.jsonl  # Append-only taste asset vault export
│   └── kiro-debiasing-methodology.md   # Mathematical specification of de-biasing
└── self-host/                 # Standalone Zero-Dependency Self-Host Node
    ├── Dockerfile             # Hardened non-root Python 3.11-slim container
    ├── docker-compose.yml     # 1-command deployment with volume persistence
    ├── server.py              # Zero-dependency HTTP + SQLite WAL taste server
    └── README-SELF-HOST.md    # Dedicated REST API & deployment manual
```

---

### 4. 1-Command Self-Hosting

The `self-host/` package runs with **zero external pip dependencies** (only Python standard libraries `http.server`, `sqlite3`, `hashlib`, etc.).

#### Option A: Docker Compose (Recommended)

```bash
# 1. Clone repo and enter self-host directory
git clone https://github.com/MachengShen/system-evolution-public.git
cd system-evolution-public/tabelog-eye-vro/self-host

# 2. Launch background node
docker compose up -d

# 3. Check node health
curl -s http://127.0.0.1:8080/health | jq
```

#### Option B: Standalone Python 3

```bash
cd system-evolution-public/tabelog-eye-vro/self-host
python3 server.py
```

Open **`http://localhost:8080/`** to access your private taste vault. Each visiting browser receives an isolated random `localStorage` sandbox token (`tabelog_eye_sandbox_id`, zero hardware fingerprinting) with independent virtual sandbox balances and zero risk of cross-polluting other profiles.

---

### 5. How to Fork & Submit Pull Requests (Upstream Merge)

We encourage open-source contributions from mechanism designers, culinary researchers, and distributed systems engineers.

#### Workflow

```
[Fork Repository]
       │
       ▼
[Create Feature Branch] (git checkout -b feat/my-improvement)
       │
       ▼
[Local Development & Testing]
  - Add restaurant calibrations / Enhance de-biasing formulas
  - Verify Authentic Physical Assets (ZERO stock photos!)
       │
       ▼
[Run Verification Harness: python3 tabelog-eye-vro/tools/verify_tier1.py]
       │
       ▼
[Submit Pull Request] (Using .github/PULL_REQUEST_TEMPLATE.md)
       │
       ▼
[Automated C-Gate Cross-Model Evaluation & Upstream Merge]
       │
       ▼
[Recorded in CONTRIBUTORS.md & Proposed Soulbound Weight W_i(t) Roadmap]
```

1. **Fork the Repo**: Fork `https://github.com/MachengShen/system-evolution-public` to your personal GitHub account.
2. **Implement Feature**:
   - Enhancing de-biasing algorithms or adding regional venue adapters.
   - **Strict Anti-Fabrication Rule**: Never use stock photography (`unsplash.com`, `pexels.com`, `pixabay.com`, etc.). If authentic photography is blocked by anti-scraping (403), mark the venue as `QUARANTINED_MISSING_AUTHENTIC_ASSET` rather than faking images.
3. **Verify Locally**:
   Run the self-contained Tier-1 static and asset integrity check:
   ```bash
   python3 tabelog-eye-vro/tools/verify_tier1.py
   ```
4. **Submit PR**: Open a PR with our template (`.github/PULL_REQUEST_TEMPLATE.md`).
5. **Upstream Review & Contributor Attestation**: Verified PRs are merged, recorded in `CONTRIBUTORS.md`, and mapped to the proposed Soulbound Track-Record weight $W_i(t)$ in the decentralized fulfillment roadmap.

---

## 中文版 (Chinese Edition)

### 1. 架构愿景与问题定义

当一个人看到真正心动却「难买、难订、仅限本地座机或现金线下、跨语言跨制度」的长尾非标之物时：
- **纯大模型 Agent** 困死于没有 API 的物理制度墙；
- **传统代购与众包市场** 则在委托—代理信息不对称下，迅速坍缩为典型 30%–50% 示意暗箱加价与假货横行的阿克洛夫柠檬市场。

**Tabelog·Eye + VRO** 通过人机混合解耦打破这一三角困境：
- **前端极简眼缘层**：仅捕获不可压缩的私有审美信号 $v_{\text{eye}}$ 与最高全包预算 $B_{\max}$，绝不让用户承担比价、筛查与盯梢的认知负荷。
- **后端 SGDO 4-Cell 自治网格**：以目标拆分比例（Illustrative Target Split $\sim 95\% / \sim 5\%$），机器以 $\$0$ 边际成本吞吐约 $95\%$ 的数字摩擦；仅当遇到接口断层（$\kappa_{\text{API}}=\infty$）或物理感官期望信息增益超阈值（$\text{EIG}_{\text{phys}}>\tau_{\text{gate}}$）时，才向本地可信人类节点派发 $\$5\text{–}\$25$ 标准化微赏金。
- **三路径正交履约核验 ($R_{\text{verified}}$)**：制度独立回执 (Path A) ∧ 活体挑战码微距探针 (Path B) ∧ 下游物流称重握手 (Path C)，在完全条件独立（$\rho_{ab}=0$）下联合伪造漏网率压低至 $\prod_k f_k \approx 10^{-3}$ 量级（单次检测率 $>99.9\%$），在 $\rho_{ab} \le 0.2$ 保守相关界下仍保持 $\Pr[\text{FA}] \le 0.0353$（单次检测率 $\ge 96.5\%$）。
- **永久零投机代币**：权力完全基于不可转让、不可买卖的灵魂绑定声誉 $W_i(t)$。

---

### 2. 破偏置真味校准法 v1.0（五因子 Logit-Shapley）

公开星级 $S_{i,\text{pub}} \in [3.00, 5.00]$ 并非手艺真值，而是混杂了采样生态位、社会礼仪规训、环境光环与网红泡沫的粗糙观测。系统将有界分数映射至无界优势空间 $\eta_i = \log\frac{S_i - 2.80}{5.00 - S_i}$，剥离五大系统性偏置：

$$\widehat{S}_i^{\star} = S_{i,\text{pub}} + \underbrace{\Delta_i^{\text{sample}}}_{\substack{\text{👥 辛口评委 } z\text{-score}\\\text{与昼夜采样修正}}} + \underbrace{\Delta_i^{\text{ortho}}}_{\substack{\text{😤 剥离臭脸大将/规矩严}\\\text{与昭和窄店光环惩罚}}} + \underbrace{\Delta_i^{\text{surprise}}}_{\substack{\text{🤯 评论超预期语义残差}\\(\text{期待外れ vs. 穴場})}} + \underbrace{\Delta_i^{\text{vision}}}_{\substack{\text{🔪 多模态手艺硬指标}\\(\text{刀工/美拉德/米粒})}} - \underbrace{\Delta_i^{\text{hype}}}_{\substack{\text{🛡️ 熟客互捧/映え罠}\\\text{泡沫逆向折价}}}$$

- **公允价格与黄牛熔断**：凡报价 $P_{\text{quote}} > P_{\text{fair}}(1+\epsilon)$ 或非一手渠道的派单，在 `C-Pred` 阶段直接一票否决。

---

### 3. 一键私有化自建部署 (Self-Host)

套件提供完全独立、零外部依赖的私有化节点服务。所有赏味偏好沉淀于本机 SQLite WAL 数据库，绝不上报外部公有大模型。

```bash
# Docker Compose 一键启动
git clone https://github.com/MachengShen/system-evolution-public.git
cd system-evolution-public/tabelog-eye-vro/self-host
docker compose up -d

# 或使用原生 Python 3 标准库（无需 pip）
python3 server.py
```

访问 `http://localhost:8080/` 即可进入本地专属的味觉资产管理仪表盘。

---

### 4. 开源参与与 Pull Request 上游回流机制

我们诚挚欢迎全球机制设计者、老饕食客与开发者提交贡献！

#### 贡献流转规范
1. **Fork 仓库**：Fork `https://github.com/MachengShen/system-evolution-public`。
2. **功能开发与防伪铁律**：
   - 严禁使用 Unsplash、Pexels 等图库假图掩盖 403 缺失数据。
   - 缺失真实资产时，必须显式标注为 `QUARANTINED_MISSING_AUTHENTIC_ASSET`。
3. **本地测试与静态门禁**：
   运行仓库自带的静态与无假图核验脚本：
   ```bash
   python3 tabelog-eye-vro/tools/verify_tier1.py
   ```
4. **提交 Pull Request**：基于 `.github/PULL_REQUEST_TEMPLATE.md` 详述变更范围、正交验证证据与收益。
5. **C-Gate 跨模型自动化裁决与贡献者署名**：PR 经异构模型审计合并后，贡献者将载入 `CONTRIBUTORS.md`，并在协议演进路线图中映射为灵魂绑定声誉权重 $W_i(t)$。

---

### 5. 许可与合规 (PCSE Compliance)

- **代码与引擎**：采用 [MIT License](LICENSE)。
- **PCSE 合规保证**：严格满足零私人真名、零私人财务数字、零第三方平台自动化违规写操作。
- **非金融承诺**：永久无代币化治理，真实法币结算走合规持牌支付通道。
