# -*- coding: utf-8 -*-
import os
import unittest

from pyPodcastParser import Podcast

# py.test test_pyPodcastParser.py

#######
# coverage run --source pyPodcastParser -m py.test
#######
# py.test --cov=pyPodcastParser tests/
#######
# py.test -v   --capture=sys tests/test_pyPodcastParser.py


class Test_Test(unittest.TestCase):

    def test_loading_sample_data(self):
        self.assertEqual(True, True)

class Test_Basic_Feed_Items(unittest.TestCase):

    def setUp(self):
        test_dir = os.path.dirname(__file__)
        test_feeds_dir = os.path.join(test_dir, 'test_feeds')
        basic_podcast_path = os.path.join(test_feeds_dir, 'basic_podcast.rss')
        basic_podcast_file = open(basic_podcast_path, "r")
        self.basic_podcast = basic_podcast_file.read()
        self.podcast = Podcast.Podcast(self.basic_podcast)

    def test_item_count(self):
        number_of_items = len(self.podcast.items)
        self.assertEqual(number_of_items, 2)

    def test_item_comments(self):
        self.assertEqual(self.podcast.items[0].comments, "http://comments.com/entry/0")
        self.assertEqual(self.podcast.items[1].comments, "http://comments.com/entry/1")

    def test_item_categories(self):
        self.assertTrue("Grateful Dead" in self.podcast.items[0].categories)
        self.assertTrue("Dead and Grateful" in self.podcast.items[1].categories)

    def test_item_multi_categories(self):
        self.assertTrue("Grateful Dead" in self.podcast.items[0].categories)
        self.assertTrue("Stones" in self.podcast.items[0].categories)

    def test_item_categories_fail(self):
        self.assertFalse("x" in self.podcast.items[0].categories)
        self.assertFalse("x" in self.podcast.items[1].categories)


    def test_item_description(self):
        self.assertEqual(self.podcast.items[0].description, "basic item description")
        self.assertEqual(self.podcast.items[1].description, "another basic item description")

    def test_item_author(self):
        self.assertEqual(self.podcast.items[0].author, "lawyer@boyer.net")
        self.assertEqual(self.podcast.items[1].author, "lawyer@boyer.net (Lawyer Boyer)")

    def test_item_enclosure_url(self):
        self.assertEqual(self.podcast.items[0].enclosure_url, 'https://github.com/jrigden/pyPodcastParser.mp3')

    def test_item_enclosure_type(self):
        self.assertEqual(self.podcast.items[0].enclosure_type, 'audio/mpeg')

    def test_item_enclosure_length(self):
        self.assertEqual(self.podcast.items[0].enclosure_length, 123456)

    def test_item_guid(self):
        self.assertEqual(self.podcast.items[0].guid, 'basic item guid')
        self.assertEqual(self.podcast.items[1].guid, 'another basic item guid')

    def test_item_link(self):
        self.assertEqual(self.podcast.items[0].link, "http://google.com/0")
        self.assertEqual(self.podcast.items[1].link, "http://google.com/1")

    def test_item_published_date(self):
        self.assertEqual(self.podcast.items[0].published_date, "Fri, 21 Mar 2008 09:51:00 EDT")
        self.assertEqual(self.podcast.items[1].published_date, "Fri, 21 Mar 2008 09:50:00 EDT")

    def test_item_title(self):
        self.assertEqual(self.podcast.items[0].title, "basic item title")
        self.assertEqual(self.podcast.items[1].title, "another basic item title")


class Test_Basic_Feed(unittest.TestCase):

    def setUp(self):
        test_dir = os.path.dirname(__file__)
        test_feeds_dir = os.path.join(test_dir, 'test_feeds')
        basic_podcast_path = os.path.join(test_feeds_dir, 'basic_podcast.rss')
        basic_podcast_file = open(basic_podcast_path, "r")
        self.basic_podcast = basic_podcast_file.read()
        self.podcast = Podcast.Podcast(self.basic_podcast)

    def test_loding_of_basic_podcast(self):
        self.assertIsNotNone(self.basic_podcast)

    def test_count_items(self):
        self.assertNotEqual(self.podcast.count_items(), "basic c")

    def test_copyright(self):
        self.assertEqual(self.podcast.copyright, "basic copyright")

    def test_description(self):
        self.assertEqual(self.podcast.description, "basic description")

    def test_generator(self):
        self.assertEqual(self.podcast.generator, "an infinite monkeys")

    def test_itunes_author_name(self):
        self.assertEqual(self.podcast.itunes_author_name,
                         "basic itunes author")

    def test_itunes_block(self):
        self.assertEqual(self.podcast.itunes_block, False)

    def test_itunes_categories(self):
        self.assertTrue("News" in self.podcast.itunes_categories)
        self.assertTrue("Health" in self.podcast.itunes_categories)

    def test_itune_image(self):
        self.assertEqual(self.podcast.itune_image,
                         "https://github.com/jrigden/pyPodcastParser.jpg")

    def test_itunes_categories_length(self):
        number_of_categories = len(self.podcast.itunes_categories)
        self.assertEqual(number_of_categories, 2)

    def test_itunes_keyword_length(self):
        number_of_keywords = len(self.podcast.itunes_keywords)
        self.assertEqual(number_of_keywords, 2)

    def test_language(self):
        self.assertEqual(self.podcast.language, "basic  language")

    def test_last_build_date(self):
        self.assertEqual(self.podcast.last_build_date,
                         "Mon, 24 Mar 2008 23:30:07 EDT")

    def test_link(self):
        self.assertEqual(self.podcast.link,
                         "https://github.com/jrigden/pyPodcastParser")

    def test_managing_editor(self):
        self.assertEqual(self.podcast.managing_editor, "nobody")

    def test_published_date(self):
        self.assertEqual(self.podcast.published_date,
                         "Mon, 24 Mar 2008 23:30:07 EDT")

    def test_owner_name(self):
        self.assertEqual(self.podcast.owner_name, "basic itunes owner name")

    def test_owner_email(self):
        self.assertEqual(self.podcast.owner_email, "basic itunes owner email")

    def test_subtitle(self):
        self.assertEqual(self.podcast.subtitle, "basic itunes subtitle")

    def test_summary(self):
        self.assertEqual(self.podcast.summary, "basic itunes summary")

    def test_summary(self):
        self.assertEqual(self.podcast.summary, "basic itunes summary")

    def test_title(self):
        self.assertEqual(self.podcast.title, "basic title")

    def test_web_master(self):
        self.assertEqual(self.podcast.web_master, "webrobot")


class Test_Itunes_Block_Feed(unittest.TestCase):

    def setUp(self):
        test_dir = os.path.dirname(__file__)
        test_feeds_dir = os.path.join(test_dir, 'test_feeds')
        basic_podcast_path = os.path.join(
            test_feeds_dir, 'itunes_block_podcast.rss')
        basic_podcast_file = open(basic_podcast_path, "r")
        self.basic_podcast = basic_podcast_file.read()
        self.podcast = Podcast.Podcast(self.basic_podcast)

    def test_itunes_block(self):
        self.assertEqual(self.podcast.itunes_block, True)

if __name__ == '__main__':
    unittest.main()
