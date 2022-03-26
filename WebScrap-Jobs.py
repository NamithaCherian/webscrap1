import requests
from bs4 import BeautifulSoup 
import time



def find_jobs():
    url='https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation='

    html_text=requests.get(url).text
    soup=BeautifulSoup(html_text,'lxml')

    jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')

    for job in jobs:
        published_date=job.find('span',class_='sim-posted').span.text

        if 'few' in published_date:
            company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
            skills=job.find('span',class_='srp-skills').text.replace(' ','')
            more_info=job.header.h2.a['href']
            location=job.find('ul',class_='top-jd-dtl clearfix').span['title']
            print(f'Company Name: {company_name.strip()}')
            print(f'Location: {location}')
            print(f'Skills: {skills.strip()}')
            print(f'More Information: {more_info}')
            print('')


if __name__=='__main__':
    while True:
        find_jobs()
        time_wait_in_min=10
        print(f'Waiting {time_wait_in_min} minutes...')
        time.sleep(time_wait_in_min*60)
