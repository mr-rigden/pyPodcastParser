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
        self.set_full_soup()

        self.set_extended_elements()
        self.set_itunes()
        self.set_optional_elements()
        self.set_required_elements()

    def set_extended_elements(self):
        self.set_creative_commons()
        self.set_owner()
        self.set_subtitle()
        self.set_summary()

    def set_itunes(self):
        self.set_itunes_author_name()
        self.set_itunes_block()
        self.set_itune_image()
        self.set_itunes_keywords()
        self.set_itunes_categories()

    def set_optional_elements(self):
        self.set_copyright()
        self.set_generator()
        self.set_language()
        self.set_last_build_date()
        self.set_managing_editor()
        self.set_published_date()
        self.set_web_master()

    def set_required_elements(self):
        self.set_title()
        self.set_link()
        self.set_description()

    def set_soup(self):
        self.soup = BeautifulSoup(self.feed_content, "html.parser")
        for item in self.soup.findAll('item'):
            item.decompose()

    def set_full_soup(self):
        self.full_soup = BeautifulSoup(self.feed_content, "html.parser")

    def count_items(self):
        soup_items = self.soup.findAll('item')
        full_soup_items = self.full_soup.findAll('item')
        return len(soup_items), len(full_soup_items)



    def set_copyright(self):
        self.copyright = self.soup.find('copyright').string

    def set_creative_commons(self):
        self.creative_commons = self.soup.find('creativeCommons:license')

    def set_description(self):
        self.description = self.soup.find('description').string

    def set_generator(self):
        self.generator = self.soup.find('generator').string

    def set_itunes_author_name(self):
        self.itunes_author_name = self.soup.find('itunes:author').string

    def set_itunes_block(self):
        try:
            block = self.soup.find('itunes:block').string.lower()
        except AttributeError:
            block = ""
        if block == "yes":
            self.itunes_block = True
        else:
            self.itunes_block = False

    def set_itunes_categories(self):
        self.itunes_categories = []
        temp_categories = self.soup.findAll('itunes:category')
        for category in temp_categories:
            category_text = category.get('text')
            self.itunes_categories.append(category_text)

    def set_itune_image(self):
        self.itune_image = self.soup.find('itunes:image').get('href')

    def set_itunes_keywords(self):
        keywords = self.soup.find('itunes:keywords').string
        self.itunes_keywords = [keyword.strip() for keyword in keywords.split(',')]
        self.itunes_keywords = list(set(self.itunes_keywords))




    def set_language(self):
        self.language = self.soup.find('language').string


    def set_last_build_date(self):
        self.last_build_date = self.soup.find('lastbuilddate').string

    def set_link(self):
        self.link = self.soup.find('link').string

    def set_managing_editor(self):
        self.managing_editor = self.soup.find('managingeditor').string

    def set_published_date(self):
        self.published_date = self.soup.find('pubdate').string
        #print(self.published_date)
        x = datetime.datetime.fromtimestamp( email.utils.mktime_tz(email.utils.parsedate_tz( self.published_date )), pytz.utc )
        #print(x)

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

    def set_web_master(self):
        self.web_master = self.soup.find('webmaster').string
