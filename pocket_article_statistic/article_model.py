class Article:
    def __init__(self, web_link, blog_link, tags, time_added, year, month, date, hour, title):
        """
        :param web_link: the full link of the post
        :param blog_link: the link of author
        :param tags:     the tags of article: eg:android, python, java, kotlin, binder,
        :param time_added: the time since the article was added, seconds
        :param year:     2015
        :param month:    10
        :param hour:     14
        :param title: the title of article
        """
        self.web_link = web_link
        self.blog_link = blog_link
        self.tags = tags
        self.time_added = time_added
        self.year = year
        self.month = month
        self.date = date
        self.hour = hour
        self.title = title

    def get_web_link(self):
        return self.web_link

    def get_tag(self):
        return self.tags
