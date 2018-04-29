import re
from collections import Counter

from bs4 import BeautifulSoup

from company_recruit import RecruitInfo
import matplotlib.pyplot as plot

web_site_home_url = 'https://www.zhipin.com'
text = str()
with open("/home/xuwanjin/Downloads/job_all_list.html", 'r') as f:
    text = str(f.read())

soup_page = BeautifulSoup(text, 'html.parser')
result = soup_page.findAll(attrs={'class': 'job-primary'})


def parse_job_list(jobs_list):
    soup = BeautifulSoup(str(jobs_list), 'html.parser')
    job_title_result = soup.find(attrs={'class', 'job-title'})
    salary_result = soup.find(attrs={'class', 'red'})
    company_name_result = soup.select('div.info-company div.company-text h3.name')
    hr_info_result = soup.select('div.info-publis h3.name')
    other_info_result = soup.select('p')
    job_title = re.match(r'(.*)>(.*)<', str(job_title_result), re.MULTILINE | re.IGNORECASE)
    job_title = job_title.groups()[1]
    pattern = r'(.*)>(.*)</'
    salary_result = re.match(pattern, str(salary_result), re.MULTILINE | re.IGNORECASE)
    link_result = soup.select('a')
    link_result_str = str(link_result).replace('\n', '')
    pattern = r'(.*)<a href=\"(.*?)\" ka='
    link_result_list = re.match(pattern, link_result_str, re.MULTILINE | re.IGNORECASE)
    company_detail_link = link_result_list.groups()[1]
    company_detail_link = '{}{}'.format(web_site_home_url, company_detail_link)
    pattern = r'(.*)search\" href=\"(.*?)\" ka='
    job_detail_result = re.match(pattern, link_result_str, re.MULTILINE | re.IGNORECASE)
    job_detail_link = job_detail_result.groups()[1]
    job_detail_link = '{}{}'.format(web_site_home_url, job_detail_link)
    salary_result = salary_result.groups()[1]
    company_name_result = str(company_name_result[0]).replace('\n', '')
    pattern = r'(.*)target=\"_blank\">(.*)</a'
    company_name = re.match(pattern, company_name_result, re.MULTILINE | re.IGNORECASE)
    company_name = company_name.groups()[1]
    hr_info_result = str(hr_info_result).replace('\n', '')
    pattern = r'(.*)/>(.*)<em class='
    hr_info = re.match(pattern, hr_info_result, re.MULTILINE | re.IGNORECASE)
    hr_info_name = str(hr_info.groups()[1]).replace(' ', '')
    other_info_result_base = str(other_info_result[0]).replace("\n", '').replace('  ', '')
    pattern = r'(.*?)>(.*?)<'

    other_info = re.findall(pattern, other_info_result_base)
    site = other_info[0][-1]
    experiences = other_info[2][-1]
    education = other_info[-1][-1]

    company_other_info = str(other_info_result[1]).replace('\n', '').replace('  ', '')

    company_tag = re.findall(pattern, company_other_info)[0][-1]
    serial_round = re.findall(pattern, company_other_info)[2][-1]
    num_employee = re.findall(pattern, company_other_info)[-1][-1]

    date = other_info_result[2]
    release_date = re.findall(pattern, str(date))[-1][-1]
    recruit_instance = \
        RecruitInfo(job_title=job_title, salary=salary_result, site=site, education=education,
                    company_name=company_name, financing=serial_round, num_employee=num_employee,
                    release_date=release_date, experiences=experiences, tag=company_tag,
                    hr_name=hr_info_name, job_detail_link=job_detail_link, company_detail_link=company_detail_link)
    return recruit_instance


job_instances = map(parse_job_list, result)
print(parse_job_list(result[0]))
# num_employee = list()
# for job in job_instances:
#     num_employee.append(job.num_employee)
#
# num_employee_list = dict(Counter(num_employee))
# num_employee_list = sorted(num_employee_list.items(), key=lambda item: item[0])
# x = [num_employee_list[i][1] for i in range(len(num_employee_list))]
# # print(x)
# y = [num_employee_list[i][0] for i in range(len(num_employee_list))]
# # print(y)
# plot.figure(figsize=(200, 100))
# plot.title("employee of Company")
# plot.plot(y, x, 'r', linewidth=2)
# plot.xlabel("the scale of Company")
# plot.ylabel("the number of company")
# plot.show()
