import os
import shutil
from block_markdown import (
    markdown_to_blocks,
    is_heading,
)
from markdown_to_htmlnode import (
    markdown_to_html_node,
)


def main():
    copy_content("static", "public")
    #generate_page("content/index.md", "template.html", "public/index.html")
    generate_pages_recursive("content", "template.html", "public")


def copy_content(src, dst):
    # Test function
    #print(os.path.exists(src))
    #print(os.listdir("."))
    #print(os.path.join(src, "index.html"))
    #print(os.path.isfile("public/index.html"))
    #os.mkdir("test")
    #print(shutil.copy("public/index.html", "src"))
    #shutil.rmtree("test.hello")

    # Check dst exists, if so remove it
    if os.path.exists(dst):
        shutil.rmtree(dst)
        print(f"Remove folder: {dst}")
    os.mkdir(dst)
    print(f"Create new folder: {dst}")

    # Copy files nested
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
            print(f"Copied file: {src_path} to {dst_path}")
        else:
            copy_content(src_path, dst_path)
            print(f"Copied directory: {src_path} to {dst_path}")

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        if is_heading(block):
            sections = block.split(" ", maxsplit=1)
            heading_level = sections[0].count("#")
            if heading_level == 1:
                return sections[1]

    raise Exception("No header to extract")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read file content
    file = open(from_path, "r")
    markdown = file.read()
    file = open(template_path, "r")
    template = file.read()
    file.close()

    html_string = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html_string)

    
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "" and not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    to_file = open(dest_path, "w")
    to_file.write(template)
    print(f"Write template to {dest_path}")
    to_file.close()


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)
        if os.path.isfile(from_path):
            new_dest_path = dest_path.replace(".md", ".html")
            generate_page(from_path, template_path, new_dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)

if __name__ == "__main__":
    main()
