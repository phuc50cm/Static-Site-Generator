import functools
import re

# Check function for block
def all_line_startswith(lines, prefix):
    for line in lines:
        if not line.startswith(prefix):
            return False
    return True

def is_ordered_list(lines):
    number = 1
    for line in lines:
        if not line.startswith(f"{number}. "):
            return False
        number += 1
    return True

def get_heading_level(text):
    prefix = text.split(" ", maxsplit=1)[0]
    return prefix.count("#")

def markdown_to_blocks(markdown):
    blocks = list(map(lambda x : x.strip(), markdown.split("\n\n")))
    return blocks

def block_to_block_type(block):
    lines = block.split("\n")

    if re.match(r"^#{1,6} ", lines[0]):
        return f"heading {get_heading_level(lines[0])}"
    
    if lines[0].startswith("```") and lines[len(lines) - 1].endswith("```"):
        return "code"

    if all_line_startswith(lines, ">"):
        return "quote"

    if all_line_startswith(lines, "* ") or all_line_startswith(lines, "- "):
        return "unordered list"

    if is_ordered_list(lines):
        return "ordered list"

    return "paragraph"

