import unittest

import numpy as np

from estimator import EstimatorError, fit_projection, match_scalar, score_heldout
from run_certificates import (
    N_CHANNELS,
    TEST_SEEDS,
    TRAIN_SEEDS,
    coherent_fixture,
    randomized_identity_fixture,
    zero_fixture,
)


class EstimatorContractTests(unittest.TestCase):
    def setUp(self):
        train = coherent_fixture("train", TRAIN_SEEDS, 0, 8)
        self.projection = fit_projection(match_scalar(train, n_channels=N_CHANNELS))

    def test_projection_is_frozen_scalar_shadow_direction(self):
        expected = np.zeros(N_CHANNELS)
        expected[0] = 1 / np.sqrt(2)
        expected[8] = -1 / np.sqrt(2)
        np.testing.assert_allclose(self.projection, expected, atol=1e-12)

    def test_known_answer_orthogonal_set_latch_is_two_channels(self):
        rows = coherent_fixture("positive", TEST_SEEDS, 2, 9)
        result = score_heldout(match_scalar(rows, n_channels=N_CHANNELS), self.projection)
        self.assertAlmostEqual(result["mean"], 2.0, places=12)

    def test_gate_const_is_zero(self):
        rows = zero_fixture("negative", TEST_SEEDS)
        result = score_heldout(match_scalar(rows, n_channels=N_CHANNELS), self.projection)
        self.assertEqual(result["mean"], 0.0)

    def test_identity_randomized_has_churn_but_zero_coherence(self):
        rows = randomized_identity_fixture("random", TEST_SEEDS)
        result = score_heldout(match_scalar(rows, n_channels=N_CHANNELS), self.projection)
        self.assertAlmostEqual(result["mean"], 0.0, places=12)
        self.assertGreater(result["seed_scores"][0]["raw_mean_hamming"], 0.0)

    def test_too_few_pairs_refused(self):
        rows = coherent_fixture("short", (0,), 2, 9)[:6]
        with self.assertRaises(EstimatorError):
            match_scalar(rows, n_channels=N_CHANNELS, min_pairs=4)

    def test_train_and_test_seeds_disjoint(self):
        self.assertTrue(set(TRAIN_SEEDS).isdisjoint(TEST_SEEDS))


if __name__ == "__main__":
    unittest.main()
