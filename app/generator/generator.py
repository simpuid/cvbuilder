from jinja2 import FileSystemLoader, Environment
import os
from flask_login import current_user
from models import *

latex_jinja_env = Environment(
    block_start_string=r'\BLOCK{',
    block_end_string='}',
    variable_start_string=r'\VAR{',
    variable_end_string='}',
    comment_start_string=r'\#{',
    comment_end_string='}',
    line_statement_prefix='%% ',
    line_comment_prefix='%# ',
    trim_blocks=True,
    autoescape=False,
    loader=FileSystemLoader(os.path.abspath('.'))
)


def render_latex(uid: int):
    student = Student.load(current_user.id)
    tenth = Tenth.load(current_user.id)
    twelfth = Twelfth.load(current_user.id)
    sgpa = SGPA.load(current_user.id)
    skill = Skill.load(current_user.id)
    language = Language.load(current_user.id)
    achievement = Achievement.load(current_user.id)
    extra_curr = ExtraCurricular.load(current_user.id)
    intern = Internship.load(current_user.id)
    reference = Reference.load(current_user.id)
    project = Project.load(current_user.id)

    data = {}
    if student is not None:
        data['student'] = student
    if tenth is not None:
        data['tenth'] = tenth
    if twelfth is not None:
        data['twelfth'] = twelfth
    if len(sgpa.sg_list) is not 0:
        data['sgpa'] = sgpa.sg_list
    if len(skill.skill_list) is not 0:
        data['skill'] = skill.skill_list
    if len(language.language_list) is not 0:
        data['language'] = language.language_list
    if len(achievement.achievement_list) is not 0:
        data['achievement'] = achievement.achievement_list
    if len(extra_curr.ec_list) is not 0:
        data['extra_curr'] = extra_curr.ec_list
    if len(intern.intern_list) is not 0:
        data['intern'] = intern.intern_list

    professor = {}
    for email in reference.ref_list:
        if email not in professor:
            professor[email] = Professor.load(email)
    for proj in project.project_list:
        for email in proj['professor_list']:
            if email not in professor:
                professor[email] = Professor.load(email)

    data['professor'] = professor
    data['reference'] = reference.ref_list
    data['project'] = project.project_list
    data['id'] = uid

    template = latex_jinja_env.get_template('generator/CV.tex')
    return template.render(data)
