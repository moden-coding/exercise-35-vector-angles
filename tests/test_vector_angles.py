#!/usr/bin/env python3

import unittest
from unittest.mock import patch

import numpy as np

from src.vector_angles import main, vector_angles


class TestVectorAngles(unittest.TestCase):

    def test_worked_example(self):
        A = np.array([[0, 0, 1], [-1, 1, 0]])
        B = np.array([[0, 1, 0], [1, 1, 0]])
        a = vector_angles(A, B)
        np.testing.assert_allclose(
            a, [90, 90],
            err_msg="Incorrect result for vectors %s and %s!" % (A, B))

    def test_main_calls_vector_angles(self):
        with patch("src.vector_angles.vector_angles", wraps=vector_angles) as va:
            main()
        self.assertGreaterEqual(
            va.call_count, 1,
            msg="You should call the vector_angles function from the main "
                "function!")

    def test_identical_vectors_have_zero_angle(self):
        n = 10
        A = np.random.randn(n, 3)
        a = vector_angles(A, A)
        np.testing.assert_allclose(
            a, [0] * 10, atol=1e-04,
            err_msg="Incorrect result for vectors %s and %s!" % (A, A))

    def test_opposite_vectors_have_180_degree_angle(self):
        A = np.array([[1, 0, 0], [0, 2, 0]])
        B = np.array([[-1, 0, 0], [0, -2, 0]])
        a = vector_angles(A, B)
        np.testing.assert_allclose(
            a, [180, 180], atol=1e-04,
            err_msg="Opposite vectors should be 180 degrees apart. Incorrect "
                    "result for vectors %s and %s!" % (A, B))


if __name__ == '__main__':
    unittest.main()
