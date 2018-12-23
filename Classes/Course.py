from Constants import *


class Course:
    def __init__(self):
        self.web_page = ''
        # self.state = ''
        # self.category = ''
        # self.name = ''
        # self.skills_covered = []

    def obtain_data(self, course):
        self.state = self._get_state(course)

    @staticmethod
    def _get_state(course):
        state = course.find("span", class_=STATE_COURSE)
        return "Active" if state is None else state.contents[0]

    @staticmethod
    def _get_category(course):
        category = course.find("h4", class_=CATEGORY)
        return "No-category" if category is None else category.contents[0]

    @staticmethod
    def _get_title(course):
        title_head = course.find("h3", class_=TITLE_HEAD)
        return title_head.text

    @staticmethod
    def _get_skills(skills_tag):
        # skills covered:
        skills = skills_tag.find("span", LIST_SKILLS)
        return None if skills is None else skills.text.split(' ')

    @staticmethod
    def _get_colaborators(collaborators_tag):
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
