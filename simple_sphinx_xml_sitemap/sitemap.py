"""Core sitemap generation logic."""

from __future__ import annotations

import os
from typing import List
from urllib.parse import urljoin
from xml.etree import ElementTree as ET

from sphinx import addnodes
from sphinx.application import Sphinx
from sphinx.util import logging

logger = logging.getLogger(__name__)


def _collect_nav_docnames(env) -> List[str]:
    """Return a list of document names reachable via toctrees."""

    def is_hidden(name: str) -> bool:
        """Return ``True`` if ``name`` includes a hidden path component."""
        return any(part.startswith('.') for part in name.split('/'))

    docnames = set(env.tocs.keys())
    for doctree in env.tocs.values():
        for node in doctree.traverse(addnodes.toctree):
            for _, docname in node.get('entries', []):
                if docname:
                    docnames.add(docname)

    visible = [d for d in docnames if not is_hidden(d)]
    return sorted(visible)


def _write_sitemap(app: Sphinx, docnames: List[str]) -> None:
    builder = app.builder
    base_url = app.config.html_baseurl
    urls = []
    for docname in docnames:
        target = builder.get_target_uri(docname)
        if target.startswith('.') or '/.' in target:
            continue
        urls.append(urljoin(base_url, target))

    root = ET.Element('urlset', xmlns='http://www.sitemaps.org/schemas/sitemap/0.9')
    for url in urls:
        url_elem = ET.SubElement(root, 'url')
        loc_elem = ET.SubElement(url_elem, 'loc')
        loc_elem.text = url

    tree = ET.ElementTree(root)
    output_path = os.path.join(builder.outdir, app.config.xml_sitemap_filename)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    tree.write(output_path, encoding='utf-8', xml_declaration=True)
    logger.info('sitemap: wrote %s with %d entries', app.config.xml_sitemap_filename, len(urls))


def build_sitemap(app: Sphinx, exception: Exception | None) -> None:
    if exception is not None:
        return
    if app.builder.name != 'html':
        logger.info('sitemap: builder is not html, skipping')
        return
    base_url = app.config.html_baseurl
    if not base_url:
        logger.warning('sitemap: html_baseurl not set, skipping sitemap generation')
        return

    docnames = _collect_nav_docnames(app.env)
    _write_sitemap(app, docnames)


def setup(app: Sphinx):
    app.add_config_value('xml_sitemap_filename', 'sitemap.xml', 'html')
    app.connect('build-finished', build_sitemap)
    return {
        'version': '0.1.0',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
