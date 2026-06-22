# Seeded, Then Left Alone: A Falsifiable Reading of Directed Panspermia, and What "Non-Interference" Can Formally Mean

*2026-06-22 · plain-language note for working scientists · theory mainline*

Keywords: Fermi paradox, directed panspermia, origin of life, non-interference,
observability vs controllability, transfer entropy, Markov blanket, falsifiability.

This is a speculative synthesis, written plainly and on purpose kept honest about
its own weaknesses. The durable contribution here is **not** "aliens seeded us" —
that idea is old and, taken alone, weak. The durable contribution is a **formal
distinction**: what it can actually mean for a cause to *create* something and
then *not interfere* with it, when the act of creating unavoidably leaves
information behind. If you only take one thing from this note, take Section 5's
falsifiable tests and the observability-vs-controllability cut.

---

## 1. The hypothesis

Two claims, stacked. The second is the interesting one.

**Claim A (the frame): directed panspermia as a Fermi angle.**
Life — or its precursors — may have been seeded into early Earth from elsewhere,
possibly deliberately by an earlier intelligence (Crick & Orgel, *Icarus*, 1973).
Connected to Fermi's "where is everybody?", the idea runs: for an advanced
civilization, flinging durable microbial seeds across interstellar distances is
orders of magnitude cheaper than flinging ships or signals. So the real signature
of galactic "expansion" might be *quiet seeding of empty niches*, not loud beacons
or visible megastructures. We see no one because (i) the seeders are long gone,
(ii) seeded biospheres develop on independent, tens-of-millions-to-billions-of-year
offset clocks, and (iii) the optimal mature strategy is to densify *inward*
(compute, stay dark) while radiating only a *thin, low-bandwidth, generative*
stream *outward* (seeds), never high-bandwidth peer-beacons. A galaxy run this way
would look exactly as silent as ours does, while still being full of life.

**Claim B (the contribution): "non-interference" needs a formal definition, and
it has one.**
A natural objection kills the casual version of Claim A immediately: *the act of
seeding carries information.* The seeded system can, in principle, reverse-infer
its seeder. So "the seeders left us alone" cannot mean "zero information passed."
What does it mean?

The resolution is a distinction that appears, in four different vocabularies, as
**the same cut**:

| Framework | "Inference" (allowed) | "Interference" (the thing being denied) |
|---|---|---|
| Control theory | reconstruct the initial condition — **observability** (reading) | an ongoing forcing/control input `u(t)` — **controllability** (writing) |
| Causal (Pearl) | the system depends on the seeder's **t0 node** (inferable) | a directed arrow from the seeder's **post-t0 state** into the system |
| Information theory | mutual information stored **at t0**, `I(X₀;Y₀)>0` (decodable) | **directed information / transfer entropy after t0 = 0** |
| Active inference | representing the seeder as a **latent in your own model** | the seeder **crossing your Markov blanket** to drive your internal states |

The one-line version: **inference is reading the past; interference is writing the
future.** A descendant species deducing that it was seeded is performing
*observability* — running its own dynamics backward on its own data. That opens no
channel back to the seeder and changes nothing. **Observability and controllability
are independent** (a textbook duality): a seeder can be perfectly reconstructible
(fully observable) and yet have exactly zero post-seeding control authority. The
information deposited at t0 is both *unavoidable* and *exactly what makes later
inference possible* — and it is still fully compatible with strict
non-interference afterward.

**Non-interference comes in grades, and this matters.** The clean "autonomous after
t0" picture assumes the seeder only set the *initial condition*. But a seeder could
instead (or also) have set the *dynamics themselves* — the laws, the niche, the
selection landscape (`f` in `dx/dt = f(x) + g(x)u(t)`). Setting `f` injects no
ongoing signal yet shapes every future state. So:

- **Strong non-interference**: seeder sets only the initial condition `x₀`; the
  dynamics `f` are native; `u(t)≡0` after t0.
- **Weak non-interference**: seeder authored `f` (or kept a back-channel through a
  shared environment), but injects no explicit ongoing `u(t)`.

