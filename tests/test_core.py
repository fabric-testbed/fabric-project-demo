"""Tests for fabric_demo."""

import unittest

from fabric_demo.core import greet, add
from fabric_demo.utils import slugify, truncate


class TestCore(unittest.TestCase):
    def test_greet(self):
        result = greet("World")
        self.assertEqual(result, "Hello, World! Welcome to Fabric Demo.")

    def test_greet_empty(self):
        result = greet("")
        self.assertEqual(result, "Hello, ! Welcome to Fabric Demo.")

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_floats(self):
        self.assertAlmostEqual(add(0.1, 0.2), 0.3, places=10)


class TestUtils(unittest.TestCase):
    def test_slugify(self):
        self.assertEqual(slugify("Hello World"), "hello-world")

    def test_slugify_special_chars(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_slugify_multiple_spaces(self):
        self.assertEqual(slugify("hello   world"), "hello-world")

    def test_truncate_short(self):
        self.assertEqual(truncate("hello", 10), "hello")

    def test_truncate_long(self):
        self.assertEqual(truncate("hello world", 8), "hello...")

    def test_truncate_custom_suffix(self):
        self.assertEqual(truncate("hello world", 9, "~"), "hello wo~")


if __name__ == "__main__":
    unittest.main()
