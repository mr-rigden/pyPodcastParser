###############
pyPodcastParser
###############

|pypi| |pip_monthly| |testing| |coverall| |codacy| |license|

pyPodcastParser is a podcast parser. It should parse any RSS file, but it specializes in parsing podcast rss feeds. pyPodcastParser is agnostic about the method you use to get a podcast RSS feed. Most user will be comfortable with the Requests_ library.


.. _Requests: http://docs.python-requests.org/en/latest/

************
Installation
************


::

   pip install pyPodcastParser


*****
Usage
*****

::

   from pyPodcastParser.Podcast import Podcast
   import requests

   response = requests.get('https://some_rss_feed')
   podcast = Podcast(response.content)


===================================
Objects and their Useful Attributes
===================================

**Notes:**

* All attributes with empty or nonexistent element will have a value of None.
* Attributes are generally strings or lists of strings, because we want to record the literal value of elements.
* The cloud element aka RSS Cloud is not supported as it has been superseded by the superior PubSubHubbub protocal

-------
Podcast
-------

* categories (list) A list for strings representing the feed categories
* copyright (string): The feed's copyright
* creative_commons (string): The feed's creative commons license
* items (list): A list of Item objects
* description (string): The feed's description
* generator (string): The feed's generator
* image_title (string): Feed image title
* image_url (string): Feed image url
* image_link (string): Feed image link to homepage
* image_width (string): Feed image width
* image_height (Sample H4string): Feed image height
* itunes_author_name (string): The podcast's author name for iTunes
* itunes_block (boolean): Does the podcast block itunes
* itunes_categories (list): List of strings of itunes categories
* itunes_complete (string): Is this podcast done and complete
* itunes_explicit (string): Is this item explicit. Should only be "yes" and "clean."
* itune_image (string): URL to itunes image
* itunes_keywords (list): List of strings of itunes keywords
* itunes_new_feed_url (string): The new url of this podcast
* language (string): Language of feed
* last_build_date (string): Last build date of this feed
* link (string): URL to homepage
* managing_editor (string): managing editor of feed
* published_date (string): Date feed was published
* pubsubhubbub (string): The URL of the pubsubhubbub service for this feed
* owner_name (string): Name of feed owner
* owner_email (string): Email of feed owner
* subtitle (string): The feed subtitle
* title (string): The feed title
* ttl (string): The time to live or number of minutes to cache feed
* web_master (string): The feed's webmaster
* date_time (datetime): When published

----
Item
----

* author (string): The author of the item
* comments (string): URL of comments
* creative_commons (string): creative commons license for this item
* description (string): Description of the item.
* enclosure_url (string): URL of enclosure
* enclosure_type (string): File MIME type
* enclosure_length (integer): File size in bytes
* guid (string): globally unique identifier
* itunes_author_name (string): Author name given to iTunes
* itunes_block (boolean): It this Item blocked from itunes
* itunes_closed_captioned: (string): It is this item have closed captions
* itunes_duration (string): Duration of enclosure
* itunes_explicit (string): Is this item explicit. Should only be "yes" and "clean."
* itune_image (string): URL of item cover art
* itunes_order (string): Override published_date order
* itunes_subtitle (string): The item subtitle
* itunes_summary (string): The summary of the item
* link (string): The URL of item.
* published_date (string): Date item was published
* title (string): The title of item.
* date_time (datetime): When published

***********************
Bugs & Feature Requests
***********************

https://github.com/jrigden/pyPodcastParser/issues/new

*******
Credits
*******

============
Jason Rigden
============

    **Email:** jasonrigden@gmail.com

    **Linkedin:** https://www.linkedin.com/in/jasonrigden

    **Twitter:** |twitter|

*******
History
*******

**Version 2.0.0**

* Removed most time attributes and replaced then them with more concise and versatile datetime object

**Version 1.1.1**

* Fixed missed named attribute in items

**Version 1.1.0**

* Added Validation for RSS and podcasts
* Added several useful time attributes


***********
Development
***********

https://github.com/jrigden/pyPodcastParser

****
Docs
****

http://pypodcastparser.readthedocs.org/en/latest/

*******
Testing
*******

.. image:: https://travis-ci.org/jrigden/pyPodcastParser.svg?branch=master
    :target: https://travis-ci.org/jrigden/pyPodcastParser
.. image:: https://coveralls.io/repos/github/jrigden/pyPodcastParser/badge.svg?branch=master
    :target: https://coveralls.io/github/jrigden/pyPodcastParser?branch=master

*******
License
*******

**The MIT License** (MIT) Copyright (c) 2016 **Jason Rigden**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

.. |coverall| image:: https://coveralls.io/repos/github/jrigden/pyPodcastParser/badge.svg?branch=master
    :alt: Test Status
    :scale: 100%
    :target: https://coveralls.io/github/jrigden/pyPodcastParser?branch=master

.. |codacy| image:: https://img.shields.io/codacy/6f81796c588f455f85c631d8e47b46fc.svg?style=flat-square
    :alt: Codacy Grade
    :scale: 100%
    :target: https://www.codacy.com/app/jasonrigden/pyPodcastParser/dashboard

.. |docs| image:: https://readthedocs.org/projects/docs/badge/?version=latest
    :alt: Documentation Status
    :scale: 100%
    :target: https://pypodcastparser.readthedocs.org/en/latest/?badge=latest

.. |license| image:: https://img.shields.io/pypi/l/pyloudness.svg
    :alt: License
    :scale: 100%
    :target: https://opensource.org/licenses/MIT

.. |pypi| image:: https://badge.fury.io/py/pyPodcastParser.svg
    :alt: pypi
    :scale: 100%
    :target: https://pypi.python.org/pypi/pyPodcastParser

.. |pip_monthly| image:: https://img.shields.io/pypi/dm/pyPodcastParser.svg
    :alt: Pip Monthly Downloads
    :scale: 100%
    :target: https://pypi.python.org/pypi/pyPodcastParser

.. |testing| image:: https://travis-ci.org/jrigden/pyPodcastParser.svg?branch=master
    :alt: Test Status
    :scale: 100%
    :target: https://travis-ci.org/jrigden/pyPodcastParser

.. |twitter| image:: https://img.shields.io/twitter/follow/mr_rigden.svg?style=social
    :alt: @mr_rigden
    :scale: 100%
    :target: https://twitter.com/mr_rigden
