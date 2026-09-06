#!/usr/bin/env python3
"""Small mathematical witnesses; no empirical claim or old rig execution."""
import itertools
import json
import math
from pathlib import Path


def outer(v):
    return [[a * b.conjugate() for b in v] for a in v]


def purity(m):
    return sum(m[i][j] * m[j][i] for i in range(len(m)) for j in range(len(m))).real


def partial_a(m):
    return [[sum(m[2*i+b][2*j+b] for b in range(2)) for j in range(2)] for i in range(2)]


def partial_b(m):
    return [[sum(m[2*a+i][2*a+j] for a in range(2)) for j in range(2)] for i in range(2)]


def entropy(p):
    return -sum(x * math.log2(x) for x in p if x > 0)


def kron(a, b):
    return [[a[i//len(b)][j//len(b)] * b[i%len(b)][j%len(b)]
             for j in range(len(a)*len(b))] for i in range(len(a)*len(b))]


def trace_product(a, b):
    return sum(a[i][j]*b[j][i] for i in range(len(a)) for j in range(len(a))).real


def main():
    count = 0
    # Every map of four states, under every bijective four-state recoding.
    for f in itertools.product(range(4), repeat=4):
        for enc in itertools.permutations(range(4)):
            dec = [enc.index(i) for i in range(4)]
            g = [enc[f[dec[y]]] for y in range(4)]
            assert all(g[enc[x]] == enc[f[x]] for x in range(4))
            count += 1

    cases = []
    for sign in (1, -1):
        v = [complex(1/math.sqrt(2)), 0j, 0j, complex(sign/math.sqrt(2))]
        rho = outer(v)
        a, b = partial_a(rho), partial_b(rho)
        xx = sum(v[i].conjugate() * v[3-i] for i in range(4)).real
        assert abs(purity(rho)-1) < 1e-14
        assert abs(purity(a)-.5) < 1e-14 and abs(purity(b)-.5) < 1e-14
        assert abs(xx-sign) < 1e-14
        cases.append({"relative_phase_sign": sign, "global_purity": purity(rho),
                      "marginal_purity": purity(a), "z_measurement_probabilities": [abs(x)**2 for x in v],
                      "z_measurement_entropy_bits": entropy([abs(x)**2 for x in v]),
                      "xx_expectation": xx})

    # All four pure joint states of an ordinary classical pair of bits.
    classical = []
    for index in range(4):
        joint = [int(i == index) for i in range(4)]
        a = [joint[0]+joint[1], joint[2]+joint[3]]
        b = [joint[0]+joint[2], joint[1]+joint[3]]
        assert sum(x*x for x in a) == 1 and sum(x*x for x in b) == 1
        classical.append({"joint_point": index, "a": a, "b": b})

    # Same initial |+>, same mean energy zero; H=0 and H=Z/2 have different futures.
    times = [0, math.pi/2, math.pi]
    quantum_dynamics = [{"t": t, "mean_energy_both": 0, "x_under_H0": 1,
                         "x_under_Hz": math.cos(t)} for t in times]
    assert abs(quantum_dynamics[-1]["x_under_Hz"] + 1) < 1e-14
    # A real-quantum joint distinction invisible to every product of real local effects.
    identity = [[1, 0], [0, 1]]
    x, z, y = [[0, 1], [1, 0]], [[1, 0], [0, -1]], [[0, -1j], [1j, 0]]
    ii, yy = kron(identity, identity), kron(y, y)
    rhos = [[[complex(ii[i][j] + sign*yy[i][j])/4 for j in range(4)]
             for i in range(4)] for sign in (1, -1)]
    pplus = [[complex(ii[i][j]+yy[i][j])/2 for j in range(4)] for i in range(4)]
    local_differences = [trace_product(rhos[0], kron(a, b))-trace_product(rhos[1], kron(a, b))
                         for a in (identity, x, z) for b in (identity, x, z)]
    global_probabilities = [trace_product(rho, pplus) for rho in rhos]
    assert local_differences == [0.0]*9 and global_probabilities == [1.0, 0.0]
    assert all(all(value.imag == 0 for row in rho for value in row) for rho in rhos)
    for rho in rhos:
        assert sum(rho[i][i] for i in range(4)) == 1
        assert all(sum(rho[i][k]*rho[k][j] for k in range(4)) == rho[i][j]/2
                   for i in range(4) for j in range(4))
    result = {"scope": "Conditional mathematical witnesses, not a theory or simulation of our universe.",
              "finite_encoding_cases": count, "bell_states": cases,
              "classical_pure_joint_marginals": classical,
              "same_state_same_mean_energy_different_dynamics": quantum_dynamics,
              "real_quantum_local_tomography_counterexample": {
                  "local_product_basis_differences": local_differences,
                  "global_Pplus_probabilities": global_probabilities,
                  "positivity_check": "Real symmetric, trace 1, rho^2=rho/2 imply eigenvalues 0 or 1/2"},
              "status": "all assertions passed"}
    output = Path(__file__).with_name("structure-witnesses.json")
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(f"PASS: {count} recoded maps; Bell/classical composition and Hamiltonian witnesses. {output}")


if __name__ == "__main__":
    main()
