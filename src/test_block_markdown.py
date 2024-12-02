from block_markdown import markdown_to_blocks, block_to_block_type
import unittest

class TestBlockMarkDown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
        blocks = markdown_to_blocks(markdown)
        self.assertEqual(
            blocks,
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
                """* This is the first list item in a list block
* This is a list item
* This is another list item""",
            ],
        )

    def test_block_to_block_type_para(self):
        block_type2 = block_to_block_type("""Hello word
                                          Hahaha""")
        block_type = block_to_block_type("This is paragraph")
        self.assertEqual(
            block_type, "paragraph"
        )
        self.assertEqual(block_type2, "paragraph")

    def test_block_to_block_type_heading(self):
        block_type = block_to_block_type("# Heading1")
        self.assertEqual(block_type, "heading 1")

    def test_block_to_block_type_code(self):
        block_type = block_to_block_type("```print('Hello Word')\nprint()```")
        self.assertEqual(block_type, "code")

    def test_block_to_block_type_quote(self):
        block_type = block_to_block_type(">This is multi\n>line quotes")
        self.assertEqual(block_type, "quote")

    def test_block_to_block_type_ulist(self):
        block_type1 = block_to_block_type("* cat\n* dog\n* penguin")
        block_type2 = block_to_block_type("- cat\n- dog\n- penguin")
        self.assertEqual(block_type1, "unordered list")
        self.assertEqual(block_type2, "unordered list")

    def test_block_to_block_type_olist(self):
        block_type = block_to_block_type("1. cat\n2. dog\n3. pig")
        self.assertEqual(block_type, "ordered list")

if __name__ == "__main__":
    unittest.main()
