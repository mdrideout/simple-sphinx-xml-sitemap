# Simple Sphinx XML Sitemap Extension

This project provides a minimal Sphinx extension that generates an XML sitemap
for your documentation.  The extension inspects the navigation structure of your
project and writes a `sitemap.xml` file after the HTML build step completes.

The extension does not support internationalisation or multiple languages, but
it is suitable for most single language documentation sites.

## Installation

Install from PyPI using `pip`:

```bash
pip install simple-sphinx-xml-sitemap
```

Alternatively add it to your `pyproject.toml` or `requirements.txt` file.

## Usage

Add the extension to the `extensions` list in your Sphinx `conf.py` file and
set `html_baseurl` to the public URL where the documentation will be hosted.

```python
extensions = [
    # other extensions
    'simple_sphinx_xml_sitemap',
]

html_baseurl = 'https://example.com/docs/'
```

Build your documentation as normal:

```bash
sphinx-build -b html docs docs/_build
```

After the build completes a `sitemap.xml` file will be present in the output
folder.

## Example

An example project is provided under `examples/docs`.  Change to that directory
and run `sphinx-build` to see the extension in action.

```bash
cd examples/docs
sphinx-build -b html . _build
```

The generated site will contain `sitemap.xml` alongside the HTML output.

## Why

Search engines often crawl every file of a Sphinx build, including sources and
module documentation pages that may not be useful.  Providing an XML sitemap
allows you to indicate which pages are important and helps search engines index
your documentation correctly.
