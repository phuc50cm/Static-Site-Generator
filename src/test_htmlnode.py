import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "This is a link to google", None,
                        {"href": "https://www.google.com"})
        self.assertEqual(
            node.props_to_html(),
            " href=\"https://www.google.com\""
        )

    def test_props_to_html2(self):
        node = HTMLNode("a", "This is a link to google", None,
                        {"href": "https://www.google.com", "target": "_blank"})

        self.assertEqual(
            node.props_to_html(),
            " href=\"https://www.google.com\" target=\"_blank\""
        )

    def test_repr(self):
        node = HTMLNode("a", "This is a link to google", None,
                        {"href": "https://www.google.com"})
        self.assertEqual(
            repr(node),
            "HTMLNode(a, This is a link to google, None,  href=\"https://www.google.com\")"
        )

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(
            node.to_html(),
            "<p>This is a paragraph of text.</p>"
        )

    def test_to_html2(self):
        node = LeafNode(None, "This is a paragraph of text.")
        self.assertEqual(
            node.to_html(),
            "This is a paragraph of text."
        )

    def test_to_html3(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            "<a href=\"https://www.google.com\">Click me!</a>"
        ) 

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>"
        )

    def test_to_html2(self):
        grand_child_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grand_child_node]) 
        node = ParentNode("div", [child_node])
        self.assertEqual(
            node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()
