# Liberation is reachability, not custody

Date: 2026-09-07 · Cognitive state: 🟡 **speculative** (confidence 0.6) — a synthesis
over published evidence, not a result. The literature claims below are
`survived-stress-test`; the strategic conclusion drawn from them is not.

## The question

"Closed platforms lock users in. Can we get the users out?" Two answers get
proposed almost immediately, by almost everyone. Both are wrong, and they are
wrong for different reasons worth separating.

## Answer 1: reverse-engineer the recommender — VOID

Not hard. **The project conditions do not obtain.** The model-extraction
literature ([arXiv:2109.01165](https://arxiv.org/abs/2109.01165), RecSys'21)
assumes an attacker-chosen query interface returning scored top-N lists over a
closed catalog. A live UGC platform offers none of that: candidate pools are
~10⁹, the model trains online continuously (so the target moves daily), and a
large fraction of "the model" is per-user hidden state inside the serving stack —
there is no stationary, user-independent artifact to extract.

Two further facts close it. First, production clients sign every request
(rotating request signatures + device fingerprints), so any non-official client
must break the signing scheme first — in several jurisdictions that specific act,
not the reading, is what anchors prosecution. Second, and most instructive:
**"read-only, and it's my own account" is not a shield.** AlgorithmWatch
automated the reading of ~1,500 *consenting volunteers' own* Instagram feeds in
2020-21, received a cease-and-desist citing the terms-of-service ban on automated
collection, and deleted the project rather than litigate. Platform automation
policies generally do not distinguish read from write, or your account from
anyone else's.

The consolation is real: the priors you wanted are already published for free.
Follow > like > dwell-time in reshaping a feed
([arXiv:2201.12271](https://arxiv.org/abs/2201.12271), WWW'22); interest profiles
lock in within roughly two hours of viewing; and the platforms publish their own
architecture class (e.g. [NoteLLM](https://arxiv.org/abs/2403.01744), WWW'24).
You do not need to steal what the venue already printed.

## Answer 2: a content-generation engine — commodity, and structurally blind

The generation engine sits **upstream of a delivery channel it does not own**.
It never touches the audience at all. This is the structural difference from the
canonical creator-tool win: the newsletter platform succeeds because the mailing
list is an asset the platform cannot revoke *and* because the tool itself **is**
the pipe to the reader. A generation engine has neither property. Meanwhile the
capability is commoditizing to zero — one well-funded incumbent went from ~$120M
to ~$55M in revenue in a year, losing a reported 60% of subscribers to native AI
features inside tools people already had open.

## What the migration record actually says

Every instinct to "move the users somewhere better" runs into the same wall:

- Mastodon: ~2.6M MAU peak (Nov 2022) → under 1M by 2026.
- The best-case cohort — academics with pre-built networks — went 7,505 active
  to 2,398 in eleven months ([arXiv:2406.04005](https://arxiv.org/abs/2406.04005), ICWSM'24).
- Bluesky: ~42M registered, but mobile MAU −27% YoY and DAU ~3M by mid-2026.
- Lemmy: ~1.9M peak signups → ~130K MAU, while the incumbent's DAU *rose*.
- Algorithmic pluralism is a power-user feature, not a mass demand: of ~5M
  Bluesky users studied, **2.8%** ever liked a custom feed, across 39,639 feeds
  ([PLOS ONE 2025](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0318034)).

And the legal lever is decorative where it matters most. GDPR Art. 20's
peer-reviewed verdict after years of operation is that inter-service transfer
"is far from being fulfilled" ([PoPETs 2021(3)](https://petsymposium.org/popets/2021/popets-2021-0051.pdf));
challengers have not used portability to lower their switching-cost disadvantage.
The EU's messaging-interoperability mandate produced two minor integrations in
three and a half years with no measurable uptake. Where portability exists at
all, the export is an advertising-taxonomy proxy — a few dozen coarse interest
tags — never the recommender's actual state, and the destinations offered are
cloud-storage backends rather than rival networks.

## The reframe

The failure is in the translation. "Liberation" gets silently rendered as
**custody** — get my data back onto my own disk. Custody is real, and it is
solvable alone, at n=1, today, with unglamorous per-source export scripts into a
local database. That shape is the only one in this space that survived a decade,
precisely because it served a market of one and never tried to be a platform.

But custody is the *secondary* problem. The primary one, the one people actually
feel, is **reachability**: *I cannot reach the people and the content I actually
want.* The feed shows me what the objective function guesses I will click; the
person or the essay I want is a few degrees away and out of reach. Getting my
data home does not move that by one millimetre.

Reachability is a matching problem, and matching is where the evidence gets
sharp in a useful way. Two findings, pointing the same direction:

- **Positive:** day-one network reconstruction is the single strongest predictor
  of retention after any platform move
  ([arXiv:2505.24801](https://arxiv.org/abs/2505.24801), n=276,431). Not "build
  it and they will come" — *explicitly rebuild the graph on day one*.
- **Negative:** embedding-based people-matching needs density. The production
  systems that work run on ~10⁸-node graphs. The 2012-14 ambient-social-discovery
  generation worked at a conference and died everywhere else.

Together these have exactly one exit. **Below the density threshold, do not
build a matching engine — reconstruct the graph by hand.** At small n a human
reading five profiles beats any embedding index. What the machine should do is
not the judging but the *remembering*: hold the structured, append-only record of
what each person is trying to reach, across more people than a human can keep in
working memory at once. Judgment stays human; recall becomes mechanical.

That inverts the usual build order, and it has a pleasant property: it degrades
gracefully. If density never arrives, the hand-cranked version was still
delivering the actual good the whole time. Mechanise only when the volume of
matches outgrows a person's reading capacity — **triggered by density, not by
interest in building it.**

## Falsifiers

This note is wrong if any of these show up: a small-n (n < 10³) interest-matching
layer that demonstrably outperforms hand-curation on a retention metric; a
portability regime anywhere that produces a measurable increase in cross-platform
switching; or a documented case of an external party recovering usable production
ranking behaviour from a live large-scale recommender without privileged access.
