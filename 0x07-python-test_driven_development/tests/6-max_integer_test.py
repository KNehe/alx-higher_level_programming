#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_4(self):
        self.assertEqual(max_integer([1,2,4,2]), 4)

    def test_max_with_one_item(self):
        self.assertEqual(max_integer([10]), 10)

    def test_max_with_same_items(self):
        self.assertEqual(max_integer([1,1,1,1]), 1)

    def test_negative_and_positive_items(self):
        self.assertEqual(max_integer([-1,4,-3,3]), 4)
    
    def test_negative_items(self):
        self.assertEqual(max_integer([-1,-2,-3]), -1)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_none_list(self):
        self.assertRaises(TypeError, max_integer, None)

    def test_list_with_int_strings(self):
        self.assertEqual(max_integer(["1", "2"]), "2")

    def test_list_with_word_strings(self):
        self.assertEqual(max_integer(["one", "three", "five"]), "three")

    def test_list_with_empty_string(self):
        self.assertEqual(max_integer([""]), "")
