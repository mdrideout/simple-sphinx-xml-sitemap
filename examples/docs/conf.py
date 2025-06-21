
project = 'Example'
extensions = ['simple_sphinx_xml_sitemap']
html_baseurl = 'https://example.com/docs/'

# Exclude the virtual environment so Sphinx does not try to parse files inside
# ``.venv`` when building the docs. Without this exclusion Sphinx may pick up
# ``.rst`` files from dependencies which can lead to confusing errors.
exclude_patterns = ['_build', '.venv']

# minimal settings for demonstration
