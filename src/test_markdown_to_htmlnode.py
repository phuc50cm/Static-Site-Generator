import unittest
from markdown_to_htmlnode import (
    text_to_children,
    markdown_to_html_node,
    heading_to_html_node,
    code_to_html_node,
    quote_to_html_node,
    ulist_to_html_node,
    olist_to_html_node,
    para_to_html_node,
)
from htmlnode import LeafNode, HTMLNode

class TestMarkDownToHTMLNode(unittest.TestCase):
    def test_markdown_to_html_node(self):
        markdown = "# Heading\n\nParagraph\n\n>Quote"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(
            html_node.to_html(),
            "<div><h1>Heading</h1><p>Paragraph</p><blockquote>Quote</blockquote></div>"
        )

    def test_markdown_to_html_node_nested(self):
        markdown = "This is paragraph with **bold** and *italic* text\n\nThis is another paragraph"
        html_node = markdown_to_html_node(markdown)
        self.assertEqual(
            html_node.to_html(),
            "<div><p>This is paragraph with <b>bold</b> and <i>italic</i> text</p><p>This is another paragraph</p></div>"
        )

    def test_markdown_to_html_node_full(self):
        markdown = """
# Tolkien Fan Club

**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn't work yet)

> All that is gold does not glitter

## Reasons I like Tolkien

* You can spend years studying the legendarium and still not understand its depths
* It can be enjoyed by children and adults alike
* Disney *didn't ruin it*
* It created an entirely new genre of fantasy

## My favorite characters (in order)

1. Gandalf
2. Bilbo
3. Sam
4. Glorfindel
5. Galadriel
6. Elrond
7. Thorin
8. Sauron
9. Aragorn

Here's what `elflang` looks like (the perfect coding language):

```
func main(){
    fmt.Println("Hello, World!")
}
```
"""
        #html_node = markdown_to_html_node(markdown)
        #self.assertEqual(
        #    html_node.to_html(),
        #    "<div></div>"
        #)

    def test_heading_to_html_node(self):
        block = "# This is heading 1"
        html_node = heading_to_html_node(block)
        self.assertEqual(
            html_node.to_html(),
            "<h1>This is heading 1</h1>"
        )

    def test_code_to_html_node(self):
        block = "```This is code\nAnother code```"
        html_node = code_to_html_node(block)
        self.assertEqual(
            html_node.to_html(),
            "<pre><code>This is code\nAnother code</code></pre>"
        )

    def test_quote_to_html_node(self):
        block = ">This is quote"
        block2 = ">This is quote\n>Another quote"
        html_node = quote_to_html_node(block) 
        html_node2 = quote_to_html_node(block2)
        self.assertEqual(
            html_node.to_html(),
            "<blockquote>This is quote</blockquote>"
        )
        self.assertEqual(
            html_node2.to_html(),
            "<blockquote>This is quote Another quote</blockquote>"
        )

    def test_ulist_to_html_node(self):
        block = "* Item 1\n* Item 2"
        html_node = ulist_to_html_node(block)
        self.assertEqual(
            html_node.to_html(),
            "<ul><li>Item 1</li><li>Item 2</li></ul>"
        )

    def test_olist_to_html_node(self):
        block = "1. Item 1\n2. Item 2"
        html_node = olist_to_html_node(block)
        self.assertEqual(html_node.to_html(),
                         "<ol><li>Item 1</li><li>Item 2</li></ol>")

    def test_para_to_html_node(self):
        block = "This is paragraph"
        html_node = para_to_html_node(block)
        self.assertEqual(html_node.to_html(), "<p>This is paragraph</p>")

    def test_text_to_children(self):
        text = "This is **text** with an *italic* word."
        html_nodes = text_to_children(text)
        self.assertListEqual(
            html_nodes,
            [
                LeafNode(None, "This is "),
                LeafNode("b", "text"),
                LeafNode(None, " with an "),
                LeafNode("i", "italic"),
                LeafNode(None, " word."),
            ]
        )

if __name__ == "__main__":
    unittest.main()
