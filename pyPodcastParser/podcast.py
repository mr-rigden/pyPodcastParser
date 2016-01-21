import os
from chronyk import Chronyk
import email.utils
from bs4 import BeautifulSoup
import pytz
import datetime

class Podcast():
    def __init__(self, feed_content):
        self.feed_content = feed_content
        self.set_soup()

        self.set_author_name()
        self.set_copyright()
        self.set_creative_commons()
        self.set_categories()
        self.set_generator()
        self.set_image()
        self.set_itunes_block()
        self.set_published_date()
        self.set_owner()
        self.set_subtitle()
        self.set_summary()
        self.set_title()

    def set_soup(self):
        self.soup = BeautifulSoup(self.feed_content, "html.parser")

    def set_author_name(self):
        self.author_name = self.soup.find('itunes:author').string

    def set_categories(self):
        self.categories = []
        temp_categories = self.soup.findAll('itunes:category')
        for category in temp_categories:
            category_text = category.get('text')
            self.categories.append(category_text)

    def set_copyright(self):
        self.copyright = self.soup.find('copyright').string

    def set_creative_commons(self):
        self.creative_commons = self.soup.find('creativeCommons:license')

    def set_generator(self):
        self.generator = self.soup.find('generator').string

    def set_image(self):
        self.image = self.soup.find('itunes:image').get('href')

    def set_itunes_block(self):
        block = self.soup.find('itunes:block')
        if block == "yes":
            self.itunes_block = True
        else:
            self.itunes_block = False

    def set_published_date(self):
        self.published_date = self.soup.find('pubdate').string
        print(self.published_date)
        x = datetime.datetime.fromtimestamp( email.utils.mktime_tz(email.utils.parsedate_tz( self.published_date )), pytz.utc )
        print(x)

    def set_owner(self):
        owner = self.soup.find('itunes:owner')
        self.owner_name = owner.find('itunes:name').string
        self.owner_email = owner.find('itunes:email').string

    def set_subtitle(self):
        self.subtitle = self.soup.find('itunes:subtitle').string

    def set_summary(self):
        self.summary = self.soup.find('itunes:summary').string




    def set_title(self):
        self.title = self.soup.title.string


test_dir = os.path.dirname(__file__)
test_feeds_dir = os.path.join(test_dir, 'test_feeds')
basic_podcast_path = os.path.join(test_feeds_dir, 'basic_podcast.rss')
basic_podcast_file = open(basic_podcast_path, "r")
basic_podcast = basic_podcast_file.read()

podcast = Podcast(basic_podcast)

print(podcast.summary)
