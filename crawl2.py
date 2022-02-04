import time

from bs4 import BeautifulSoup
import requests
import  time
html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text


#print(html_text)
print("skills you dont know")
unfamiliar_skills =input(">")
print(f''' filtering out{unfamiliar_skills}
    ''')



def find_jobs():
    soup = BeautifulSoup(html_text, features="html.parser")
    jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")

    # compname   = jobs.h3.text
    # print(compname)

    for index,job in enumerate(jobs):
        job_published_date = job.find('span', class_='sim-posted').span.text.strip()
        if 'few' in job_published_date:
            compname = job.find('h3', class_="joblist-comp-name").text.strip()
            skills = job.find('span', class_="srp-skills").text.strip()

            more_info = job.header.h2.a['href']

    # print(compname.strip())
    # print(skills.strip())
            if unfamiliar_skills not in skills:
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f''' 
                         company name : {compname} 
                         Required skills : {skills}
                         more info : {more_info}
                         date : {job_published_date}
                         
                             ''')
                    print(f'''company name : {compname} 
                         Required skills : {skills}
                         more info : {more_info}
                         date : {job_published_date}''')
                    print(f'File saved : {index}')



if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait =1
        print(f"waiting {time_wait}  minutes.....")
        time.sleep(time_wait*60)
