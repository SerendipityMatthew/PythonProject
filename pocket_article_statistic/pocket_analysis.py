import re
import time
from collections import Counter

import matplotlib.pyplot as plt
import numpy as np
from bs4 import BeautifulSoup

pocket_export = open("ril_export.html", 'r')
pocket_page = pocket_export.read()
soup = BeautifulSoup(pocket_page, "html.parser")
article_list = list(soup.find_all('a'))


def parse_article(articles):
    string = str(articles)
    result = re.search(r'<a href=(.*) tags=(.*) time_added=(.*)>(.*)</a>', string)
    web_link = result.group(1).strip('"')
    tags = result.group(2).strip('"')
    time_added = result.group(3).strip('"')
    time_added = int(time_added)
    time_added = time.localtime(time_added)
    time_added = time.strftime("%Y-%m-%d %H:%M:%S", time_added)
    title = result.group(4).strip('"')
    return Article(web_link, tags, time_added, title)


class Article:
    def __init__(self, web_link, tags, time_added, title):
        self.web_link = web_link
        self.tags = tags
        self.time_added = time_added
        self.title = title

    def get_web_link(self):
        return self.web_link

    def get_tag(self):
        return self.tags


lists = map(parse_article, article_list)
article_date_list = []  # 2018-03
article_time_list = []  # 12:24
for l in lists:
    time_string = l.time_added
    article_date_list.append(str(time_string)[0:7])
    article_time_list.append(int(str(time_string)[11:13]))

article_date_list = Counter(article_date_list)
article_time_list = Counter(article_time_list)

x_time = [k for k in article_date_list.keys()]
x = [k for k in reversed(x_time)]
y_count = [v for v in article_date_list.values()]
y = [v for v in reversed(y_count)]


def dict2list(dic: dict):
    keys = dic.keys()
    vals = dic.values()
    lst = [(key, val) for key, val in zip(keys, vals)]
    return lst


article_time_list = sorted(dict2list(article_time_list), key=lambda x: x[0])
article_time_list = dict(article_time_list)
time_x = [k for k in article_time_list.keys()]
time_y = [v for v in article_time_list.values()]

# print(time_x)
# print(time_y)

plt.figure(figsize=(200, 100))
plt.title("Saved Article Statistics")
plt.xlabel('Date of saved article')
plt.ylabel('Article Account')
plt.plot(x, y, 'g', linewidth=2, )
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(200, 100))
plt.title("Saved Article Statistics")
plt.xlabel('Time of saved article')
plt.ylabel('Article Account')
plt.plot(time_x, time_y, 'r', linewidth=2, )
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.xticks(np.arange(min(time_x), max(time_x) + 1, 1.0))
plt.show()
