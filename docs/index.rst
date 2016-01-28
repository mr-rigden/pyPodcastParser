.. pyPodcastParser documentation master file, created by
   sphinx-quickstart on Tue Jan 19 10:08:42 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

pyPodcastParser!
===========================================

=================
Introduction
=================


pyPodcastParser is a podcast parser. It should parse any RSS file, but it specializes in parsing podcast rss feeds. pyPodcastParser is agnostic about the method you use to get a podcast RSS feed. Most user will be most comfortable with the Requests_ library.

.. _Requests: http://docs.python-requests.org/en/latest/

=================
Installation
=================

::

   pip install pyPodcastParser


=================
Usage
=================

::

   from pyPodcastParser.Podcast import Podcast
   import requests

   request = requests.get('https://some_rss_feed')
   podcast = Podcast(request.content)


=================
Bugs & Feature Requests
=================

https://github.com/jrigden/pyPodcastParser/issues/new

=================
Credits
=================
**Jason Rigden**

    **Email:** jasonrigden@gmail.com

    **Linkedin:** https://www.linkedin.com/in/jasonrigden

    **Twitter:** mr_rigden_
.. _mr_rigden: https://twitter.com/mr_rigden


=================
Development
=================

https://github.com/jrigden/pyPodcastParser

=================
Testing
=================

.. image:: https://travis-ci.org/jrigden/pyPodcastParser.svg?branch=master
    :target: https://travis-ci.org/jrigden/pyPodcastParser
.. image:: https://coveralls.io/repos/github/jrigden/pyPodcastParser/badge.svg?branch=master
    :target: https://coveralls.io/github/jrigden/pyPodcastParser?branch=master

=================
License
=================

**The MIT License** (MIT) Copyright (c) 2016 **Jason Rigden**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

=================
Contents
=================

.. toctree::
   :maxdepth: 2

   api
