# Deterministic verification report: gain separation toy models

Scope: these checks validate only the stated equations and numerical implementation. They provide no evidence for physical integration subsets, boundary formation, agency, consciousness, or real-world systems.

## 1. Reboosting the current normalized matrix

For

\[
q_{n+1}=(1-g)q_n+g\frac{bq_n}{1+(b-1)q_n},
\]

direct iteration agrees with

\[
q_{n+1}-q_n=\frac{g(b-1)q_n(1-q_n)}{1+(b-1)q_n}
\]

to a maximum absolute error of `1.78e-16`. With `b=3` and `q0=0.2`:

| gain `g` | `q(20)` | `q(100)` | `q(1000)` |
|---:|---:|---:|---:|
| 0.05 | 0.457592400 | 0.953553210 | 0.999999999999996 |
| 0.20 | 0.916075186 | 0.999999074 | 0.9999999999999998 |
| 0.80 | 0.999999352 | 0.9999999999999998 | 0.9999999999999998 |

For the tested positive initial mass, every gain approaches the same attracting fixed point `q=1`; gain changes speed. (`q=0` is also an algebraic fixed point, but is not reached from `q0=0.2`.) This confirms that repeatedly boosting the current normalized matrix does not implement a fixed partial target.

## 2. Anchored target update

For the fixed target

\[
q_* = \frac{bq_0}{1+(b-1)q_0},\qquad
q_{n+1}=(1-\eta)q_n+\eta q_*,
\]

iteration agrees with the closed form `q_n=q_*+(1-eta)^n(q0-q_*)` to `1.39e-15` maximum absolute error.

| `b` | fixed target `q*` | `q(20), eta=.05` | `q(20), eta=.2` | `q(20), eta=.8` |
|---:|---:|---:|---:|---:|
| 1.5 | 0.272727273 | 0.246655569 | 0.271888784 | 0.272727273 |
| 3.0 | 0.428571429 | 0.346631789 | 0.425936179 | 0.428571429 |
| 6.0 | 0.600000000 | 0.456605631 | 0.595388314 | 0.600000000 |

All nine runs agree with their target by step 1000 to within `1.39e-15`. Thus `eta` changes relaxation rate only, while `b` changes the target.

## 3. Adaptive continuous toy

For

\[
\dot x=-x+u+k,\qquad \dot k=\epsilon(-k+a\tanh x),
\]

the equilibrium curve is `u=x-a*tanh(x)`. Independent bisection of `1-a*sech(x)^2` reproduced the positive fold `acosh(sqrt(a))` with maximum error `5.00e-16`. The drive-width computed from the numerical folds reproduced

\[
2\left(\sqrt{a(a-1)}-\operatorname{acosh}\sqrt a\right)
\]

with maximum error `6.66e-16`.

| `a` | positive fold `x` | static drive width |
|---:|---:|---:|
| 1.05 | 0.221784127 | 0.014689315 |
| 1.20 | 0.433507363 | 0.112781171 |
| 1.50 | 0.658478948 | 0.415092911 |
| 2.00 | 0.881373587 | 1.065679951 |

For every `a` above and `epsilon` in `{0.2, 1, 5}`, the Jacobian eigenvalues classify `x=0` as a saddle and a sample on each outer branch as stable. Static equilibria and folds do not depend on `epsilon`; eigenvalues and finite-rate behavior do.

## 4. Illustrative finite-rate RK4 sweep

Each run starts at the stable equilibrium at `u=-3`, ramps to `u=3`, holds until `max(|xdot|,|kdot|)<=1e-11`, carries the full `(x,k)` state into the down-ramp, then equilibrates again at `u=-3`. The table reports the separation between the up- and down-sweep `x=0` crossings.

| `a` | `epsilon` | gap at rate .02 | gap at rate .005 | gap at rate .00125 | static width |
|---:|---:|---:|---:|---:|---:|
| 0.5 | 0.5 | 0.14947 | 0.039698 | 0.0099948 | 0 |
| 0.5 | 2.0 | 0.09803 | 0.024959 | 0.0062493 | 0 |
| 1.5 | 0.5 | 0.99844 | 0.68172 | 0.53187 | 0.41509 |
| 1.5 | 2.0 | 0.83168 | 0.59743 | 0.49255 | 0.41509 |

The gap moves monotonically toward zero for `a=0.5` and toward the nonzero static fold width for `a=1.5` as the sweep slows. The slowest finite-rate runs remain above the static limit, so this is an approach trend rather than a numerical zero-rate extrapolation. For the selected run (`a=1.5`, `epsilon=.5`, rate `.005`), halving `dt` from `.05` to `.025` changes the gap by `4.57e-7`.

Independent Atlas verification (2026-09-06) reproduced every stored section, halved the step size over the full sweep grid, and compared three points using DOP853 with event-located crossings. The largest spot-check difference was about `2.3e-6`; this is not a rigorous global error bound. The readable table uses about five significant digits. More digits in the raw JSON are stored numerical output, not a claim of corresponding accuracy.

## 5. Fixed-coupling negative control

The non-adaptive system

\[
\dot x=x-x^3+u
\]

has stable states `x=-1` and `x=+1` at `u=0`, which can receive arbitrary sign-readout labels A/B despite having the same magnitude. Its folds are at `x=+/-1/sqrt(3)` and its static drive width is `4/(3*sqrt(3)) = 0.769800359`.

Therefore, static hysteresis plus a binary membership-style label is not specific to adaptive membership feedback. The labels in this negative control are readout conventions, not genuine physical integration subsets.

## Limits of the verification

- The normalized update assumes a fixed selected subset, fixed `b`, and a scalar internal mass `q`; changing subsets or matrix structure are outside the check.
- The fold calculation is an equilibrium statement. It does not imply universal rate independence of dynamical stability.
- The RK4 sweep is illustrative and deterministic. Only one run received a step-size convergence check, and no stochastic, spatial, empirical, or real-world claim was tested.
- The negative control rejects mechanism specificity for hysteresis/readout alone; it does not show that every proposed membership-loop property is reproduced by a double well.

Reproduction: run `verify.py` with Python 3. It uses only the standard library and rewrites `results.json`; success requires every embedded assertion to pass.
