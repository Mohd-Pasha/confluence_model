import os
import sys

sys.path.insert(0, os.path.abspath('.'))




project = 'How to include md files'
copyright = '2024, TTL'
author = 'TTL'
release = '1.0.03'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
     'myst_parser', 
    
    'sphinxcontrib.confluencebuilder',
    'custom_directive',
    'custom1',
    'custom2',
    'custom3',
    'custom4',
    'custom5',
    'custom7',
    'comment',
    'excerpt',
    'excerpt_include',
    'exceprt1',
    'link',
    'excerpt_new',
    'table'
    
    ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']



# Confluence configuration
confluence_publish = True
confluence_space_key = 'ESDF1'
confluence_server_url = 'https://armanpasha0.atlassian.net/wiki/'
# confluence_server_user = 
# confluence_server_pass = ' # Preferably, use environment variables for security
# confluence_parent_page = 'Sofware Factory' 

confluence_permit_raw_html=True
confluence_html_macro='html'
# confluence_version_comment='Automatically genrerated.'



