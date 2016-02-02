from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyPodcastParser',

    version='1.1.1',

    description='pyPodcastParser is a podcast parser.',
    long_description=long_description,

    url='https://github.com/jrigden/pyPodcastParser',

    author='Jason Rigden',
    author_email='jasonrigden@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup :: XML',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    install_requires=[
        "beautifulsoup4",
    ],

    keywords=['podcast', 'parser', 'rss', 'feed'],

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),


)
