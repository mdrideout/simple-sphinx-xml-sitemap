import os
import sys

# Include the project package and extension
sys.path.insert(0, os.path.abspath('..'))  # hello_world package
sys.path.insert(0, os.path.abspath('../../../'))  # extension root

project = 'Hello World Example'
extensions = ['simple_sphinx_xml_sitemap']
html_baseurl = 'https://example.com/hello/'

# minimal settings for demonstration
