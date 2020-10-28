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
    student=Student.load(current_user.id)
    tenth=Tenth.load(current_user.id)
    twelfth=Twelfth.load(current_user.id)
    sgpa=SGPA.load(current_user.id)
    skill=Skill.load(current_user.id)
    language=Language.load(current_user.id)
    achievement=Achievement.load(current_user.id)
    extra_curr=ExtraCurricular.load(current_user.id)
    intern=Internship.load(current_user.id)
    template = latex_jinja_env.get_template('generator/CV.tex')
    return template.render(intern=intern.intern_list,extra_curr=extra_curr.ec_list,achievement=achievement.achievement_list,language=language.language_list,student=student,tenth=tenth,twelfth=twelfth,sgpa=sgpa.sg_list,skill=skill.skill_list, id=uid)
