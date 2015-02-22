#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Евгений Орлов'
SITENAME = u'Евгений Орлов'
SITESUBTITLE = u'Персональный блог об анализе данных'
SITEURL = 'http://localhost:8000'

# Path to theme
THEME = "pelican-bootstrap3"

PATH = 'content'
DELETE_OUTPUT_DIRECTORY = False

TIMEZONE = 'Europe/Moscow'

DEFAULT_LANG = u'ru'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SITELOGO = 'images/logo.png'
SITELOGO_SIZE = 32
FAVICON = 'images/favicon.png'

# Disqus comments plugin
DISQUS_SITENAME = 'eorlov'
DISQUS_SHORTNAME = 'eo'
DISQUS_DISPLAY_COUNTS = False

DEFAULT_PAGINATION = 5


# Recently active GitHub repos in the sidebar
GITHUB_USER = 'evgenyorlov'
GITHUB_REPO_COUNT = 3
GITHUB_SKIP_FORK = True
GITHUB_SHOW_USER_LINK = True

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)
LINKS = None

# Social widget
#SOCIAL = (('twitter', 'http://twitter.com/evgeny_orlov'),
#          ('github', 'https://github.com/evgenyorlov'),)
SOCIAL = None

# Tags
DISPLAY_TAGS_ON_SIDEBAR = True
TAG_CLOUD_MAX_ITEMS = 10

# Categories
#DISPLAY_CATEGORIES_ON_SIDEBAR = False

# Recent posts
#DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
#RECENT_POST_COUNT = 5

#HIDE_SIDEBAR = False

# Bootstrap theme: http://bootswatch.com/
BOOTSTRAP_THEME = 'flatly'
BOOTSTRAP_NAVBAR_INVERSE = False

# License
CC_LICENSE = "CC-BY"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

