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

Build your documentation as normal.  The `sphinx-build` command becomes
available after installing the project's dependencies (for example with
`uv`):

```bash
sphinx-build -b html docs docs/_build
```

After the build completes a `sitemap.xml` file will be present in the output
folder.

## Examples

The `examples/` directory contains small projects showing different ways to use
the extension.

### `docs`

This directory contains only a Sphinx project.  To build it run:

```bash
cd examples/docs
uv venv
source .venv/bin/activate
uv pip install -e ../..
sphinx-build -b html . _build
```

### `hello_world`

This example is a tiny Python package with a documentation folder and its own
`pyproject.toml`.  Build the docs and install the package in editable mode:

```bash
cd examples/hello_world
uv venv
source .venv/bin/activate
uv pip install -e .
uv pip install -e ../..
sphinx-build -b html docs docs/_build
```

Both examples will produce a `sitemap.xml` alongside the HTML output.

## Why

Search engines often crawl every file of a Sphinx build, including sources and
module documentation pages that may not be useful.  Providing an XML sitemap
allows you to indicate which pages are important and helps search engines index
your documentation correctly.
