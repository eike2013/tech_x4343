#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Eike Grundkoetter'
SITENAME = u'tech.x4343'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'de'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Fefe', 'http://blog.fefe.de/'),)

# Social widget
SOCIAL = (('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Use Typogrify Library
#TYPOGRIFY = True

# Plugins
# Where to look for plugins
PLUGIN_PATH = '../pelican-plugins'
# Which plugins to enable
PLUGINS = ['better_figures_and_images']
# Setting for the better_figures_and_images plugin
RESPONSIVE_IMAGES = True
# Setting for Latex
#LATEX = 'article'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
STATIC_PATHS = [
	'pictures',]
