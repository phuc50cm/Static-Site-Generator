from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
)
from htmlnode import HTMLNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

# Convert full markdown doc to single htmlnode
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)

    return ParentNode("div",children)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    match block_type:
        case "heading":
            return heading_to_html_node(block)
        case "code":
            return code_to_html_node(block)
        case "quote":
            return quote_to_html_node(block)
        case "unordered list":
            return ulist_to_html_node(block)
        case "ordered list":
            return olist_to_html_node(block)
        case "paragraph":
            return para_to_html_node(block)

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))

    return html_nodes
        
def heading_to_html_node(block):
    sections = block.split(" ", maxsplit=1)
    heading_level = sections[0].count("#")
    text = sections[1]
    children = text_to_children(text)
    return ParentNode(f"h{heading_level}", children)

def code_to_html_node(block):
    text = block[3:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip(">"))
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item.split(" ", maxsplit=1)[1]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def para_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)
