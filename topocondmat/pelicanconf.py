#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'TU Delft and course contributors'
SITENAME = 'Topology in Condensed Matter'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('This course on edX', 'http://tiny.cc/topocm'),
         ('Course chat', 'https://meso.tnw.tudelft.nl/topocondmat'),
         ('Source code', 'https://github.com/topocm/topocm_content'),)


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']
THEME = "themes/pelican-bootstrap3"
# THEME = "themes/notmyidea"
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
BOOTSTRAP_FLUID = True
SHOW_DATE_MODIFIED = False
SHOW_ARTICLE_INFO = False
SHOW_TITLE_HEADER = False

PIWIK_URL = 'piwik.kwant-project.org'
# PIWIK_SSL_URL
PIWIK_SITE_ID = 4
