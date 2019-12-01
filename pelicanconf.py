#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'ayakomuro'
SITENAME = 'popowa'
SITEURL = 'http://blog.popowa.com'
#SITEURL = 'http://localhost:8000'

PATH = 'content'
ARTICLE_PATHS = ['blog', 'workspace']

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Twitter', 'https://twitter.com/ayakomuro'),
#         ('popowa', 'http://www.popowa.com'),)

# Social widget
#SOCIAL = (('Twitter', 'https://twitter.com/ayakomuro'),
#         ('popowa', 'http://www.popowa.com'),)

MENUITEMS = (('TOP', 'http://blog.popowa.com'),
            ('About Aya', 'http://www.popowa.com'),
            ('Twitter', 'https://twitter.com/ayakomuro'),
            ('Github', 'https://github.com/popowa'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "pelican-fresh-master"
STATIC_PATHS = ['images']
GOOGLE_ANALYTICS = "UA-845207-15"
TWITTER_USERNAME="ayakomuro"
GOOGLE_CUSTOM_SEARCH = '014316853335343165598:-bgzniyqm3y'
HIDE_CATEGORIES_FROM_MENU = True
TAG_CLOUD_STEPS = True
SHARETHIS_PUB_KEY = "5a2ce781d0739000123acd73"

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['pelican-toc', 'tag_cloud']
