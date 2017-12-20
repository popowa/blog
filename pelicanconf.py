#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'ayakomuro'
SITENAME = 'popowa'
SITEURL = 'http://blog.popowa.com'

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

MENUITEMS = ( ('Profile', 'http://www.popowa.com'),
            ('Twitter', 'https://twitter.com/ayakomuro'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "pelican-fresh-master"
STATIC_PATHS = ['images']
GOOGLE_ANALYTICS = "UA-845207-15"
TWITTER_USERNAME="ayakomuro"
GOOGLE_CUSTOM_SEARCH = '014316853335343165598:-bgzniyqm3y'
HIDE_CATEGORIES_FROM_MENU = True
TAG_CLOUD_STEPS = False
SHARETHIS_PUB_KEY = "5a2ce781d0739000123acd73"
