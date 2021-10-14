#!/usr/bin/python3
import unittest
from models.base import Base
import pycodestyle


class TestBase(unittest.TestCase):
    """Tests fro models/base.py"""

    def test_param_is_none(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_param_is_given(self):
        b2 = Base(2)
        self.assertEqual(b2.id, 2)

    def test_param_is_none_with_2_objects(self):
        """Create more two objects without passind id"""
        b3 = Base()
        self.assertEqual(b3.id, 2)
        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_invalid_args(self):
        """More than one arg given"""
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_private_var_access(self):
        """Should not access private class variable"""
        with self.assertRaises(AttributeError):
            Base.__nb_objects

    def test_var_not_exist(self):
        """Should not find a variable which doesn't exist"""
        with self.assertRaises(AttributeError):
            Base._nb_objects


class TestPycodeStyle(unittest.TestCase):
    """Test PycodeStyle on models/base.py and tests/tests/test_base.py"""

    def test_pycodestyle(self):
        style = pycodestyle.StyleGuide(quiet=True)
        files = ["models/base.py", "tests/test_models/test_base.py"]
        result = style.check_files(files)
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
