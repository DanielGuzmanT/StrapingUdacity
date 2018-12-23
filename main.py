from Classes.Course import *
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


def main():
    page = requests.get("https://www.udacity.com/courses/all")
    soup = BeautifulSoup(page.content, 'html.parser')

    # [<class 'bs4.element.Doctype'>, <class 'bs4.element.Tag'>]
    html = list(soup.children)[1]
    # [<class 'bs4.element.Tag'>, <class 'bs4.element.NavigableString'>, <class 'bs4.element.Tag'>]
    body = list(html.children)[2]

    card_list = body.find_all('div', attrs=COURSE_SUMMARY_CARD)
    datos, i = [], 0
    for course in card_list:
        i, extra = i+1, get_extra_data(course)
        dato = [i, get_state(course), get_category(course), get_title(course), extra[LEVEL_KEY], extra[COLLAB_KEY],
                extra[SKILLS_KEY]]
        datos.append(dato)

    titulos = ["N°", "State", "Category", "Course", "Level", "In collaboration with", "Skills covered"]
    tabla = tabulate(datos, titulos, "fancy_grid")

    file = open("cursos.txt", "w")
    file.write(tabla)
    file.write("\n")
    file.close()


if __name__ == '__main__':
    main()
