class Item(object):
    """Parses an xml rss feed

    Args:
        soup (bs4.BeautifulSoup): BeautifulSoup object representing a rss item

    Note:
        All attributes with empty or nonexistent element will have a value of None

    Attributes:
        author (str): The author of the item
        comments (str): URL of comments
        description (str): Description of the item.
        enclosure_url (str): URL of enclosure
        enclosure_type (str): File MIME type
        enclosure_length (int): File size in bytes
        guid (str): globally unique identifier
        link (str): The URL of item.
        published_date (str): Date item was published
        title (str): The title of item.
    """
    def __init__(self, soup):
        super(Item, self).__init__()

        self.soup = soup
        self.set_rss_element()
        self.set_itunes_element()

    def set_rss_element(self):
        self.set_author()
        self.set_categories()
        self.set_comments()
        self.set_description()
        self.set_enclosure()
        self.set_guid()
        self.set_link()
        self.set_published_date()
        self.set_title()

    def set_itunes_element(self):
        pass

    def set_author(self):
        """Parses author and set value"""
        self.author = self.soup.find('author').string

    def set_categories(self):
        """Parses and set categories"""
        self.categories = []
        temp_categories = self.soup.findAll('category')
        for category in temp_categories:
            category_text = category.string
            self.categories.append(category_text)

    def set_comments(self):
        """Parses comments and set value"""
        self.comments = self.soup.find('comments').string

    def set_description(self):
        """Parses description and set value"""
        self.description = self.soup.find('description').string

    def set_enclosure(self):
        """Parses enclosure_url, enclosure_type then set values"""
        self.enclosure_url = self.soup.find('enclosure')['url']
        self.enclosure_type = self.soup.find('enclosure')['type']
        self.enclosure_length = self.soup.find('enclosure')['length']
        self.enclosure_length = int(self.enclosure_length)

    def set_guid(self):
        """Parses guid and set value"""
        self.guid = self.soup.find('guid').string

    def set_link(self):
        """Parses link and set value"""
        self.link = self.soup.find('link').string

    def set_published_date(self):
        """Parses published date and set value"""
        self.published_date = self.soup.find('pubdate').string

    def set_title(self):
        """Parses title and set value"""
        self.title = self.soup.find('title').string
