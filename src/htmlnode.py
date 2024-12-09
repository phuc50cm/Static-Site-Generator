class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return ""

        html_attributes = ""
        for attribute in self.props:
            html_attributes += f" {attribute}=\"{self.props[attribute]}\""

        return html_attributes

    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf node must have a value")
        if self.tag is None:
            return self.value

        # Otherwise, render an HTML tag
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, child, props=None):
        super().__init__(tag, None, child, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent node must have a tag")
        if self.children is None:
            raise ValueError("Parent node must have at least one children")

        # Otherwise, return the HTML tag of node and its children
        html_tag = ""
        for child in self.children:
            html_tag += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{html_tag}</{self.tag}>"
