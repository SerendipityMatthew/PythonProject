import requests
import time
from bs4 import BeautifulSoup

"""
    https://www.zhipin.com/job_detail/?query=&scity=101020100&industry=&position=100109    上海python
    https://www.zhipin.com/job_detail/?query=&scity=101020100&industry=&position=100101    上海Java
    https://www.zhipin.com/job_detail/?query=&scity=101010100&industry=&position=100109    北京Python
    https://www.zhipin.com/job_detail/?query=&scity=101010100&industry=&position=100101    北京Java
    https://www.zhipin.com/job_detail/?query=&scity=101190100&industry=&position=100109    南京Python
    https://www.zhipin.com/job_detail/?query=&scity=101190100&industry=&position=100101    南京Java
    https://www.zhipin.com/job_detail/?query=&scity=101210100&industry=&position=100109    杭州Python
    https://www.zhipin.com/job_detail/?query=&scity=101210100&industry=&position=100101    杭州Java
    
    北京, 上海, 杭州, 深圳, 广州, 南京, 苏州
"""

from parse_html import parse_job_list

url_other = 'https://www.zhipin.com/c101020100-p100109/?page=%s&ka=page-%s'
headers = {
    'Referer': 'https://www.zhipin.com/',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.18 Safari/537.36'
}
url_list = list()
for i in range(1, 4):
    url = url_other % (i, i)
    url_list.append(url)


def request_url(url):
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf8'
    time.sleep(2)
    soup = BeautifulSoup(response.text, 'html.parser')
    result = soup.findAll(attrs={'class': 'job-primary'})
    return result


request_list = map(request_url, url_list)

all_job_list = []
for r in request_list:
    all_job_list.extend(r)
print(len(all_job_list))
job_result = map(parse_job_list, all_job_list)
for x in job_result:
    print(x)
