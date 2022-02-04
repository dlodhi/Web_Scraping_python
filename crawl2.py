from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text


#print(html_text)


soup = BeautifulSoup(html_text, features="html.parser")
jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

# compname   = jobs.h3.text
# print(compname)
for job in jobs:
    job_published_date = job.find('span', class_='sim-posted').span.text.strip()
    if 'few' in job_published_date:
        compname = job.find('h3', class_="joblist-comp-name").text.strip()
        skills = job.find('span', class_="srp-skills").text.strip()

# print(compname.strip())
# print(skills.strip())
        print(f''' 
             company name : {compname} 
             Required skills : {skills}
             date : {job_published_date}
             ''')



