# 🛡️ Tabelog·Eye + VRO 自主代订与反偏置服务 · 私有化自建部署套件 (Self-Host Kit)

> **Zero-Dependency · Per-Device Fingerprint Isolation · Local SQLite Taste Vault · $100/mo Covenant Budget Gate**

本套件提供完全独立、零外部依赖（Zero External Dependency）的私有化节点服务。只需一台具备 Python 3.10+ 或 Docker 环境的机器（Mac mini、家用 NAS、VPS 或云主机），即可将 **Tabelog·Eye（破偏置真味引擎）** 与 **VRO（Visual-Resonance Orchestrator 自主代订与履约账本）** 完整私有化部署。

---

## 🌟 为什么选择私有化自建？

1. **绝对味觉主权与隐私安全 (Taste Sovereignty)**  
   您的所有私密赏味坐标、3.2–3.6 沧海遗珠收藏、常客小店品鉴笔记与代订意向，**全部以 WAL 模式加密沉淀在您本机的 SQLite 数据库中**，绝不上报或泄露给任何商业中心化平台或公有大模型供应商。
2. **多设备指纹严格隔离 (Per-Device Fingerprint Isolation)**  
   基于加盐散列 (`SHA-256(DEVICE_SALT + Fingerprint)`) 为每台手机或浏览器分配独立的加密 Vault 空间。家庭成员、不同终端各自拥有独立的味觉 DNA 与预约记录，杜绝跨设备数据污染与串号。
3. **$100/月 契约硬顶安全门禁 (Configurable Monthly Budget Cap)**  
   内置硬性博弈论契约安全门禁（Covenant Ledger）。默认月度代订微悬赏与开销硬顶为 **$100.00 USD/月**（可自主配置）。任何试图突破硬顶的自主代订意向将被系统直接阻断（`BUDGET_CAP_EXCEEDED_GATE`），彻底消除自治 AI Agent 误触发或天价账单风险。
4. **五维多模态反偏置引擎 (5-Factor Multimodal De-Biasing Engine)**  
   就地运行「破偏置真味校准法 v1.0」：实时分离刀工炭火火入硬证据（$\Delta_{\text{vision}}$）、超预期语义残差（$\Delta_{\text{surprise}}$）、服务环境正交解耦（$\Delta_{\text{ortho}}$）、贝叶斯样本收缩（$\Delta_{\text{sample}}$）与网红泡沫扣除（$\Delta_{\text{hype}}$），还原 80% 可信区间。

---

## 📦 目录结构

```text
self-host/
├── Dockerfile              # 极简轻量容器镜像 (Python 3.11-slim, 非 root 权限)
├── docker-compose.yml      # 一键编排配置 (包含数据卷挂载与健康检查)
├── server.py               # 零外部依赖 Python 3 标准库 HTTP + SQLite 服务端
├── README-SELF-HOST.md     # 本部署指南与 REST API 交互规范
└── data/                   # 本地 SQLite 数据目录 (持久化 taste_vault.db)
```

---

## 🚀 三分钟快速上手

### 选项 A：Docker Compose 一键启动（推荐）

```bash
# 1. 克隆系统仓库并进入 self-host 目录
git clone https://github.com/MachengShen/system-evolution-public.git
cd system-evolution-public/tabelog-eye-vro/self-host

# 2. 启动容器服务（后台运行）
docker compose up -d

# 3. 验证服务状态
curl -s http://127.0.0.1:8080/health | jq
```

### 选项 B：原生 Python 3 零依赖直跑（无需 pip 安装任何三方库）

仅依赖 Python 标准库（`http.server`, `sqlite3`, `json`, `hashlib` 等）：

```bash
cd self-host

# 设置环境变量并启动（默认监听 0.0.0.0:8080）
python3 server.py
```

### 选项 C：纯 Docker CLI 单行运行

```bash
docker run -d \
  --name tabelog-eye-vro-node \
  -p 8080:8080 \
  -v $(pwd)/data:/app/data \
  --restart unless-stopped \
  tabelog-eye-vro:latest
```

