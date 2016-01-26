# -*- coding: utf-8 -*-
import email.utils
from bs4 import BeautifulSoup
import pytz
import datetime


class Podcast():
    """Parses an xml rss feed

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
        itune_image (str): URL to itunes image
        itunes_keywords (list): List of strings of itunes keywords
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
        self.set_itune_image()
        self.set_itunes_keywords()
        self.set_itunes_categories()

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

    def count_items(self):
        """Counts Items in full_soup and soup. For debugging"""
        soup_items = self.soup.findAll('item')
        full_soup_items = self.full_soup.findAll('item')
        return len(soup_items), len(full_soup_items)

    def set_copyright(self):
        """Parses copyright and set value"""
        self.copyright = self.soup.find('copyright').string

    def set_creative_commons(self):
        """Parses creative commons and set value"""
        self.creative_commons = self.soup.find('creativeCommons:license')

    def set_description(self):
        """Parses description and sets value"""
        self.description = self.soup.find('description').string

    def set_generator(self):
        """Parses feed generator and sets value"""
        self.generator = self.soup.find('generator').string

    def set_itunes_author_name(self):
        """Parses author name from itunes tags and sets value"""
        self.itunes_author_name = self.soup.find('itunes:author').string

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

    def set_itune_image(self):
        """Parses itunes images and set url as value"""
        self.itune_image = self.soup.find('itunes:image').get('href')

    def set_itunes_keywords(self):
        """Parses itunes keywords and set value"""
        keywords = self.soup.find('itunes:keywords').string
        self.itunes_keywords = [keyword.strip()
                                for keyword in keywords.split(',')]
        self.itunes_keywords = list(set(self.itunes_keywords))

    def set_language(self):
        """Parses feed language and set value"""
        self.language = self.soup.find('language').string

    def set_last_build_date(self):
        """Parses last build date and set value"""
        self.last_build_date = self.soup.find('lastbuilddate').string

    def set_link(self):
        """Parses link to homepage and set value"""
        self.link = self.soup.find('link').string

    def set_managing_editor(self):
        """Parses managing editor and set value"""
        self.managing_editor = self.soup.find('managingeditor').string

    def set_published_date(self):
        """Parses published date and set value"""
        self.published_date = self.soup.find('pubdate').string

    def set_owner(self):
        """Parses owner name and email then sets value"""
        owner = self.soup.find('itunes:owner')
        self.owner_name = owner.find('itunes:name').string
        self.owner_email = owner.find('itunes:email').string

    def set_subtitle(self):
        """Parses subtitle and sets value"""
        self.subtitle = self.soup.find('itunes:subtitle').string

    def set_summary(self):
        """Parses summary and set value"""
        self.summary = self.soup.find('itunes:summary').string

    def set_title(self):
        """Parses title and set value"""
        self.title = self.soup.title.string

    def set_web_master(self):
        """Parses the feed's webmaster and sets value"""
        self.web_master = self.soup.find('webmaster').string
