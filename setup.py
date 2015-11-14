#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


__version__ = "0.0.2"


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()


if sys.argv[-1] == 'tag':
    os.system("git tag -a v%s -m 'version v%s'" % (__version__, __version__))
    os.system("git push --tags")
    sys.exit()

requirements = [
    'BeautifulSoup==3.2.1',
    'requests==2.7.0',
]


long_description = open('README.md').read() + "\n\n"


setup(
    name='vocabpie',
    version=__version__,
    license='License :: OSI Approved :: MIT License',
    description="Look up dictionary definitions, etymology references, and synonym/antonyms of words.",
    long_description=long_description,
    author='DietrichWambach',
    author_email='dietrich.wambach@protonmail.ch',
    url='https://github.com/wamsachel/vocabpie',
    download_url='https://github.com/wamsachel/vocabpie',
    #packages = find_packages(),
    packages = ['vocabpie'],
    # scripts = ['bin/etym', 'bin/dict', 'bin/thes'],
    # scripts = ['bin/etym', 'bin/dict', 'bin/thes'],
    # entry_points = {'console_scripts': ['dict = vocabpie.dictionary:run_dict',]},
    install_requires=requirements,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
)
