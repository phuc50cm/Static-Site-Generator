from markdown_to_html import block_to_html_node, text_to_children
from htmlnode import ParentNode, LeafNode
import unittest


class TestMarkDownToHTML(unittest.TestCase):
    def test_block_to_html_node(self):
        block = """I love dog\nI also love her"""
        
    def test_para_to_html_node(self):
        block = "I love dog\nI also love her"


if __name__ == "__main__":
    unittest.main()