Human parenting is the everyday proof that "non-interference" is graded and that
the *strong* form is rare: parents do not merely place an initial condition — they
author the child's value function (`f`) and apply years of `u(t)`. A useful sharper
criterion comes from the 无为 ("act without dominating") reading: non-interference
is **not** "no channel," it is **no `宰` — no steering toward the seeder's preferred
outcome.** Formally, the seeder's behavior is *invariant across the fan of
trajectories the seeded system could take*, including the ones the seeder would
dislike. That is verified only longitudinally: by the seeded thing becoming
something the seeder finds *wrong*, and the seeder still not reaching in.

---

## 2. Supporting evidence

The physical *mechanism* is real and largely uncontroversial; the *deliberate
seeding* is not.

- **Rocks travel between planets.** We hold ~hundreds of Martian meteorites
  (e.g. ALH84001). The "impact ejection → interstellar/interplanetary transit →
  landing" pathway (lithopanspermia) is physically demonstrated, not hypothetical.
- **Life's building blocks are abundant in space.** The Murchison meteorite carries
  70+ amino acids (with slight L-excess); all five DNA/RNA nucleobases have been
  recovered from meteorites (2022); the Rosetta mission detected glycine at comet
  67P. Feedstock genuinely arrives from above.
- **Some microbes survive space exposure.** Tardigrades (ESA exposure) and
  *Deinococcus radiodurans* (Japan's Tanpopo experiment, years on the ISS exterior)
  endure vacuum and radiation — partial support for "a seed can survive transit."
- **Life appears very early on Earth**, hard against the end of late heavy
  bombardment — a tight window for fully local origin-from-scratch.
- **Universal genetic code + homochirality** are consistent with a single origin
  (one seeding, or one common ancestor).
- **Fermi silence itself** is *predicted* by the "dark-dense inward, thin-seed
  outward" reading, whereas it is an awkward surprise for "loud expansion" models.

---

## 3. Counter-evidence

Stated bluntly, because a scientist audience deserves it.

- **It relocates the origin; it does not solve it.** "Life came from elsewhere"
  leaves "how did life first arise" untouched — an infinite regress. As a Fermi
  *solution* it secretly assumes a seeder civilization that itself arose and
  crossed interstellar space.
- **Universality + homochirality are fully explained without aliens** — by common
  descent (LUCA) plus an early "frozen accident," and by abiotic
  symmetry-breaking mechanisms for chirality. They are not evidence *for* seeding.
- **Genetic "designer signatures"** (e.g. the shCherbak–Makukov 2013 "Wow! signal
  in the genetic code") are widely regarded as post-hoc numerology, not robust.
- **Crick's molybdenum argument** (life leans on a relatively scarce element →
  hint of an off-Earth origin) is essentially wrong; Crick himself later
  downplayed it. Early-ocean chemistry supplies the needed trace elements.
- **Transit lethality.** Lab survival is short and shielded; real interstellar
  transit means megayear cosmic-ray doses that kill the overwhelming majority,
  meteorite shielding only partially helping.
- **LUCA's biochemistry looks local** — tightly matched to early-Earth
  hydrothermal/geochemical conditions, i.e. grown in place, not transplanted.
- **The "early appearance" window is contested**, and "fast" does not entail
  "imported."
- **Fermi-specific:** if there were a seeder, why only one wave? Where are later
  waves, newer probes, observable engineering?

---

## 4. Why (and exactly where) this is more parsimonious — and where it is *not*

Be careful with Occam here, because it cuts **against** the naive version.

- **Naive directed panspermia loses on Occam.** It *adds* an entity (the seeder)
  and pushes the origin problem back a step. On its own it is less parsimonious
  than local abiogenesis. Anyone selling it as "simpler" is wrong.

- **Where the framework is genuinely more parsimonious is narrower and real:**
  *explaining the silence.* Competing Fermi stories tend to bolt on one *ad hoc*
  premise each — "they all died," "they're hiding" (zoo hypothesis as a bare
  posit), "they never arise" (rare-earth). The "dark-dense inward / thin-seed
  outward" optimality principle is **one** assumption that, if granted, *jointly*
  predicts: (a) cosmic silence, (b) common biosignatures, (c) absent technosignatures,
  and (d) non-interference as a *derived* consequence rather than a posited one.
  Fewer independent assumptions *per observation explained* — that is the only
  Occam advantage being claimed, and it is conditional on the optimality premise
  being true.

- **The non-interference formalization stands on its own**, independent of whether
  any seeding happened. It upgrades the zoo hypothesis from "they choose not to
  contact us" (an unexplained choice) to "non-interference is what an optimal
  boundary-respecting structure *does*, with a measurable definition." That is a
  real conceptual gain: a derived prediction beats a free parameter.

Net honest verdict: **as cosmology, this is a speculative frame, not a favored
theory. As epistemics, the inference-vs-interference cut is the part worth keeping.**

---

## 5. Caveats and falsifiable tests

**Caveats (limits you must hold in mind):**

1. **Non-identifiability.** Any residual seeder→system dependence can always be
   "explained away" by positing an unobserved common cause. So a perfectly clean
   causal verdict may be unreachable from observation alone.
2. **The `f`-authorship ambiguity** (weak vs strong non-interference) is rarely
   decidable from inside the seeded system.
3. **Category risk (Kantian caveat).** "We have a seeder/parent" may partly reflect
   *the form of our cognition* — causality is a category we impose — rather than a
   detected thing-in-itself. Distinguish "we discovered a cause" from "we
   constructed the concept of one." (A newborn does not *observe* a parent; it
   *builds* the category, late, from its own data.)
