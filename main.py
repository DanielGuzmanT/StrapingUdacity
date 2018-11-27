import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.udacity.com/courses/all")
soup = BeautifulSoup(page.content, 'html.parser')

# [<class 'bs4.element.Doctype'>, <class 'bs4.element.Tag'>]
html = list(soup.children)[1]

# [<class 'bs4.element.Tag'>, <class 'bs4.element.NavigableString'>, <class 'bs4.element.Tag'>]
body = list(html.children)[2]

file = open("UdacityCourses.html", "w")
file.write(body.prettify())
file.close()

ir_course_card_catalog = html.find("ir-course-card-catalog")
file = open("UdacityCoursesCatalog.html","w")
file.write(ir_course_card_catalog.prettify())
file.close()
