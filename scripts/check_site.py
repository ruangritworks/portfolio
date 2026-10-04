"""Validate the static site and its deployment artifact without dependencies."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.links = []
        self.h1_count = 0
        self.feed(source)

    def handle_starttag(self, tag, attributes):
        attributes = dict(attributes)
        if "id" in attributes:
            self.ids.append(attributes["id"])
        if tag == "h1":
            self.h1_count += 1
        for attribute in ("href", "src"):
            if attribute in attributes:
                self.links.append(attributes[attribute])


def check(root):
    errors = []
    pages = {}
    required = ("index.html", "styles.css", "favicon.svg", "resume.html",
                "404.html", "robots.txt", "sitemap.xml", ".nojekyll",
                "files/Ruangrit-Srimuang-Resume.pdf")
    for name in required:
        if not (root / name).is_file():
            errors.append(f"Missing production file: {name}")
    for name in ("index.html", "resume.html", "404.html"):
        path = root / name
        if not path.is_file():
            continue
        source = path.read_text(encoding="utf-8")
        if "{{" in source or "{%" in source:
            errors.append(f"{name}: unrendered template syntax")
        page = pages[name] = Page(source)
        if page.h1_count != 1:
            errors.append(f"{name}: expected one main heading")
        for identifier, count in Counter(page.ids).items():
            if count > 1:
                errors.append(f"{name}: duplicate id {identifier}")
    for name, page in pages.items():
        for link in page.links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc:
                continue
            if parsed.path.startswith("/"):
                errors.append(f"{name}: root-relative URL breaks project hosting: {link}")
                continue
            target = unquote(parsed.path) or name
            if not (root / target).is_file():
                errors.append(f"{name}: missing local target {link}")
            if parsed.fragment and target in pages:
                if unquote(parsed.fragment) not in pages[target].ids:
                    errors.append(f"{name}: missing anchor {link}")
    pdf = root / "files/Ruangrit-Srimuang-Resume.pdf"
    if pdf.is_file():
        with pdf.open("rb") as stream:
            if stream.read(5) != b"%PDF-":
                errors.append("Resume download is not a PDF")
    for name in ("favicon.svg", "sitemap.xml"):
        if (root / name).is_file():
            try:
                ET.parse(root / name)
            except ET.ParseError as error:
                errors.append(f"{name}: invalid XML: {error}")
    if root.name == "_site":
        expected = set(required)
        actual = {str(path.relative_to(root)).replace("\\", "/")
                  for path in root.rglob("*") if path.is_file()}
        if actual != expected:
            errors.append(f"Unexpected deployment files: {sorted(actual - expected)}")
    if errors:
        print("\n".join(errors))
        return 1
    print(f"PASS: {len(pages)} pages; local links, anchors, PDF, XML, and deployment assets checked.")
    return 0


if __name__ == "__main__":
    sys.exit(check(Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]))