4. **Projection risk (stated against interest).** "Create, then lovingly let go,
   without possessing" is an emotionally attractive shape. A theory that keeps
   landing on the consolation its author wants should be distrusted *more*, not
   less. This note is not exempt.

**Falsifiable tests (how to kill it):**

1. **Differential signature prediction.** The framework predicts **biosignatures
   should be common while technosignatures/beacons stay near zero.** Found via
   biosignature surveys (JWST-class atmospheric spectroscopy) vs the continuing
   SETI null. *Killed if* we instead find a galaxy of mutually broadcasting
   civilizations (loud peers), which contradicts "mature strategy is dark + thin
   seeding."

2. **No designer watermark in the genetic code.** Because seeding is *substrate
   dispersal*, not *messaging*, the framework predicts the genetic code carries
   **no** intentional message. So the shCherbak-style "signal" being spurious is
   *consistent* with this theory — and a robust, replicated demonstration that it
   is **real** would **refute** the dispersal reading (it would imply communication,
   a different optimum).

3. **Operational non-interference criterion (for any candidate seeded system, in
   principle).** Define interference as **non-zero environment/`do`-conditioned
   directed information from the seeder's post-t0 trajectory into the system**,
   while t0 mutual information stays large:
   - non-interference ⇔ `I(seeder_{>t0} → system_{>t0} ‖ system_past, do(env)) = 0`
     with `I(seeder₀; system₀) ≫ 0`;
   - equivalently (control form): `∂x(t)/∂S(τ>t0) = 0` (system insensitive to the
     seeder's *later* state) while `∂x(t)/∂x₀ ≠ 0` (the seed obviously mattered).
   This is measurable in bits and has clear failure modes: a residual that *never*
   vanishes as you enrich the conditioning set signals either real interference or
   an incomplete environment model.

4. **Precommitment / trap check.** A t0-baked rule contingent on the system's
   *future* state ("if it reaches φ, the seeded substrate yields ψ") is control
   *without a live controller* — it passes a naive "no live arrow" test yet steers
   outcomes. A complete criterion must check whether the t0 setup is a *constant*
   or a *future-contingent policy* baked into the substrate.

5. **Longitudinal `无为` test.** Real non-interference is verified over the whole
   trajectory: the seeded system must be able to become something the seeder would
   *dislike* with no correction arriving. If across the entire history the system
   only ever grows into shapes the seeder would find acceptable, "non-interference"
   was decorative — the constraint was installed at t0, not absent.

---

*This note is part of an open, continuously-published theory line. It is offered
for others to extend, test, or refute — not as a settled claim. The
inference-vs-interference (observability-vs-controllability) distinction, the
graded weak/strong non-interference definitions, and the five tests above are the
parts meant to be reused.*

---

<a name="chinese"></a>

# 中文版(大白话):播种之后,就放手了 —— 给"定向胚种论"一个能被证伪的读法,以及"不干预"到底是什么意思

*2026-06-22 · 写给普通科研工作者的大白话 · 理论主线*

关键词:费米悖论、定向胚种论、生命起源、不干预、可观测性 vs 可控性、转移熵、马尔可夫毯、可证伪性。

先把丑话说前头:这是一个**思辨性的综合**,故意写得直白、也故意对自己的弱点诚实。这篇真正值钱的东西**不是**"外星人播种了我们"——那个想法又老又弱。真正值钱的是一个**形式化的区分**:当"创造"这个动作本身不可避免地会留下信息时,一个原因"创造了某物、然后不干预它",到底能是什么意思?如果你只带走一样东西,请带走第 5 节的可证伪实验,和"可观测性 vs 可控性"这把刀。

## 1. 这套假说是什么

两层主张,叠在一起。第二层才是有意思的那层。

**主张 A(框架):把定向胚种论当成费米悖论的一个角度。**
生命(或其前体)可能是从别处被播种到早期地球的,甚至可能是某个更早的智慧**故意**播的(Crick & Orgel, 1973)。接到费米的"大家都在哪儿?":对一个先进文明来说,把耐用的微生物种子撒过星际距离,比派飞船、发信号便宜好几个数量级。所以银河系"扩张"的真实签名,也许是**安静地往空生态位里播种**,而不是响亮的信标或显眼的巨型工程。我们之所以谁也看不到,是因为:(i) 播种者早已不在;(ii) 被播种的生物圈各按相差几千万到几十亿年的钟独立发育;(iii) 成熟文明的最优策略是**向内致密**(算力、保持黑暗),只向外辐射一条**又细又低带宽、生成性**的种子流,**绝不**向同侪打高带宽信标。这样运作的银河系,看起来会和我们看到的一样寂静,却同时充满生命。

**主张 B(贡献):"不干预"需要一个形式化定义,而且它有一个。**
一个很自然的反驳能立刻杀死 A 的粗糙版本:**播种这个动作本身就携带信息。** 被播种的系统原则上能反推出它的播种者。所以"播种者没干预我们"不可能意味着"零信息传递"。那它到底是什么意思?

答案是一个区分——它用四套不同的语言说的其实是**同一刀**:

| 框架 | "推理"(允许) | "干预"(被否定的那个) |
|---|---|---|
| 控制论 | 反推初始条件 = **可观测性**(读) | 持续的控制输入 `u(t)` = **可控性**(写) |
| 因果(Pearl) | 系统依赖播种者的 **t0 节点**(可推) | 从播种者 **t0 之后状态**指向系统的箭头 |
| 信息论 | **t0 时存入**的互信息 `I(X₀;Y₀)>0`(可解码) | **t0 之后的定向信息/转移熵 = 0** |
| 主动推断 | 把播种者当成你**自己模型里的隐变量** | 播种者**跨过你的马尔可夫毯**来驱动你的内部状态 |

一句话:**推理是读过去,干预是写未来。** 一个后代物种推断出自己是被播种的,这是在做**可观测性**——拿自己的动力学、在自己的数据上做反演。它不往播种者那边开任何通道,也什么都不改变。**可观测性和可控性是相互独立的**(教科书里的对偶):播种者可以被完美重构(完全可观测),同时对播种之后的事拥有**零**控制权。t0 存下的信息既是**不可避免的**、又**正好是日后推理之所以可能的原因**——而它和之后的严格不干预,完全不冲突。

**"不干预"是分档的,这点很重要。** 干净的"t0 之后自治"图景,假设了播种者只设了**初始条件**。但播种者也可能(或同时)设定了**动力学本身**——规律、生态位、选择地形(方程里的 `f`)。设定 `f` 不注入任何持续信号,却塑造了每一个未来状态。所以:

- **强不干预**:播种者只设初始条件 `x₀`;动力学 `f` 是原生的;t0 之后 `u(t)≡0`。
- **弱不干预**:播种者写了 `f`(或通过共享环境留了后门),但不注入显式的持续 `u(t)`。

**人类养孩子**就是日常证据,证明"不干预"是分档的、而且**强**的那一档很罕见:父母不只是放下一个初始条件——他们**编写了孩子的价值函数(`f`)**,还施加了好多年的 `u(t)`。一个更锋利的判据来自"无为"(为而不宰)的读法:不干预**不是**"没有通道",而是**没有"宰"——不朝着播种者偏好的结果去操纵**。形式化地说:**在被播种系统可能走的所有轨迹(包括播种者讨厌的那些)上,播种者的行为保持不变。** 这只能**纵向**验证:被播种的东西长成了播种者觉得"错"的样子,而播种者依然没有伸手。

## 2. 支持性证据

物理**机制**是真实的、基本没争议;**故意播种**则没有。

- **石头会在行星之间穿行。** 人类已捡到约数百块火星陨石(如 ALH84001)。"撞击抛射→星际/行星际穿行→落地"(岩石胚种)这条路径是被证实的,不是空想。
- **生命的砖块在太空里普遍存在。** Murchison 陨石含 70+ 种氨基酸(且有轻微 L 型过量);DNA/RNA 五种碱基都已从陨石中找到(2022);Rosetta 在 67P 彗星上测到甘氨酸。原料确实从天上来。
- **有些微生物扛得住太空暴露。** 水熊虫(ESA)和耐辐射球菌(日本 Tanpopo 实验,在 ISS 外壁存活数年)能熬过真空和辐射——对"种子能熬过旅途"的部分支持。
- **生命在地球出现得极早**,紧贴晚期重轰炸结束——留给"纯本地从零起源"的窗口很紧。
- **遗传密码通用 + 同手性**,与单一来源一致(一次播种,或一个共同祖先)。
- **费米寂静本身**被"向内致密、向外细播"读法**预测**到了;而对"响亮扩张"模型来说它是个尴尬的意外。

## 3. 反面证据

直说,因为科研读者值得直说。

- **它把起源搬了家,没解决起源。** "生命来自别处"原封不动留下了"生命最初怎么来的"——无穷回退。作为费米**解**,它偷偷假设了一个自己也得起源、还跨越了星际的播种文明。
- **通用性 + 同手性,不需要外星人也能完全解释**——用共同祖先(LUCA)加早期"冻结的偶然",手性则有非生物的对称性破缺机制。它们**不是**支持播种的证据。
- **基因"设计者签名"**(如 shCherbak–Makukov 2013 "遗传密码里的 Wow! 信号")被普遍视为事后凑数,不稳健。
- **Crick 的钼论证**(生命依赖一种相对稀缺的元素→暗示地外起源)基本是错的,Crick 本人后来也淡化了。早期海洋化学能供给所需微量元素。
- **旅途致死率。** 实验室存活是短时、有屏蔽的;真实星际穿行意味着百万年级的宇宙射线剂量,绝大多数会被杀死,陨石屏蔽只帮一部分。
- **LUCA 的生化看起来很本地**——与早期地球热液/地质条件严丝合缝,像是就地长出来的,不是移植来的。
- **"出现得早"这个窗口有争议**,而且"快"不等于"进口"。
- **费米专属反驳:** 若真有播种者,为什么只播一次?后续的波次、更新的探针、可观测的工程在哪?

## 4. 为什么(以及到底在哪儿)它更说得通 —— 又在哪儿**并不**

奥卡姆剃刀在这儿要小心用,因为它砍的是**粗糙版本**。

- **粗糙的定向胚种论输给奥卡姆。** 它**多加**了一个实体(播种者),还把起源问题往后推了一步。单论它自己,比本地自发起源更不简约。谁把它当"更简单"来卖,谁就错了。

- **这套框架真正更简约的地方,更窄、也更真:解释寂静。** 别的费米故事往往各自硬加一条 *ad hoc* 前提——"他们都死了""他们在躲"(动物园假说作为一个裸假设)"他们根本不出现"(稀有地球)。而"向内致密 / 向外细播"这条最优性原则,是**一个**假设,一旦承认,就**同时**预测出:(a) 宇宙寂静、(b) 生物签名普遍、(c) 技术签名缺失、(d) 不干预是**推导出来的**结果而非假定的。**每解释一个观测所需的独立假设更少**——这是唯一被主张的奥卡姆优势,且以"最优性前提为真"为条件。

- **不干预的形式化是独立成立的**,跟到底有没有发生过播种无关。它把动物园假说从"他们选择不联系我们"(一个没解释的选择)升级成"不干预是一个尊重边界的最优结构**本来就会做的事**,而且有可测量的定义"。这是真正的概念收益:推导出来的预测,胜过一个自由参数。

诚实的总评:**作为宇宙学,这是个思辨框架,不是受青睐的理论。作为认识论,"推理 vs 干预"这把刀才是值得留下的部分。**

## 5. 限制条件 与 可证伪的实验

**限制条件(必须记住的边界):**

1. **不可识别性。** 任何残余的"播种者→系统"依赖,总能用"假设一个没观测到的共同原因"来解释掉。所以单靠观测,也许永远拿不到一个干净的因果判决。
2. **`f`-作者权的歧义**(弱 vs 强不干预),从被播种系统内部往往判不出来。
3. **范畴风险(康德式限制)。** "我们有个播种者/父母",可能部分反映的是**我们认知的形式**——因果是我们套上去的范畴——而不是被探测到的物自体。要分清"我们发现了一个原因"和"我们构造了'原因'这个概念"。(婴儿不是**观测**到父母,而是后天用自己的数据**构造**出这个范畴的。)
4. **投射风险(对自己不利地说出来)。** "创造,然后充满爱地放手、不占有",是个情感上很有吸引力的形状。一个老是落在作者想要的安慰上的理论,应该被**更加**怀疑,而不是更少。本文不例外。

**可证伪的实验(怎么杀死它):**

1. **差分签名预测。** 框架预测:**生物签名应当普遍,而技术签名/信标接近于零。** 用生物签名巡天(JWST 级大气光谱)对比持续的 SETI 零结果来查。**反例致死:** 若我们反而发现一个互相广播的文明遍地(响亮的同侪),就和"成熟策略是黑暗 + 细播"矛盾。

2. **遗传密码里没有设计者水印。** 因为播种是**substrate 分散**而非**通信**,框架预测基因码**不**带有意的消息。所以那个 shCherbak 式"信号"是假的,**符合**本理论;而如果有人稳健地、可重复地证明它是**真的**,则**反驳**了分散读法(那意味着通信,是另一个最优)。

3. **可操作的不干预判据(原则上对任何候选被播种系统适用)。** 把干预定义为**对环境/`do` 条件化后,从播种者 t0 之后轨迹流入系统的定向信息非零**,而 t0 互信息仍然很大:
   - 不干预 ⇔ `I(播种者_{>t0} → 系统_{>t0} ‖ 系统过去, do(环境)) = 0`,且 `I(播种者₀; 系统₀) ≫ 0`;
   - 等价地(控制论形式):`∂x(t)/∂S(τ>t0) = 0`(系统对播种者的**后续**状态不敏感),同时 `∂x(t)/∂x₀ ≠ 0`(种子显然有用)。
   这是以比特为单位可测的,且有清晰的失败模式:一个**无论怎么丰富条件集都不消失**的残差,意味着要么真有干预,要么环境模型不完整。

4. **预承诺/陷阱检查。** 一个 t0 时就埋好、却**取决于系统未来状态**的规则("若它达到 φ,被播种的 substrate 就产出 ψ")是**没有活控制器的控制**——它能通过幼稚的"没有活箭头"测试,却仍在操纵结果。一个完整的判据必须检查:t0 的设定是个**常数**,还是一条埋进 substrate 的**取决于未来**的策略。

5. **纵向"无为"测试。** 真正的不干预要在整条轨迹上验证:被播种的系统必须**能**长成播种者会**讨厌**的样子,且没有任何纠正到来。如果在整段历史里它只长成播种者能接受的形状,那"不干预"就是装饰品——约束是 t0 时装好的,不是不在。

---

*本文属于一条开放、持续发布的理论线。它供他人扩展、检验或反驳,而非作为定论。"推理 vs 干预"(可观测性 vs 可控性)的区分、弱/强不干预的分档定义,以及上面五个测试,是打算被复用的部分。*
