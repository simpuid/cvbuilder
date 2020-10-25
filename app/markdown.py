from mdutils.mdutils import MdUtils
from flask import render_template, Blueprint
from flask_login import current_user, login_required
from models import *

blueprint = Blueprint('md', __name__)

@blueprint.route('/md')
@login_required
def md():
    mdfile = MdUtils(file_name='Resume', title='Resume')
    student = Student.load(current_user.id)
    tenth = Tenth.load(current_user.id)
    twelfth = Twelfth.load(current_user.id)
    skill= Skill.load(current_user.id)
    mdfile.new_header(level=1, title='Personal Detail : ')
    if student is not None:
        mdfile.write("Enrollment : " + str(student.id))
        mdfile.write('  \n')
        mdfile.write("Name : " + student.name)
        mdfile.write('  \n')
        mdfile.write("Phone : " + str(student.phone))
        mdfile.write('  \n')
        mdfile.write("Email : " + student.email)
        mdfile.write('  \n')
        mdfile.write("DOB : " + str(student.dob))
        mdfile.write('  \n')
    mdfile.new_header(level=1, title='Educational Detail : ')
    ed_dt = ["Year", "Degree/Board", "Institution", "CGPA"]
    co = 1
    if twelfth is not None:
        ed_dt.extend([str(twelfth.year), twelfth.board, twelfth.school_name, str(twelfth.cgpa)])
        co = co + 1
    if tenth is not None:
        ed_dt.extend([str(tenth.year), tenth.board, tenth.school_name, str(tenth.cgpa)])
        co = co + 1
    mdfile.new_table(columns=4, rows=co, text=ed_dt, text_align='center')
    mdfile.new_header(level=1, title='Skill : ')
    if skill is not None:
        sk_d=skill.skill_list
        mdfile.new_list(items=sk_d,marked_with='1')

    mdfile.new_table_of_contents(table_title='Contents', depth=2)
    mdfile.create_md_file()
    return render_template("404_error.html")