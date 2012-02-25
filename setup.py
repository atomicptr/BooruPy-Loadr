#!/usr/bin/env python
from distutils.core import setup

setup(
	name = "BooruPy Loadr",
	version = "1.2",
	keywords = ['pictures', 'anime', 'booru', 'gelbooru', 'danbooru', 'image',
		'board', 'imageboard', 'download', 'tool'],
	author = 'Christopher Kaster',
	author_email = 'ikasoki@gmail.com',
	maintainer = 'Christopher Kaster',
	maintainer_email = 'ikasoki@gmail.com',
	install_requires = ['BooruPy>=0.1.5'],
	url = 'http://github.com/Kasoki/BooruPy-Loadr',
	license = 'GNU GENERAL PUBLIC LICENSE v3',
	description = 'BooruPy Loadr is a download tool for various image board "Booru" systems.',
	long_description = open('README.rst').read(),
	platforms = 'OS Independent',
	classifiers = [
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: End Users/Desktop',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 2.7',
		'Topic :: Internet'
	],
	data_files = [
		('data', '*')
	]
)