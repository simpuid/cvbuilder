from flask import render_template, Blueprint
from flask_login import current_user, login_required
from models import *
from pylatex import Document, Section, Command, Itemize, Tabu, Center,Subsection

from pylatex.utils import  bold


blueprint = Blueprint('md', __name__)

@blueprint.route('/md')
@login_required
def md():
    geometry_options = {
        "head": "40pt",
        "margin": "0.5in",
        "bottom": "0.6in",
        "includeheadfoot": False

    }
    student = Student.load(current_user.id)
    tenth = Tenth.load(current_user.id)
    twelfth = Twelfth.load(current_user.id)
    skill = Skill.load(current_user.id)
    achievement=Achievement.load(current_user.id)
    extracurr=ExtraCurricular.load(current_user.id)


    doc = Document('report',geometry_options=geometry_options)

    if student is not None:
        with doc.create(Section(student.name,numbering=False)):
            doc.append('Date of Birth : ' + str(student.dob) + '\n')
            doc.append('Branch : ' + student.branch + '\n')
            doc.append('Minor : ' + student.minor + '\n')
            doc.append('College Year : ' + str(student.year) + '\n')
            doc.append('Phone No : ' + str(student.phone) + '\n')
            doc.append('Email : ' + student.email + '\n')
    if tenth or twelfth is not None:
        with doc.create(Section('__________Educational Detail : ',numbering=False)):
            page="hello"
        fmt = "X[r] X[r] X[r] X[r] X[r] "
        with doc.create(Center()) as centered:
            with centered.create(Tabu(fmt,booktabs=True, spread="2in")) as data_table:
                header_row1 = ["Class", "Year", "Board/Degree", "Institution", "CGPA"]
                data_table.add_row(header_row1, mapper=[bold])
                data_table.add_hline()
                if twelfth is not None:
                    data_table.add_row(["12",str(twelfth.year),twelfth.board,twelfth.school_name,str(twelfth.cgpa)])
                if tenth is not None:
                    data_table.add_row(["10",str(tenth.year),tenth.board,tenth.school_name,str(tenth.cgpa)])



    if skill is not None:
        with doc.create(Section('__________Skills : ',numbering=False)):
            with doc.create(Itemize()) as itemize:
                for i in skill.skill_list:
                    itemize.add_item(i)
                itemize.append(Command("ldots"))
    if achievement is not None:
        with doc.create(Section('__________Achievements : ',numbering=False)):
            with doc.create(Itemize()) as itemize:
                for i in achievement.achievement_list:
                    itemize.add_item(i)
                itemize.append(Command("ldots"))
    if extracurr is not None:
        with doc.create(Section('__________Extracurricula Activities :  ', numbering=False)):
            for i in extracurr.ec_list:
                with doc.create(Subsection(i["title"]+'\t'+str(i["start"])+"-"+str(i["end"]),numbering=False)):
                    doc.append(i["text_description"])








    doc.generate_pdf("output/resume",clean_tex=True)


    return render_template("404_error.html")