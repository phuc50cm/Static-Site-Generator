import unittest
from main import extract_title

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        self.assertEqual(
            extract_title("# Hello"),
            "Hello"
        )

    def test_extract_title_multilines(self):
        self.assertEqual(
            extract_title("# Hello\n\n## Examples"),
            "Hello"
        )
