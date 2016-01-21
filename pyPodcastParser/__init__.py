import os

from bs4 import BeautifulSoup

class Podcast():
    def __init__(self, feed_content):
        self.feed_content = feed_content
        self.soup = BeautifulSoup(self.feed_content, "html.parser")
        self.title = self.soup.title.string

#
# test_dir = os.path.dirname(__file__)
# test_feeds_dir = os.path.join(test_dir, 'test_feeds')
# basic_podcast_path = os.path.join(test_feeds_dir, 'basic_podcast.rss')
# basic_podcast_file = open(basic_podcast_path, "r")
# basic_podcast = basic_podcast_file.read()
#
# podcast = Podcast(basic_podcast)
#
# print("sss")
