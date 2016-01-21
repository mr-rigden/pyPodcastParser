import os
import unittest

import pyPodcastParser
#py.test test_pyPodcastParser.py

#######
# coverage run --source pyPodcastParser -m py.test
#######
# py.test --cov=pyPodcastParser tests/
#######
# py.test -v   --capture=sys tests/test_pyPodcastParser.py


class Test_Test(unittest.TestCase):
    def test_loading_sample_data(self):
        self.assertEqual(True, True)

class Test_Basic_Feed(unittest.TestCase):
    def setUp(self):
        test_dir = os.path.dirname(__file__)
        test_feeds_dir = os.path.join(test_dir, 'test_feeds')
        basic_podcast_path = os.path.join(test_feeds_dir, 'basic_podcast.rss')
        basic_podcast_file = open(basic_podcast_path, "r")
        self.basic_podcast = basic_podcast_file.read()
        self.podcast = pyPodcastParser.Podcast(self.basic_podcast)


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
        self.assertEqual(self.podcast.itunes_author_name, "basic itunes author")

    def test_itunes_block(self):
        self.assertEqual(self.podcast.itunes_block, False)


    def test_itunes_categories(self):
        self.assertTrue("News" in self.podcast.itunes_categories)
        self.assertTrue("Health" in self.podcast.itunes_categories)

    def test_itune_image(self):
        self.assertEqual(self.podcast.itune_image, "https://github.com/jrigden/pyPodcastParser.jpg")

    def test_itunes_categories_length(self):
        number_of_categories = len(self.podcast.itunes_categories)
        self.assertEqual(number_of_categories, 2)

    def test_itunes_keyword_length(self):
        number_of_keywords = len(self.podcast.itunes_keywords)
        self.assertEqual(number_of_keywords, 2)

    def test_language(self):
        self.assertEqual(self.podcast.language, "basic  language")

    def test_last_build_date(self):
        self.assertEqual(self.podcast.last_build_date, "Mon, 24 Mar 2008 23:30:07 EDT")

    def test_link(self):
        self.assertEqual(self.podcast.link, "https://github.com/jrigden/pyPodcastParser")

    def test_managing_editor(self):
        self.assertEqual(self.podcast.managing_editor, "nobody")

    def test_published_date(self):
        self.assertEqual(self.podcast.published_date, "Mon, 24 Mar 2008 23:30:07 EDT")

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
        basic_podcast_path = os.path.join(test_feeds_dir, 'itunes_block_podcast.rss')
        basic_podcast_file = open(basic_podcast_path, "r")
        self.basic_podcast = basic_podcast_file.read()
        self.podcast = pyPodcastParser.Podcast(self.basic_podcast)

    def test_itunes_block(self):
        self.assertEqual(self.podcast.itunes_block, True)

if __name__ == '__main__':
    unittest.main()
