# -*- coding: utf-8 -*-
import email.utils
from bs4 import BeautifulSoup
import pytz
import datetime

from pyPodcastParser.Item import Item

class Podcast():
    """Parses an xml rss feed

    RSS Specs http://cyber.law.harvard.edu/rss/rss.html
    iTunes Podcast Specs http://www.apple.com/itunes/podcasts/specs.html

    Args:
        feed_content (str): An rss string

    Note:
        All attributes with empty or nonexistent element will have a value of None

    Attributes:
        feed_content (str): The actual xml of the feed
        soup (bs4.BeautifulSoup): A soup of the xml with items removed
        full_soup (bs4.BeautifulSoup): A soup of the xml with items
        copyright (str): The feed's copyright
        creative_commons (str): The feed's creative commons licens
        description (str): The feed's description
        generator (str): The feed's generator
        itunes_author_name (str): The podcast's author name for iTunes
        itunes_block (bool): Does the podcast block itunes
        itunes_categories (list): List of strings of itunes categories
        itunes_complete (str): Is this podcast done and complete
        itunes_explicit (str): Is this item explicit. Should only be "yes" and "clean."
        itune_image (str): URL to itunes image
        itunes_keywords (list): List of strings of itunes keywords
        itunes_new_feed_url (str): The new url of this podcast
        language (str): Language of feed
        last_build_date (str): Last build date of this feed
        link (str): URL to homepage
        managing_editor (str): managing editor of feed
        published_date (str): Date feed was published
        owner_name (str): Name of feed owner
        owner_email (str): Email of feed owner
        subtitle (str): The feed subtitle
        title (str): The feed title
        web_master (str): The feed's webmaster
    """

    def __init__(self, feed_content):
        super(Podcast, self).__init__()
        self.feed_content = feed_content
        self.set_soup()
        self.set_full_soup()

        self.set_extended_elements()
        self.set_itunes()
        self.set_optional_elements()
        self.set_required_elements()

    def set_extended_elements(self):

        """Parses and sets non required elements"""
        self.set_creative_commons()
        self.set_owner()
        self.set_subtitle()
        self.set_summary()

    def set_itunes(self):
        """Sets elements related to itunes"""
        self.set_itunes_author_name()
        self.set_itunes_block()
        self.set_itunes_complete()
        self.set_itunes_explicit()
        self.set_itune_image()
        self.set_itunes_keywords()
        self.set_itunes_new_feed_url()
        self.set_itunes_categories()
        self.set_items()

    def set_optional_elements(self):
        """Sets elements considered option by RSS spec"""
        self.set_copyright()
        self.set_generator()
        self.set_language()
        self.set_last_build_date()
        self.set_managing_editor()
        self.set_published_date()
        self.set_web_master()

    def set_required_elements(self):
        """Sets elements required by RSS spec"""
        self.set_title()
        self.set_link()
        self.set_description()

    def set_soup(self):
        """Sets soup and strips items"""
        self.soup = BeautifulSoup(self.feed_content, "html.parser")
        for item in self.soup.findAll('item'):
            item.decompose()

    def set_full_soup(self):
        """Sets soup and keeps items"""
        self.full_soup = BeautifulSoup(self.feed_content, "html.parser")

    def set_items(self):
        self.items = []
        full_soup_items = self.full_soup.findAll('item')
        for full_soup_item in full_soup_items:
            item = Item(full_soup_item)
            print(item)
            if item:
                self.items.append(item)

    def count_items(self):
        """Counts Items in full_soup and soup. For debugging"""
        soup_items = self.soup.findAll('item')
        full_soup_items = self.full_soup.findAll('item')
        return len(soup_items), len(full_soup_items)

    def set_copyright(self):
        """Parses copyright and set value"""
        try:
            self.copyright = self.soup.find('copyright').string
        except AttributeError:
            self.copyright = None

    def set_creative_commons(self):
        """Parses creative commons and set value"""
        try:
            self.creative_commons = self.soup.find('creativeCommons:license').string
        except AttributeError:
            self.creative_commons = None

    def set_description(self):
        """Parses description and sets value"""
        try:
            self.description = self.soup.find('description').string
        except AttributeError:
            self.description = None

    def set_generator(self):
        """Parses feed generator and sets value"""
        try:
            self.generator = self.soup.find('generator').string
        except AttributeError:
            self.generator = None

    def set_itunes_author_name(self):
        """Parses author name from itunes tags and sets value"""
        try:
            self.itunes_author_name = self.soup.find('itunes:author').string
        except AttributeError:
            self.itunes_author_name = None

    def set_itunes_block(self):
        """Check and see if podcast is blocked from iTunes and sets value"""
        try:
            block = self.soup.find('itunes:block').string.lower()
        except AttributeError:
            block = ""
        if block == "yes":
            self.itunes_block = True
        else:
            self.itunes_block = False

    def set_itunes_categories(self):
        """Parses and set itunes categories"""
        self.itunes_categories = []
        temp_categories = self.soup.findAll('itunes:category')
        for category in temp_categories:
            category_text = category.get('text')
            self.itunes_categories.append(category_text)

    def set_itunes_complete(self):
        """Parses complete from itunes tags and sets value"""
        try:
            self.itunes_complete = self.soup.find('itunes:complete').string
            self.itunes_complete = self.itunes_complete.lower()
        except AttributeError:
            self.itunes_complete = None

    def set_itunes_explicit(self):
        """Parses explicit from itunes tags and sets value"""
        try:
            self.itunes_explicit = self.soup.find('itunes:explicit').string
            self.itunes_explicit = self.itunes_explicit.lower()
        except AttributeError:
            self.itunes_explicit = None

    def set_itune_image(self):
        """Parses itunes images and set url as value"""
        try:
            self.itune_image = self.soup.find('itunes:image').get('href')
        except AttributeError:
            self.itune_image = None

    def set_itunes_keywords(self):
        """Parses itunes keywords and set value"""
        try:
            keywords = self.soup.find('itunes:keywords').string
        except AttributeError:
            keywords = None
        try:
            self.itunes_keywords = [keyword.strip() for keyword in keywords.split(',')]
            self.itunes_keywords = list(set(self.itunes_keywords))
        except AttributeError:
            self.itunes_keywords = []


    def set_itunes_new_feed_url(self):
        """Parses new feed url from itunes tags and sets value"""
        try:
            self.itunes_new_feed_url = self.soup.find('itunes:new-feed-url').string
        except AttributeError:
            self.itunes_new_feed_url = None

    def set_language(self):
        """Parses feed language and set value"""
        try:
            self.language = self.soup.find('language').string
        except AttributeError:
            self.language = None

    def set_last_build_date(self):
        """Parses last build date and set value"""
        try:
            self.last_build_date = self.soup.find('lastbuilddate').string
        except AttributeError:
            self.last_build_date = None


    def set_link(self):
        """Parses link to homepage and set value"""
        try:
            self.link = self.soup.find('link').string
        except AttributeError:
            self.link = None

    def set_managing_editor(self):
        """Parses managing editor and set value"""
        try:
            self.managing_editor = self.soup.find('managingeditor').string
        except AttributeError:
            self.managing_editor = None

    def set_published_date(self):
        """Parses published date and set value"""
        try:
            self.published_date = self.soup.find('pubdate').string
        except AttributeError:
            self.published_date = None


    def set_owner(self):
        """Parses owner name and email then sets value"""
        try:
            owner = self.soup.find('itunes:owner')
        except AttributeError:
            owner = None
        try:
            self.owner_name = owner.find('itunes:name').string
        except AttributeError:
            self.owner_name = None
        try:
            self.owner_email = owner.find('itunes:email').string
        except AttributeError:
            self.owner_email = None

    def set_subtitle(self):
        """Parses subtitle and sets value"""
        try:
            self.subtitle = self.soup.find('itunes:subtitle').string
        except AttributeError:
            self.subtitle = None

    def set_summary(self):
        """Parses summary and set value"""
        try:
            self.summary = self.soup.find('itunes:summary').string
        except AttributeError:
            self.summary = None

    def set_title(self):
        """Parses title and set value"""
        try:
            self.title = self.soup.title.string
        except AttributeError:
            self.title = None

    def set_web_master(self):
        """Parses the feed's webmaster and sets value"""
        try:
            self.web_master = self.soup.find('webmaster').string
        except AttributeError:
            self.web_master = None
