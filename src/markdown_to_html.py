from block_markdown import markdown_to_blocks, block_to_block_type, get_heading_level
from htmlnode import HTMLNode, ParentNode, text_node_to_html_node
from inline_markdown import text_to_textnodes

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        children.append(text_node_to_html_node(text_node))
    return children

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        html_node = block_to_html_node(block)
        block_nodes.append(html_node)

    return ParentNode("div", block_nodes, None)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type.startswith("heading"):
        return heading_to_html_node(block)
    if block_type == "code":
        return code_to_html_node(block)
    if block_type == "quote":
        return quote_to_html_node(block)
    if block_type == "unordered list":
        return ul_to_html_node(block)
    if block_type == "ordered list":
        return ol_to_html_node(block)
    if block_type == "paragraph":
        return paragraph_to_html_node(block)
    raise ValueError("Invalid Block Type")

def heading_to_html_node(block):
    heading_level = get_heading_level(block)
    text = block[heading_level + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{heading_level}", children)

def code_to_html_node(block):
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)    

def ul_to_html_node(block):
    items = block.split("\n") 
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def ol_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

