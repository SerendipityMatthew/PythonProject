import re
import time
from collections import Counter

import matplotlib.pyplot as plt
import numpy as np
import tld
from bs4 import BeautifulSoup

from article_model import Article

pocket_export = open("./pocket_analysis/ril_export.html", 'r')
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
    year = time_added[0:4]
    month = time_added[5:7]
    date = time_added[8:10]
    hour = time_added[11:13]
    blog_link = tld.get_tld(url=web_link)
    return Article(web_link=web_link, blog_link=blog_link, tags=tags,
                   time_added=time_added, year=year, month=month, date=date,
                   hour=hour, title=title)


lists = map(parse_article, article_list)
article_date_list = []  # 2018-03
article_time_list = []  # 12:24
article_blog_link = []
for l in lists:
    time_string = l.time_added
    article_date_list.append(str(time_string)[0:7])
    article_time_list.append(int(str(time_string)[11:13]))
    article_blog_link.append(l.blog_link)

article_date_list = Counter(article_date_list)
article_time_list = Counter(article_time_list)
article_blog_link_list = Counter(article_blog_link)

article_blog_link_other_list = []
count = 0
article_blog_link_final_list = dict()
for k in article_blog_link_list.keys():
    v = article_blog_link_list.get(k)
    if v <= 10:
        count += v
    else:
        article_blog_link_final_list[k] = v


def dict2list(dic: dict):
    keys = dic.keys()
    vals = dic.values()
    lst = [(key, val) for key, val in zip(keys, vals)]
    return lst


article_blog_link_final_list = sorted(dict2list(article_blog_link_final_list), key=lambda x: x[1])
print(article_blog_link_final_list)
article_blog_link_final_list = dict(article_blog_link_final_list)
article_blog_link_final_list["other"] = count
article_blog_link_list = article_blog_link_final_list
x_time = [k for k in article_date_list.keys()]
x = [k for k in reversed(x_time)]
y_count = [v for v in article_date_list.values()]
y = [v for v in reversed(y_count)]

article_time_list = sorted(dict2list(article_time_list), key=lambda x: x[0])
article_time_list = dict(article_time_list)
time_x = [k for k in article_time_list.keys()]
time_y = [v for v in article_time_list.values()]


blog_link_x = [k for k in article_blog_link_list.keys()]
blog_link_y = [v for v in article_blog_link_list.values()]

plt.figure(figsize=(200, 100))
plt.title("Saved Article Statistics by month")
plt.xlabel('Date of saved article')
plt.ylabel('Article Account')
plt.plot(x, y, 'g', linewidth=2, )
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
# plt.show()

plt.figure(figsize=(200, 100))
plt.title("Saved Article Statistics by hours")
plt.xlabel('Time of saved article')
plt.ylabel('Article Account')
plt.plot(time_x, time_y, 'r', linewidth=2, )
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.xticks(np.arange(min(time_x), max(time_x) + 1, 1.0))
# plt.show()

plt.figure(figsize=(200, 100))
plt.title("Saved Article Statistics by website")
plt.xlabel('the website of article source')
plt.ylabel('Article Number')
plt.plot(blog_link_x, blog_link_y, 'r', linewidth=2, )
plt.grid(True)
plt.legend()
plt.xticks(range(len(blog_link_x)), blog_link_x, rotation=90)
plt.show()
