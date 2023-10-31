#!/usr/bin/python3
"""Unittest for max_integer function
"""
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_empty_list(self):
        result = max_integer([])
        self.assertIsNone(result)

    def test_positive_numbers(self):
        result = max_integer([1, 3, 2, 4, 5])
        self.assertEqual(result, 5)

    def test_negative_numbers(self):
        result = max_integer([-1, -3, -2, -4, -5])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        result = max_integer([1, -3, 2, -4, 5])
        self.assertEqual(result, 5)

    def test_duplicate_max(self):
        result = max_integer([5, 5, 5, 5, 5])
        self.assertEqual(result, 5)

    def test_single_element_list(self):
        result = max_integer([7])
        self.assertEqual(result, 7)


if __name__ == "__main__":
    unittest.main()
