import os
import sys

# Include the project package and extension
sys.path.insert(0, os.path.abspath('..'))  # hello_world package
sys.path.insert(0, os.path.abspath('../../../'))  # extension root

project = 'Hello World Example'

extensions = [
    'simple_sphinx_xml_sitemap',
    'sphinx.ext.autodoc',  # Core Sphinx library for auto html doc generation
    'sphinx.ext.napoleon',  # Support for NumPy and Google style docstrings
    'sphinx.ext.viewcode',  # Add links to highlighted source code
    'sphinx.ext.intersphinx',  # Link to other project's documentation (see mapping below)
    'sphinx.ext.doctest',  # Test code examples in docstrings
    'sphinx.ext.todo',  # Support for TODO items
    'sphinx.ext.coverage',  # Check documentation coverage
    'sphinx.ext.ifconfig',  # Conditional content based on configuration
]

html_baseurl = 'https://example.com/'

# minimal settings for demonstration