启动完成后，在浏览器打开：
👉 **`http://localhost:8080/`** 即可进入自建节点专属的交互式 Web 仪表盘与实时校准沙箱。

---

## ⚙️ 环境变量配置

可在 `docker-compose.yml` 或操作系统环境中覆盖以下配置项：

| 变量名 | 默认值 | 说明 |
|---|---|---|
| `PORT` | `8080` | HTTP 服务监听端口 |
| `HOST` | `0.0.0.0` | 绑定网卡地址 |
| `DEFAULT_MONTHLY_BUDGET_CAP` | `100.00` | 默认每月 VRO 自主代订履约硬顶 (USD) |
| `VAULT_DB_PATH` | `/app/data/taste_vault.db` | 本地 SQLite 赏味资产保险库文件路径 |
| `DEVICE_SALT` | `tabelog-eye-vro-local-salt-2026` | 设备指纹单向加密混淆盐值 |
| `ALLOW_CORS` | `true` | 是否允许跨域请求（供前端 WebPWA 访问） |

---

## 🗄️ 本地 SQLite 数据表结构

服务首次启动时会自动在 `VAULT_DB_PATH` 初始化以下 5 张表（开启 WAL 模式）：

1. **`device_profiles`**：隔离登记的各设备指纹哈希、别名、个性化味觉 DNA 坐标（旨味、盐度敏感度、炭火权重）。
2. **`taste_assets`**：本地专属赏味资产表。存储各餐厅原始分、校准分、个人私密笔记、状态（`bookmarked`/`visited`/`blacklist`）。
3. **`covenant_budget`**：月度契约预算账本。按账期（`YYYY-MM`）追踪各设备预算硬顶、已实付金额（`spent_usd`）与待批意向（`pending_queue_usd`）。
4. **`vro_reservations`**：VRO 自主代订订单表。状态流转：`PENDING_OWNER_TOKEN` → `AGENT_MATCHING` → `CONFIRMED`。
5. **`debiasing_cache`**：高频校准缓存与手艺证据库。

---

## 🔌 与 Tabelog·Eye 前端连接

在 Tabelog·Eye PWA 或网页端中，点击页面顶部的 **「⚙️ 自建私有节点」** 或在设置中配置：

- **自建服务地址 (Self-Host Endpoint)**：`http://localhost:8080`（或您的内网 Tailscale / LAN IP）
- **客户端设备指纹头**：`X-Device-Fingerprint: <任意字符串或硬件标识>`
- **设备别名头（可选）**：`X-Device-Alias: Macheng-iPhone-16`

前端将自动从自建节点加载本地私密赏味藏馆，并受自建节点的 $100/月 契约硬顶保护。

---

## 📡 REST API 核心接口参考

### 1. 健康检查与节点状态
```bash
curl -X GET http://127.0.0.1:8080/health
```
**响应示例：**
```json
{
  "status": "healthy",
  "service": "Tabelog·Eye + VRO Autonomous Booking & De-Biasing Node",
  "version": "1.0.0-selfhost",
  "uptime_seconds": 128.4,
  "architecture": "zero-dependency-sqlite-vault",
  "stats": {
    "isolated_devices": 1,
    "vault_taste_assets": 12,
    "vro_reservations": 2
  },
  "timestamp": "2026-10-18T08:00:00.000000+00:00"
}
```

---

### 2. 查询当前月度契约预算账本
```bash
curl -X GET http://127.0.0.1:8080/api/vro/budget \
  -H "X-Device-Fingerprint: macheng-macbook-m3"
```
**响应示例：**
```json
{
  "device_id": "dev_3f8a91b2c4e5",
  "billing_cycle": "2026-10",
  "budget_cap_usd": 100.0,
  "spent_usd": 0.0,
  "pending_queue_usd": 24.0,
  "remaining_usd": 76.0,
  "utilization_pct": 24.0,
  "is_exhausted": false,
  "updated_at": "2026-10-18 08:05:12"
}
```

