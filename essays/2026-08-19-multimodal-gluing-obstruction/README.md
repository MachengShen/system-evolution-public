# multimodal-gluing-obstruction — E1/E2 判决实验

源理论:[../2026-08-19-multimodal-gluing-obstruction.md](../2026-08-19-multimodal-gluing-obstruction.md)(2026-08-18,owner 已 ratify 跑 E1+E2)
上游:`~/projects/information-dynamics/THEORY-v3.md`(cokernel 残差 r_perp)+ `exp_discounted_cokernel.py`

## 命题
两模态 = 同一 latent 的两个有损投影 ⟹ 跨模态对齐约束在「约束数 > latent 自由度」后 generically overdetermined,
存在**改 loss 消不掉的残差底**。对照假说(场内主流):modality gap = InfoNCE 优化缺陷,可修(xNCE, arXiv:2607.10698)。

- **E1(合成)**:已知 latent + 已知有损投影,扫 约束数/自由度 比。预测=阈值跳变 + 最优 loss 压不掉。
  falsifier:充分训练后残差随训练/规模单调→0 ⟹ 障碍论不成立,就地停。
- **E2(真模型)**:CLIP/SigLIP 现成 embedding,按 Plato's Cave(arXiv:2604.18572)协议扫数据规模,
  同时算 r_perp。预测=r_perp 上升定量解释对齐衰减;按 r_perp 分层后低残差子集不随规模衰减。
  falsifier:r_perp 与对齐衰减无关 ⟹ 弃。

## 状态
- [x] E1 done 2026-08-18(阈值跳变✓ floor 不可消✓ falsifier 未触发;见 RESULTS-E1.md)
- [x] E2 DONE(2026-08-19)— 判决:co-trained(CLIP/SigLIP)上 P1、P2 证伪(r_perp 随规模下降);独立训练对(DINOv2×mpnet,即原论文 regime)上 r_perp 早期按预测方向上升(partial r=−0.94)后平台 = 幸存 regime;P2 全线失败;粒度签名(粗可粘、细不可)三对模型全过。详见 RESULTS-E2.md §12
数字以 RESULTS-E1.md / RESULTS-E2.md 为准;stub 非空即有人在写,空 = agent 没落盘 = 失败。
