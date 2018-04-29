import requests
import time
from bs4 import BeautifulSoup

"""
example:https://www.zhipin.com/{industry}{city}{position}/h_101010100/?page=2&ka=page-2  北京, Java, Media
        https://www.zhipin.com/i100003-c101010100-p100101/h_101010100/?page=2&ka=page-2  北京, Java, Media
        https://www.zhipin.com/i100003-c101010100-p100102/h_101010100/?page=2&ka=page-2  北京, C++, Media
        https://www.zhipin.com/i100021-c101010100-p100102/h_101010100/?page=2&ka=page-2  北京, C++, 计算机软件
        https://www.zhipin.com/i100002-c101020100-p100101/h_101020100/?page=2&ka=page-2  上海, Java, 游戏
    
    北京, 上海, 杭州, 深圳, 广州, 南京, 苏州
"""

from parse_html import parse_job_list

url_other = 'https://www.zhipin.com/{industry}{city}{position}/h_101010100/?page={page}&ka=page-{page}'
headers = {
    'Referer': 'https://www.zhipin.com/',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.18 Safari/537.36'
}
url_list = list()
for i in range(1, 4):
    url = url_other.format(industry='', city='c101020100-', position='p100109', page='1')
    url_list.append(url)


def request_url(url):
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf8'
    time.sleep(2)
    soup = BeautifulSoup(response.text, 'html.parser')
    result = soup.findAll(attrs={'class': 'job-primary'})
    return result


# fetch all pages of Python job, each page as a elements
request_list = map(request_url, url_list)
#  all pages of python job should be in a list, then we use the map function
all_job_list = []
for r in request_list:
    all_job_list.extend(r)
print(len(all_job_list))
job_result = map(parse_job_list, all_job_list)
for x in job_result:
    print(x)
