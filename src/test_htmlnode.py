import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextType, TextNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        htmlnode = HTMLNode("p", "This is link")
        
        self.assertEqual("", htmlnode.props_to_html())

    def test_props_to_html2(self):
        htmlnode = HTMLNode("a", "This is link", props={
    "href": "https://www.google.com", 
    "target": "_blank",
})
        self.assertEqual(' href="https://www.google.com" target="_blank"', htmlnode.props_to_html())

    def test_props_to_html3(self):
        htmlnode = HTMLNode("p", "Hello", props={"href": "https://www.pornhub.com"})
        self.assertEqual(' href="https://www.pornhub.com"', htmlnode.props_to_html())

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    def test_html_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_leaf_values(self):
        leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"}) 
        self.assertEqual(leaf.tag, "a")
        self.assertEqual(leaf.value, "Click me!")
        self.assertEqual(leaf.props, {"href": "https://www.google.com"})

    def test_to_html(self):
        leaf1 = LeafNode("p", "This is a paragraph of text.")
        leaf2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        parent1 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        

        self.assertEqual(leaf1.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(leaf2.to_html(), '<a href="https://www.google.com">Click me!</a>')

        self.assertEqual(parent1.to_html(), '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>')

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_text_node_to_html_node(self):
        text_node = TextNode("Hello world Hahaha", TextType.NORMAL_TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(
            html_node.value,
            "Hello world Hahaha"
        )


if __name__ == "__main__":
    unittest.main()
