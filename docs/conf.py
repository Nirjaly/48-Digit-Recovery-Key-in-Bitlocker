project = '48-digit-recovery-key-in-bitlocker'
author = '48-digit-recovery-key-in-bitlocker'
release = '1.0'

# Extensions
extensions = [
    'sphinx_sitemap',
]

# Paths
templates_path = ['_templates']
exclude_patterns = []

# Theme
html_theme = 'alabaster'
html_static_path = ['_static']

# Custom JS & Favicon
html_js_files = ['chatbot.js']  # chatbot widget
html_favicon = '_static/favicon.png'

# Bing search verification
html_context = {
    'bing_verification_code': 'E06B837D01BB33B5FE05F701D0E993EE'
}

# Base URL for sitemap
html_baseurl = 'https://48digitrecoverykeyinbitlocker.readthedocs.io/en/latest/'
