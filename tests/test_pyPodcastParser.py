import os
import unittest

import pyPodcastParser
#py.test test_pyPodcastParser.py



class Test_Test(unittest.TestCase):
    def test_loading_sample_data(self):
        self.assertEqual(True, True)

class Test_pyPodcastParser(unittest.TestCase):
    def setUp(self):
        test_dir = os.path.dirname(__file__)
        test_feeds_dir = os.path.join(test_dir, 'test_feeds')
        basic_podcast_path = os.path.join(test_feeds_dir, 'basic_podcast.rss')
        basic_podcast_file = open(basic_podcast_path, "r")
        self.basic_podcast = basic_podcast_file.read()

    def test_loding_of_basic_podcast(self):
        self.assertIsNotNone(self.basic_podcast)

    def test_basic(self):
        podcast = pyPodcastParser.Podcast(self.basic_podcast)
        self.assertEqual(podcast.title, "basic title")


if __name__ == '__main__':
    unittest.main()
