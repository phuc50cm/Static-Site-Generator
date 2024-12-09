import re

# Return list of block in markdown
def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    for i in range(len(blocks)):
        blocks[i] = blocks[i].strip()
    return list(filter(lambda block : block != "", blocks))

# Take single block of markdown and return type of block as string
def block_to_block_type(block):
    if is_heading(block):
        return "heading"
    elif is_code(block):
        return "code"
    elif is_quote_block(block):
        return "quote"
    elif is_ulist(block):
        return "unordered list"
    elif is_olist(block):
        return "ordered list"
    else:
        return "paragraph"

# Check funtions
def is_heading(block):
    heading_pattern = r"^#{1,6} .+"
    if re.match(heading_pattern, block):
        return True
    return False

def is_code(block):
    return block.startswith("```") and block.endswith("```")

def is_quote_block(block):
    lines = block.split("\n")
    for line in lines:
        if not line.startswith(">"):
            return False
    return True

def is_ulist(block):
    lines = block.split("\n")
    for line in lines:
        if not (line.startswith("* ") or line.startswith("- ")):
            return False
    return True

def is_olist(block):
    lines = block.split("\n")
    number = 1
    for line in lines:
        if not line.startswith(f"{number}. "):
            return False
        number += 1
    return True

