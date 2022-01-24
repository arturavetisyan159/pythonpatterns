from main import String
import unittest

class TestStringMethods(unittest.TestCase):
    def test_concatenate(self):
        self.assertEqual(String().concatenate("pyt", "hon"), "python")

    def test_make_uppercase(self):
        self.assertEqual(String().make_uppercase("python"), "PYTHON")

    def test_make_lowercase(self):
        self.assertEqual(String().make_lowercase("PYTHON"), "python")

    def test_capitalize(self):
        self.assertEqual(String().capitalize("python"), "Python")

    def test_replace(self):
        self.assertEqual(String().replace("mama myla ramu", "mama", "rama"), "rama myla ramu")

if __name__ == "__main__":
    unittest.main()
