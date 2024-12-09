import unittest
from block_markdown import markdown_to_blocks, block_to_block_type

class TestBlockMarkDown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = "# This is a heading\n\nThis is a paragraph.\n\n*This is the first list item\n*Another list item"
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(
            blocks,
            [
                "# This is a heading",
                "This is a paragraph.",
                "*This is the first list item\n*Another list item"
            ],
        )

    def test_markdown_to_blocks_excessive_newline(self):
        markdown = "# This is heading\n\n\nThis is a para\n\n\nAnother para"
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(
            blocks,
            [
                "# This is heading",
                "This is a para",
                "Another para"
            ],
        )

    def test_markdown_to_blocks_leading_whitespaces(self):
        markdown = " # This is heading  \n\nThis is a para \n\nAnother para "
        blocks = markdown_to_blocks(markdown)
        self.assertListEqual(
            [
                "# This is heading",
                "This is a para",
                "Another para",
            ],
            blocks
        )

    def test_block_type_heading(self):
        block = "# This is heading"
        self.assertEqual(block_to_block_type(block), "heading")

    def test_block_type_para(self):
        block = "#This is heading(fake)"
        self.assertEqual(block_to_block_type(block), "paragraph")

    def test_block_type_code(self):
        block = "```This is code block\nLine 2\nLine3```"
        self.assertEqual(block_to_block_type(block), "code")

    def test_block_type_quote(self):
        block = ">This is quote\n>Another quote"
        block2 = ">This is quote\nHehe"
        self.assertEqual(block_to_block_type(block), "quote")
        self.assertNotEqual(block_to_block_type(block2), "quote") 

    def test_block_type_ulist(self):
        block = "* Element 1\n* Element 2\n* Element 3"
        block2 = "* Element 1\n- Element 2\n* Element 3"
        block3 = "*Element 1\n-Element 2\n* Element 3"
        block4 = "- Element 1\n- Element 2\n- Element 3"
        self.assertEqual(block_to_block_type(block), "unordered list")
        self.assertEqual(block_to_block_type(block2), "unordered list")
        self.assertNotEqual(block_to_block_type(block3), "unordered list")
        self.assertEqual(block_to_block_type(block4), "unordered list")

    def test_block_type_olist(self):
        block = "1. Item 1\n2. Item 2\n3. Item 3" 
        block2 = "1.Item 1\n2. Item 2\n3. Item 3" 
        block3 = "1.Item 1\n4. Item 2\n3. Item 3" 
        self.assertEqual(block_to_block_type(block), "ordered list")
        self.assertNotEqual(block_to_block_type(block2), "ordered list")
        self.assertNotEqual(block_to_block_type(block3), "ordered list")

if __name__ == "__main__":
    unittest.main()
