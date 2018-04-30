import unittest
from src.utils import math_util


class TestMathUtil(unittest.TestCase):
    # assert equals
    def test_sum(self):
        self.assertEquals(5, math_util.sum_int(3, 2))

    # assert raise error
    def test_sum_with_invalid_arg(self):
        with self.assertRaises(RuntimeError):
            math_util.sum_int("123", 2)
