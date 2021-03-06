#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Евгений Орлов'
SITENAME = u'В разработке...'
SITESUBTITLE = u'Персональный блог об анализе данных'
SITEURL = 'http://localhost:8000'

# Path to theme
THEME = "pelican-bootstrap3"

# Bootstrap theme: http://bootswatch.com/
BOOTSTRAP_THEME = 'flatly2'
BOOTSTRAP_NAVBAR_INVERSE = False

# Pygments theme
PYGMENTS_STYLE = 'zenburn'  # monokai zenburn manni

PATH = 'content'
DELETE_OUTPUT_DIRECTORY = False

TIMEZONE = 'Europe/Moscow'

LOCALE = ('rus', 'usa',  # On Windows
	'ru_RU.utf8', 'en_US.utf8',  # On Unix/Linux
)  # Locale which goes first is applied
DEFAULT_LANG = u'ru'


DATE_FORMATS = {
    'en': '%B %d, %Y',
    'ru': '%d.%m.%Y',
}
DEFAULT_DATE_FORMAT = '%d.%m.%Y'
DEFAULT_DATE = 'fs'


NEWEST_FIRST_ARCHIVES = True

ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'
TAGS_URL = 'tags.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SITELOGO = 'images/logo.png'
SITELOGO_SIZE = 32
FAVICON = 'images/favicon.png'
SITETEASER = 'images/teaser.png'

# Disqus comments plugin
DISQUS_SITENAME = 'eorlov'
DISQUS_SHORTNAME = 'eo'
DISQUS_DISPLAY_COUNTS = True

DEFAULT_PAGINATION = 4

#DISPLAY_BREADCRUMBS = False
#DISPLAY_CATEGORY_IN_BREADCRUMBS = True

# Recently active GitHub repos in the sidebar
GITHUB_URL = 'https://github.com/evgenyorlov'
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
DISPLAY_TAGS_INLINE = True
TAG_CLOUD_STEPS = 3
TAG_CLOUD_MAX_ITEMS = 10

# Categories
#DISPLAY_CATEGORIES_ON_SIDEBAR = False
#REVERSE_CATEGORY_ORDER = False

# Recent posts
#DISPLAY_RECENT_POSTS_ON_SIDEBAR = False
#RECENT_POST_COUNT = 5

#HIDE_SIDEBAR = False

# License
CC_LICENSE = "CC-BY"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['extra/robots.txt','extra/CNAME', 'images', ]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/CNAME': {'path': 'CNAME'},
}

# Article list parameters
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_TEASER_IMAGES = True
SHOW_ARTICLE_CATEGORY = False

#### Plugins ####
PLUGIN_PATHS = ["pelican-plugins", ]
PLUGINS = ["sitemap", "summary", "related_posts"]
# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        '{category}': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        '{category}': 'always',
        'indexes': 'hourly',
        'pages': 'monthly'
    }
}
# Related posts
RELATED_POSTS_MAX = 5

#### Google Analytics ####
GOOGLE_ANALYTICS = 'UA-60053622-1'
GOOGLE_ANALYTICS_DOMAIN = 'http://eorlov.com/'

SHARIFF = True
#SHARIFF_BACKEND_URL (see Shariff Backends)
SHARIFF_LANG = "en"
SHARIFF_ORIENTATION = "horizontal"
#SHARIFF_SERVICES = [&quot;facebook&quot;,&quot;googleplus&quot;]
SHARIFF_THEME = "grey"
SHARIFF_TWITTER_VIA = False  # uses TWITTER_USERNAME)