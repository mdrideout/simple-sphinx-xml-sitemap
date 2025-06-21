# Simple Sphinx XML Sitemap Extension

This is a simpler XML sitemap generator extension for Sphinx documentation. It does not support internationalization or multiple languages.

## Getting Started:

TODO: UV install, PIP install, Poetry install instructions

TODO: adding to pyproject.toml dev dependencies

TODO: Adding to sphinx `conf.py` file

```python
extensions = [
    # Other extensions
    "simple-sphinx-xml-sitemap",  # This extension
]
```

TODO: Using with standard `sphinx-build` commands

```bash
# Example of use here
$ command
```

### Deployment Builds:

TODO: adding to deployment requirements.txt (link to example) for cloudflare pages / static site builder hosts.

### Why?

The default behavior of search engines like Google is to crawl all pages of the sphinx documentation, including files that do not make sense to crawl.

Without an XML Sitemap, it's hard to tell Google which pages are most important and relevant, because there is duplicate content on `_sources/` and `_modules/` pages.

### How

This Sphinx Documentation XML Sitemap generator generates a sitemap based on your actual navigable content pages, and a couple other standard critical Sphinx documentation pages.

