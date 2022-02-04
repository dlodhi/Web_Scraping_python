from bs4 import BeautifulSoup

with open("home.html", "r") as htmlfile:
    content = htmlfile.read()

    soup = BeautifulSoup(content, features="html.parser")
    #print(soup.prettify())


    Courses_html_tags = soup.findAll("h5" )

   #print(Courses_html_tags)
#    for course in Courses_html_tags:
 #      print(course.text)

    course_card = soup.findAll("div", class_='card')
    for course in course_card:
        coursename  = course.h5.text
        price =course.a.text.split()[-1]
        print(coursename , price)

