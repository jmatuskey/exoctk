# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst
#
# Astropy documentation build configuration file.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this file.
#
# All configuration values have a default. Some values are defined in
# the global Astropy configuration which is loaded here before anything else.
# See astropy.sphinx.conf for which values are set there.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('..'))
# IMPORTANT: the above commented section was generated by sphinx-quickstart, but
# is *NOT* appropriate for astropy or Astropy affiliated packages. It is left
# commented out with this explanation to make it clear why this should not be
# done. If the sys.path entry above is added, when the astropy.sphinx.conf
# import occurs, it will import the *source* version of astropy instead of the
# version installed (if invoked as "make html" or directly with sphinx), or the
# version in the build directory (if "python setup.py build_sphinx" is used).
# Thus, any C-extensions that are needed to build the documentation will *not*
# be accessible, and the documentation will not build correctly.

import datetime
import os
import sys
import ast
import textwrap

try:
    import sphinx_astropy
except ImportError:
    # Building from inside the docs/ directory?
    if os.path.basename(os.getcwd()) == 'docs':
        a_h_path = os.path.abspath(os.path.join('..', 'sphinx_astropy'))
        if os.path.isdir(a_h_path):
            sys.path.insert(1, a_h_path)

# Load all of the global Astropy configuration
from sphinx_astropy.conf import *

# Create a mock to allow us access to the setup variables:
def parse_setup(setup_filename):
    """Parse setup.py and return args and keywords args to its setup
    function call

    """
    mock_setup = textwrap.dedent('''\
    def setup(*args, **kwargs):
        __setup_calls__.append((args, kwargs))
    ''')
    parsed_mock_setup = ast.parse(mock_setup, filename=setup_filename)
    with open(setup_filename, 'rt') as setup_file:
        parsed = ast.parse(setup_file.read())
        for index, node in enumerate(parsed.body[:]):
            if (
                not isinstance(node, ast.Expr) or
                not isinstance(node.value, ast.Call) or
                node.value.func.id != 'setup'
            ):
                continue
            parsed.body[index:index] = parsed_mock_setup.body
            break

    fixed = ast.fix_missing_locations(parsed)
    codeobj = compile(fixed, setup_filename, 'exec')
    local_vars = {}
    global_vars = {'__setup_calls__': []}
    exec(codeobj, global_vars, local_vars)
    return global_vars['__setup_calls__'][0]


setup_info = parse_setup('../setup.py')[1]
setup_py = dict(setup_info)

# -- General configuration ----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.2'

# To perform a Sphinx version check that needs to be more specific than
# major.minor, call `check_sphinx_version("x.y.z")` here.
# check_sphinx_version("1.2.1")

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns.append('_templates')

# This is added to the end of RST files - a good place to put substitutions to
# be used globally.
rst_epilog += """
"""

# -- Project information ------------------------------------------------------

# This does not *have* to match the package name, but typically does
project = setup_py['name']
author = setup_py['author']
copyright = '{0}, {1}'.format(
    datetime.datetime.now().year, setup_py['author'])

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

#__import__(setup_py['name'])
#package = sys.modules[setup_py['name']]
package = setup_py['name']

# The short X.Y version.
version = setup_py['version']
# The full version, including alpha/beta/rc tags.
#release = package.__version__


# -- Options for HTML output --------------------------------------------------

# A NOTE ON HTML THEMES
# The global astropy configuration uses a custom theme, 'bootstrap-astropy',
# which is installed along with astropy. A different theme can be used or
# the options for this theme can be modified by overriding some of the
# variables set in the global configuration. The variables set in the
# global configuration are listed below, commented out.


# Please update these texts to match the name of your package.
html_theme_options = {
    'logotext1': 'Exo',  # white,  semi-bold
    'logotext2': 'CTK',  # orange, light
    'logotext3': ':docs'   # white,  light
    }

# Add any paths that contain custom themes here, relative to this directory.
# To use a different custom theme, add the directory containing the theme.
#html_theme_path = []

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes. To override the custom theme, set this to the
# name of a builtin theme or the name of a custom theme in html_theme_path.
#html_theme = None

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = ''

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = ''

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = '{0} v{1}'.format(project, version)

# Output file base name for HTML help builder.
htmlhelp_basename = project + 'doc'


# -- Options for LaTeX output -------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [('index', project + '.tex', project + u' Documentation',
                    author, 'manual')]


# -- Options for manual page output -------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [('index', project.lower(), project + u' Documentation',
              [author], 1)]


# -- Options for the edit_on_github extension ---------------------------------

#if eval(setup_py.get('edit_on_github')):
#    extensions += ['sphinx_astropy.ext.edit_on_github']

#    versionmod = __import__(setup_py['name'] + '.version')
#    edit_on_github_project = setup_py['url']
    #if versionmod.version.release:
     #   edit_on_github_branch = "v" + versionmod.version.version
    #else:
    #    edit_on_github_branch = "master"

#    edit_on_github_source_root = ""
#    edit_on_github_doc_root = "docs"

# -- Resolving issue number to links in changelog -----------------------------
github_issues_url = '{0}'.format(setup_py['url'])

# from mock import Mock as MagicMock
#
# class Mock(MagicMock):
#     @classmethod
#     def __getattr__(cls, name):
#             return MagicMock()
#
# MOCK_MODULES = ['scipy','scipy.optimize','scipy.interpolate']
# sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)
