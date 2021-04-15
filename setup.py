#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('docs/usage.rst') as usage_file:
    usage = usage_file.read()

requirements = [
    'Click>=7.1',
    'lxml',
    'beautifulsoup4',
    'urllib3',
    'urllib3[secure]',
    'pysocks',
    'gevent',
    'stem',
    'certifi',
]

setup_requirements = [
    'pytest'
    # TODO(SekouDiaoNLP): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'Sphinx',
    'docutils',
    'pytest',
    'pytest-cov',
    'Click>=7.1',
    'lxml',
    'beautifulsoup4',
    'requests',
    'requests[socks]',
    'urllib3'
    'PySocks',
    'gevent',
    'stem'
]

setup(
    name='lyricsmaster3',
    version='2.8.1',
    description="LyricsMaster3 is a library for downloading lyrics from multiple lyrics providers. LyricWiki, AzLyrics, Genius, Lyrics007, MusixMatch and other lyrics provider are available",
    long_description=readme + '\n\n' + usage + '\n\n' + history,
    author="SekouDiaoNLP",
    author_email='diao.sekou.nlp@gmail.com',
    url='https://github.com/SekouDiaoNLP/lyricsmaster3',
    packages=find_packages(include=['lyricsmaster3']),
    entry_points={
        'console_scripts': [
            'lyricsmaster3=lyricsmaster3.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='lyricsmaster3 lyrics LyricWiki Lyrics Wikia Lyrics007 AzLyrics Genius MusixMatch Tor',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Topic :: Communications',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
