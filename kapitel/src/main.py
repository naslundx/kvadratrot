import os
import sys
import argparse
import json
import re
from pathlib import Path
from datetime import datetime

import markdown
from jinja2 import Template
from bs4 import BeautifulSoup, NavigableString

MARKDOWN_EXTENSIONS = [
    "extra", "md_in_html", "codehilite", "toc", "fenced_code", "attr_list", "smarty"
]

def convert_markdown_to_html(md_path, template_str, dictionary, metadata):
    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    raw_html = markdown.markdown(md_content, extensions=MARKDOWN_EXTENSIONS)
    processed_html = apply_post_processing(raw_html, dictionary)
    chapter_metadata = next(x for x in metadata if x["filename"] in md_path)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    template = Template(template_str)
    return template.render(
        CONTENT=processed_html,
        TITLE=chapter_metadata["title"],
        SUBTITLE=chapter_metadata["subtitle"],
        PAGENAME=chapter_metadata["pagename"],
        TIMESTAMP=timestamp,
    )

def apply_post_processing(html, dictionary):
    soup = BeautifulSoup(html, "html.parser")

    terms = [(entry["term"], entry["link"]) for entry in dictionary]
    term_pattern = re.compile(r'\b(' + '|'.join(re.escape(term) for term, _ in terms) + r')\b')

    for tag in soup.find_all(["p", "li", "blockquote"]):
        for child in tag.children:
            if isinstance(child, NavigableString):
                new_content = term_pattern.sub(lambda m: create_link_html(m.group(0), terms), str(child))
                child.replace_with(BeautifulSoup(new_content, "html.parser"))

    for img in soup.find_all("img"):
        wrapper = soup.new_tag("div", **{"class": "article-img"})
        img.replace_with(wrapper)
        wrapper.append(img)

    return str(soup)

def create_link_html(matched_term, terms):
    for term, link in terms:
        if matched_term == term:
            return f'<a href="{link}" class="dictionary">{term}</a>'
    return matched_term

def load_template(template_path="template.html"):
    if not os.path.exists(template_path):
        sys.exit(f"Template file '{template_path}' not found.")
    with open(template_path, "r", encoding="utf-8") as f:
        return f.read()

def load_dictionary(dictionary_path):
    if not dictionary_path or not os.path.exists(dictionary_path):
        return []
    with open(dictionary_path, "r", encoding="utf-8") as f:
        dictionary = json.load(f)
    dictionary = [element for element in dictionary if element["term"] != ""]
    return dictionary

def load_metadata(metadata_path):
    if not metadata_path or not os.path.exists(metadata_path):
        return []
    with open(metadata_path, "r", encoding="utf-8") as f:
        metadata = json.load(f)
    return metadata

def write_html(output_path, html_content):
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

def process_path(input_path):
    if os.path.isfile(input_path) and input_path.endswith(".md"):
        return [input_path]
    elif os.path.isdir(input_path):
        return [str(p) for p in Path(input_path).rglob("*.md")]
    else:
        sys.exit("Provided path is neither a markdown file nor a directory.")

def main():
    parser = argparse.ArgumentParser(description="Convert Markdown files to HTML with templating and dictionary linking.")
    parser.add_argument("input", help="Markdown file or folder")
    parser.add_argument("--template", default="template.html", help="HTML template with {{ CONTENT }}")
    parser.add_argument("--dictionary", default="dictionary.json", help="JSON file defining dictionary terms and links")
    parser.add_argument("--metadata", default="metadata.json", help="JSON file defining chapter metadata")
    parser.add_argument("--output", default="output", help="Directory for output HTML files")
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)
    template_str = load_template(args.template)
    dictionary = load_dictionary(args.dictionary)
    metadata = load_metadata(args.metadata)
    md_files = process_path(args.input)

    for md_file in md_files:
        html_content = convert_markdown_to_html(md_file, template_str, dictionary, metadata)
        out_file = os.path.join(args.output, Path(md_file).stem + ".html")
        write_html(out_file, html_content)
        print(f"Converted {md_file} → {out_file}")

if __name__ == "__main__":
    main()
