# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../../rethon/rethon/'))
sys.path.insert(0, os.path.abspath('../../tau/tau/'))

print('Using the python:', sys.executable)
print ('Using path:', sys.path)
# -- Project information -----------------------------------------------------

project = 'RE Docs'
copyright = '2023, Claus Beisbart, Gregor Betz, Georg Brun, Sebastian Cacean, Andreas Freivogel, Richard Lohse'
author = 'Claus Beisbart, Gregor Betz, Georg Brun, Sebastian Cacean, Andreas Freivogel, Richard Lohse'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# extensions = ['sphinx.ext.autodoc','sphinx.ext.napoleon']
# see https://github.com/agronholm/sphinx-autodoc-typehints

extensions = ['sphinx.ext.autodoc',
              'numpydoc',
              'sphinx_autodoc_typehints',
              'sphinx.ext.napoleon',
              'nbsphinx', # including jupyter notebooks
              ]


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for autodoc ----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#configuration

# Automatically extract typehints when specified and place them in
# descriptions of the relevant function/method.
autodoc_typehints = "description"

# Don't show class signature with the class' name.
autodoc_class_signature = "separated"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = "pydata_sphinx_theme"

html_theme_options = {
  "show_prev_next": False,
  "show_toc_level": 4 # toc-level of the secondary sidbar (the right one)
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

