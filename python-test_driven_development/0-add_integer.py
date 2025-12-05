#!/usr/bin/python3
"""Unittest for add_integer([..])
"""
import unittest
add_integer = __import__('0-add_integer').add_integer


class TestAddInteger(unittest.TestCase):
    """tests for add_integer"""

    def test_add_positive_integers(self):
        """tests adding two positive integers"""
        self.assertEqual(add_integer(1, 2), 3)

    def test_add_negative_integers(self):
        """tests adding negative integers"""
        self.assertEqual(add_integer(100, -2), 98)

    def test_default_parameter(self):
        """tests default parameter b=98"""
        self.assertEqual(add_integer(2), 100)

    def test_float_conversion(self):
        """tests float to int conversion"""
        self.assertEqual(add_integer(100.3, -2), 98)

    def test_both_floats(self):
        """tests two float parameters"""
        self.assertEqual(add_integer(-100.5, -10.8), -110)

    def test_default_float(self):
        """tests float with default parameter"""
        self.assertEqual(add_integer(1500.5), 1598)

    def test_invalid_first_arg_string(self):
        """tests TypeError when a is string"""
        with self.assertRaises(TypeError) as context:
            add_integer("holberton", "school")
        self.assertEqual(str(context.exception), "a must be an integer")

    def test_invalid_second_arg_string(self):
        """tests TypeError when b is string"""
        with self.assertRaises(TypeError) as context:
            add_integer(4, "School")
        self.assertEqual(str(context.exception), "b must be an integer")

    def test_invalid_first_arg_none(self):
        """tests TypeError when a is None"""
        with self.assertRaises(TypeError) as context:
            add_integer(None)
        self.assertEqual(str(context.exception), "a must be an integer")

    def test_invalid_nan(self):
        """tests ValueError when a is NaN"""
        with self.assertRaises(ValueError):
            add_integer(float('NaN'))

    def test_zero_values(self):
        """tests adding zeros"""
        self.assertEqual(add_integer(0, 0), 0)

    def test_large_integers(self):
        """tests large integer values"""
        self.assertEqual(add_integer(999999, 1), 1000000)


if __name__ == '__main__':
    unittest.main()