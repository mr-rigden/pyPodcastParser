# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from datetime import datetime
import email.utils
from time import mktime

from pyPodcastParser.Item import Item


class Podcast():
    """Parses an xml rss feed

    RSS Specs http://cyber.law.harvard.edu/rss/rss.html

    More RSS Specs http://www.rssboard.org/rss-specification

    iTunes Podcast Specs http://www.apple.com/itunes/podcasts/specs.html


    The cloud element aka RSS Cloud is not supported as it has been superseded by the superior PubSubHubbub protocal

    Args:
        feed_content (str): An rss string

    Note:
        All attributes with empty or nonexistent element will have a value of None

        Attributes are generally strings or lists of strings, because we want to record the literal value of elements.

    Attributes:
        feed_content (str): The actual xml of the feed
        soup (bs4.BeautifulSoup): A soup of the xml with items and image removed
        image_soup (bs4.BeautifulSoup): soup of image
        full_soup (bs4.BeautifulSoup): A soup of the xml with items
        categories (list): List for strings representing the feed categories
        copyright (str): The feed's copyright
        creative_commons (str): The feed's creative commons license
        items (item): Item objects
        description (str): The feed's description
        generator (str): The feed's generator
        image_title (str): Feed image title
        image_url (str): Feed image url
        image_link (str): Feed image link to homepage
        image_width (str): Feed image width
        image_height (str): Feed image height
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
        pubsubhubbub (str): The URL of the pubsubhubbub service for this feed
        owner_name (str): Name of feed owner
        owner_email (str): Email of feed owner
        subtitle (str): The feed subtitle
        title (str): The feed title
        ttl (str): The time to live or number of minutes to cache feed
        web_master (str): The feed's webmaster
        is_valid_rss (bool): Is this a valid RSS Feed
        is_valid_podcast (bool): Is this a valid Podcast
        date_time (datetime): When published
    """

    def __init__(self, feed_content):
        #super(Podcast, self).__init__()
        self.feed_content = feed_content
        self.set_soup()
        self.set_full_soup()

        self.set_extended_elements()
        self.set_itunes()
        self.set_optional_elements()
        self.set_required_elements()

        self.set_validity()
        self.set_time_published()
        self.set_dates_published()

    def set_time_published(self):
        if self.published_date is None:
            self.time_published = None
            return
        time_tuple = email.utils.parsedate_tz(self.published_date)
        self.time_published = email.utils.mktime_tz(time_tuple)

    def set_dates_published(self):
        if self.published_date is None:
            self.date_time = None
        else:
            time_tuple = email.utils.parsedate(self.published_date)
            temp_datetime = datetime(time_tuple[0], time_tuple[1], time_tuple[2])
            self.date_time = temp_datetime

    def set_validity(self):
        self.set_is_valid_rss()
        self.set_is_valid_podcast()

    def set_is_valid_rss(self):
        """Check to if this is actually a valid RSS feed"""
        if self.title and self.link and self.description:
            self.is_valid_rss = True
        else:
            self.is_valid_rss = False

    def set_is_valid_podcast(self):
        for item in self.items:
            if item.enclosure_type:
                if item.enclosure_type.lower() == "audio/mpeg":
                    self.is_valid_podcast = True
                    return
        self.is_valid_podcast =  False

    def to_dict(self):
        podcast_dict = {}
        podcast_dict['categories'] = self.categories
        podcast_dict['copyright'] = self.copyright
        podcast_dict['creative_commons'] = self.creative_commons
        podcast_dict['description'] = self.description
        podcast_dict['generator'] = self.generator
        podcast_dict['image_title'] = self.image_title
        podcast_dict['image_url'] = self.image_url
        podcast_dict['image_link'] = self.image_link
        podcast_dict['image_width'] = self.image_width
        podcast_dict['image_height'] = self.image_height
        podcast_dict['items'] = []
        for item in self.items:
            item_dict = item.to_dict()
            podcast_dict['items'].append(item_dict)
        podcast_dict['itunes_author_name'] = self.itunes_author_name
        podcast_dict['itunes_block'] = self.itunes_block
        podcast_dict['itunes_categories'] = self.itunes_categories
        podcast_dict['itunes_block'] = self.itunes_block
        podcast_dict['itunes_complete'] = self.image_width
        podcast_dict['itunes_explicit'] = self.itunes_explicit
        podcast_dict['itune_image'] = self.itune_image
        podcast_dict['itunes_keywords'] = self.image_width
        podcast_dict['itunes_explicit'] = self.itunes_explicit
        podcast_dict['itunes_new_feed_url'] = self.itunes_new_feed_url
        podcast_dict['language'] = self.language
        podcast_dict['last_build_date'] = self.last_build_date
        podcast_dict['link'] = self.link
        podcast_dict['managing_editor'] = self.managing_editor
        podcast_dict['published_date'] = self.published_date
        podcast_dict['pubsubhubbub'] = self.pubsubhubbub
        podcast_dict['owner_name'] = self.owner_name
        podcast_dict['owner_email'] = self.owner_email
        podcast_dict['subtitle'] = self.subtitle
        podcast_dict['title'] = self.title
        podcast_dict['ttl'] = self.ttl
        podcast_dict['web_master'] = self.web_master
        return podcast_dict

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
        self.set_categories()
        self.set_copyright()
        self.set_generator()
        self.set_image()
        self.set_language()
        self.set_last_build_date()
        self.set_managing_editor()
        self.set_published_date()
        self.set_pubsubhubbub()
        self.set_ttl()
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
        for image in self.soup.findAll('image'):
            image.decompose()

    def set_full_soup(self):
        """Sets soup and keeps items"""
        self.full_soup = BeautifulSoup(self.feed_content, "html.parser")

    def set_items(self):
        self.items = []
        full_soup_items = self.full_soup.findAll('item')
        for full_soup_item in full_soup_items:
            item = Item(full_soup_item)
            if item:
                self.items.append(item)

    def set_categories(self):
        """Parses and set feed categories"""
        self.categories = []
        temp_categories = self.soup.findAll('category')
        for category in temp_categories:
            category_text = category.string
            self.categories.append(category_text)

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
        """Parses creative commons for item and sets value"""
        try:
            self.creative_commons = self.soup.find(
                'creativecommons:license').string
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

    def set_image(self):
        """Parses image element and set values"""
        temp_soup = self.full_soup
        for item in temp_soup.findAll('item'):
            item.decompose()
        image = temp_soup.find('image')
        try:
            self.image_title = image.find('title').string
        except AttributeError:
            self.image_title = None
        try:
            self.image_url = image.find('url').string
        except AttributeError:
            self.image_url = None
        try:
            self.image_link = image.find('link').string
        except AttributeError:
            self.image_link = None
        try:
            self.image_width = image.find('width').string
        except AttributeError:
            self.image_width = None
        try:
            self.image_height = image.find('height').string
        except AttributeError:
            self.image_height = None

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
            self.itunes_keywords = [keyword.strip()
                                    for keyword in keywords.split(',')]
            self.itunes_keywords = list(set(self.itunes_keywords))
        except AttributeError:
            self.itunes_keywords = []

    def set_itunes_new_feed_url(self):
        """Parses new feed url from itunes tags and sets value"""
        try:
            self.itunes_new_feed_url = self.soup.find(
                'itunes:new-feed-url').string
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

    def set_pubsubhubbub(self):
        """Parses pubsubhubbub and email then sets value"""
        self.pubsubhubbub = None
        atom_links = self.soup.findAll('atom:link')
        for atom_link in atom_links:
            rel = atom_link.get('rel')
            if rel == "hub":
                self.pubsubhubbub = atom_link.get('href')

    def set_owner(self):
        """Parses owner name and email then sets value"""
        owner = self.soup.find('itunes:owner')
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

    def set_ttl(self):
        """Parses summary and set value"""
        try:
            self.ttl = self.soup.find('ttl').string
        except AttributeError:
            self.ttl = None

    def set_web_master(self):
        """Parses the feed's webmaster and sets value"""
        try:
            self.web_master = self.soup.find('webmaster').string
        except AttributeError:
            self.web_master = None