---

### 3. 动态调整月度预算硬顶
```bash
curl -X POST http://127.0.0.1:8080/api/vro/budget/cap \
  -H "Content-Type: application/json" \
  -H "X-Device-Fingerprint: macheng-macbook-m3" \
  -d '{"budget_cap_usd": 150.00}'
```

---

### 4. 提交 VRO 自主代订意向（触发预算硬顶门禁校验）
```bash
curl -X POST http://127.0.0.1:8080/api/vro/book \
  -H "Content-Type: application/json" \
  -H "X-Device-Fingerprint: macheng-macbook-m3" \
  -d '{
    "restaurant_id": "tabelog_13245678",
    "restaurant_name": "鳥恵 上野広小路",
    "target_datetime": "2026-10-25 19:30",
    "party_size": 2,
    "fee_usd": 8.00,
    "notes": "优先吧台板前，偏好鸡肉刺身与白肝炭火手艺"
  }'
```
**安全门禁拦截示例（当开销超过月度硬顶时）：**
```json
{
  "error": "BUDGET_CAP_EXCEEDED_GATE",
  "message": "VRO Autonomous Booking blocked by Covenant Budget Gate. Projected spend ($108.00) exceeds monthly cap ($100.00).",
  "status": 402,
  "details": {
    "budget_cap_usd": 100.0,
    "spent_usd": 80.0,
    "pending_queue_usd": 20.0,
    "requested_fee_usd": 8.0,
    "shortfall_usd": 8.0,
    "resolution": "Increase budget cap via POST /api/vro/budget/cap or wait for next billing cycle."
  }
}
```

---

### 5. 保存/更新本地赏味私藏 (Taste Vault)
```bash
curl -X POST http://127.0.0.1:8080/api/taste/assets \
  -H "Content-Type: application/json" \
  -H "X-Device-Fingerprint: macheng-macbook-m3" \
  -d '{
    "restaurant_id": "rest_torie_01",
    "restaurant_name": "鳥恵 上野広小路",
    "original_score": 3.48,
    "calibrated_score": 3.86,
    "status": "bookmarked",
    "tags": "烧鸟,炭火火入,老客常客",
    "notes": "大将火候精准，被大众网红拉低分数，必吃白肝"
  }'
```

---

### 6. 执行五维破偏置校准计算
```bash
curl -X POST http://127.0.0.1:8080/api/debias/calculate \
  -H "Content-Type: application/json" \
  -d '{
    "restaurant_name": "酒坊 猩々",
    "original_score": 3.34,
    "vision_craft": 0.85,
    "surprise_factor": 0.65,
    "ortho_factor": 0.50,
    "sample_size": 38,
    "hype_penalty": 0.05
  }'
```
**计算结果：**
```json
{
  "original_score": 3.34,
  "calibrated_score": 3.88,
  "total_delta": 0.54,
  "delta_vision": 0.298,
  "delta_surprise": 0.195,
  "delta_ortho": 0.125,
  "delta_sample": 0.014,
  "delta_hype": 0.018,
  "ci_80": [3.65, 4.11],
  "sample_size": 38,
  "restaurant_name": "酒坊 猩々"
}
```

---

## 🔒 安全与合规准则 (Bright-Lines & Privacy)

- **无第三方账号越权 (No Credential Hijacking)**：本服务仅管理您本机的赏味意向与去中心化悬赏账本，不代存您的第三方明文登录密码，不越权操控您的外网个人账号。
- **Fail-Closed 预算门禁**：所有自主代订指令均受本地契约账本硬顶约束，预算不足时强行进入阻断状态，杜绝自动扣费失控。
- **零外部遥测 (Zero Telemetry)**：代码内零埋点、零 Google Analytics、零三方上报。您的数据仅存于本地 `data/taste_vault.db`。

---

*Tabelog·Eye Project · Built with Craft & Zero-Dependency Simplicity.*
