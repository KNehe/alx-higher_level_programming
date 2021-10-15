#!/usr/bin/python3
import unittest
from models.square import Square
import pycodestyle


class TestPycodestyle(unittest.TestCase):
    """
    Tests pycodestyle guidelines for models/square.py
    and tests/test_models/test_rectanlge.py
    """
    def test_style(self):
        """Tests pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(["models/square.py",
                                   "tests/test_models/test_square.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestSquare(unittest.TestCase):
    def test_args(self):
        """
        Should initialize square
        with given values
        """
        sq = Square(1, 2, 3, 4)
        self.assertTrue(sq.width == 1)
        self.assertTrue(sq.height == 1)
        self.assertTrue(sq.x == 2)
        self.assertTrue(sq.y == 3)
        self.assertTrue(sq.id == 4)

    def test_default_params(self):
        """
        Should initialize square
        with default values
        """
        sq = Square(10)
        self.assertTrue(sq.width == 10)
        self.assertTrue(sq.height == 10)
        self.assertTrue(sq.x == 0)
        self.assertTrue(sq.y == 0)
        self.assertTrue(sq.id is not None)

    def test_no_args(self):
        """
        Should raise TypeError
        when no args passed
        """
        with self.assertRaises(TypeError):
            Square()
            Square(None)

    def test_more_args(self):
        """
        Should raise TypeError
        when extra args are passed
        """
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5, 6, 7)

    def test_none_int_args(self):
        """Tests when args are not int"""
        with self.assertRaises(TypeError):
            Square("j")
        with self.assertRaises(TypeError):
            Square(2, 5, "s", 8)
        with self.assertRaises(TypeError):
            Square({'yes': 1})
        with self.assertRaises(TypeError):
            Square(1, "2")

    def test_negative_Args(self):
        """Raise error when args are negative"""
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -9, 6, 7)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 3, -8, 6)

    def test_class(self):
        """Class should be a sqaure"""
        self.assertTrue(Square(6), self.__class__ == Square)

    def test_values(self):
        """
        Test error messages for wrong
        args passed
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("2", 3, 4, 5)
            Square([2, 3], 4, 5, 6)
            Square({2, })
            Square({"sq": 2})
            Square(None)
            Square((3, 2), 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
            Square(-1)
            Square(0, 2, 3, 4)
            Square(-3, 4, 5, 7)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "g", 3, 4)
            Square(2, [4, 3], 5, 5)
            Square(5, (6, 7), 5, 6)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "yes", 54)
            Square(1, 2, {"k": j}, 8)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -2, 3, 4)
            Square(21, -89, 3, 5)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 2, -4, 5)
            Square(56, 98, -100, 99)

    def test_square_area(self):
        """Should return area of the sqaure"""
        self.assertEqual(Square(4).area(), 16)
        self.assertEqual(Square(2, 0, 0, 7).area(), 4)
        self.assertEqual(Square(8, 3, 4, 76).area(), 64)
        self.assertEqual(Square(4, 2, 1).area(), 16)

    def test_str(self):
        """Test implementation of __str__"""
        sq = Square(1, 2, 3, 44)
        sq.size = 50
        self.assertEqual(str(sq), '[Square] (44) 2/3 - 50')

    def test_to_dictionary(self):
        """Should return dict form of square"""
        sq = Square(10, 2, 1, 9)
        sq_dict = sq.to_dictionary()
        sq1 = Square(5)
        sq1.update(**sq_dict)
        self.assertEqual(type(sq_dict), dict)
        self.assertFalse(sq == sq1)
