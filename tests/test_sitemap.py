import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path
import tempfile


def _build_sitemap(src: str):
    with tempfile.TemporaryDirectory() as out:
        subprocess.run([
            'sphinx-build',
            '-b', 'html',
            src,
            out,
        ], check=True)
        tree = ET.parse(Path(out) / 'sitemap.xml')
        return [loc.text for loc in tree.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]


def test_docs_example():
    expected = [
        'https://example.com/docs/index.html',
        'https://example.com/docs/page1.html',
        'https://example.com/docs/page2.html',
    ]
    assert _build_sitemap('examples/docs') == expected


def test_hello_world_example():
    expected = [
        'https://example.com/_modules/hello_world/hello.html',
        'https://example.com/_modules/hello_world/helpers.html',
        'https://example.com/_modules/index.html',
        'https://example.com/api.html',
        'https://example.com/helpers.html',
        'https://example.com/index.html',
        'https://example.com/pyproject.html',
        'https://example.com/usage.html',
    ]
    assert _build_sitemap('examples/hello_world/docs') == expected


def test_external_links_ignored():
    expected = [
        'https://example.com/index.html',
        'https://example.com/page.html',
    ]
    assert _build_sitemap('examples/external_links/docs') == expected
