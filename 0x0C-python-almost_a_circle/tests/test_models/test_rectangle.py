#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
import pycodestyle


class TestPycodeStyle(unittest.TestCase):
    """Pycodestyle tests"""

    def test_style(self):
        """Test files listed below"""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/rectangle.py',
                                   'tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""

    def test_class(self):
        """Object created should be a rectangle"""
        self.assertTrue(Rectangle(2, 4), self.__class__ == Rectangle)

    def test_rectangle_init(self):
        """Test when rectangle is created with default values"""
        r = Rectangle(10, 2)
        self.assertTrue(r.id is not None)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertTrue(r.x == 0)
        self.assertTrue(r.y == 0)

    def test_getter_setter(self):
        """Should get width/height values and set new values"""
        r = Rectangle(13, 22, 0, 0, 12)
        self.assertEqual(r.width, 13)
        self.assertEqual(r.height, 22)
        r.width = 16
        r.height = 8
        self.assertEqual(r.width, 16)
        self.assertEqual(r.height, 8)

    def test_int_type(self):
        """Should raise errors when value is not valid"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("13", 22, 0, 0, 12)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(13, "22", 0, 0, 12)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(13, 22, "0", 0, 12)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(13, 22, 0, "0", 12)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 22, 0, 0, 12)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(13, 0, 0, 0, 12)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(13, 22, -1, 0, 12)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(13, 22, 0, -1, 12)

    def test_access_private_var(self):
        """Should raise error when attempt to private variable is made"""
        with self.assertRaises(AttributeError):
            Rectangle.__width
            Rectangle.__height
            Rectangle.__x
            Rectangle.__y

    def test_no_args(self):
        """When no args are passed"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_more_args(self):
        """Raises error when extra args are passed"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6, 7, 8, 9)

    def test_less_args(self):
        """Should fail with less args passed"""
        with self.assertRaises(TypeError):
            Rectangle(3)

    def test_area(self):
        """Should calculate area of rectangle"""
        r1 = Rectangle(3, 2)
        self.assertTrue(r1.area() == 6)

        r2 = Rectangle(2, 10)
        self.assertTrue(r2.area() == 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertTrue(r3.area() == 56)
