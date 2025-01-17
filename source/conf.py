# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
#import os
#import sys
#sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'EGI notebooks'
copyright = '2021, Petr'
author = 'Petr'

# The full version, including alpha/beta/rc tags
release = '1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#import sys, os

#ys.path.append(os.path.abspath('sphinxext'))

extensions = ['myst_nb']

autosectionlabel_prefix_document = True

myst_heading_anchors = 1

myst_enable_extensions = [
    "amsmath",
#    "linkify",
#    "colon_fence",
#    "deflist",
    "dollarmath",
    "html_image",
#    "replacements",
#    "smartquotes",
#    "substitution",
#    "tasklist",
]

#myst_url_schemes = ("http", "https", "mailto")

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

source_suffix = [
    '.rst',
    '.ipynb',
    '.md'
]

suppress_warnings = ["myst.header"]

# -- Options for LaTeX output ---------------------------------------------

latex_engine = 'pdflatex'
latex_elements = {
    'maxlistdepth': '2',
}

latex_toplevel_sectioning = None

latex_documents = [
    ('index', 'main.tex', 'EGI notebooks',
     'Petr Pospíšil', 'howto')
]
