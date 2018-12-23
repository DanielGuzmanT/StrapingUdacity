from Classes.Constants import *
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


def get_state(course):
    state = course.find("span", class_=STATE_COURSE)
    if state is None:
        return "Active"
    return state.contents[0]


def get_category(course):
    category = course.find("h4", class_=CATEGORY)
    if category is None:
        return "No-category"
    return category.contents[0]


def get_title(course):
    title_head = course.find("h3", class_=TITLE_HEAD)
    return title_head.text


def get_skills(skills_tag):
    # skills covered:
    skills = skills_tag.find("span", LIST_SKILLS)
    if skills is None:
        return "no-skills required"
    return skills.text


def get_colaborators(collaborators_tag):
    collaborators = collaborators_tag.find("span", LIST_COLLAB)
    if collaborators is None:
        return "no-collaborators"
    return collaborators.text


def get_level(level_tag):
    level = level_tag.find("span", LEVEL_TEXT)
    return level.text


def get_extra_data(course):
    data = {}
    data_block = course.find("div", class_=DATA)

    # (skills_tag, colaborators_tag, level_tag)
    skills_tag = data_block.find("div", SKILLS)
    colaborators_tag = data_block.find("div", COLLABORATORS)
    level_tag = data_block.find("div", LEVEL)

    data[SKILLS_KEY] = get_skills(skills_tag) if (skills_tag is not None) else "no-skills required"
    data[COLLAB_KEY] = get_colaborators(colaborators_tag) if (colaborators_tag is not None) else "no-collaborators"
    data[LEVEL_KEY] = get_level(level_tag)
    return data


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
