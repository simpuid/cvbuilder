from collections import namedtuple

from flask_login import login_required, current_user
from flask import render_template, Blueprint, flash, redirect, url_for

from forms import ProjectListForm
from models import Project, Professor
from db import commit

blueprint = Blueprint('project', __name__)


@blueprint.route('/project', methods=['GET', 'POST'])
@login_required
def project():
    Entry = namedtuple('Entry', ['title', 'professors', 'start', 'end', 'text_description'])
    project_value = Project.load(current_user.id)
    if project_value.project_list:
        data = {'project_list': []}
        for project_dict in project_value.project_list:
            data['project_list'].append(
                Entry(project_dict['title'], "\n".join(project_dict['professor_list']), project_dict['start_date'],
                      project_dict['end_date'], project_dict['description']))
        form = ProjectListForm(data=data)
    else:
        form = ProjectListForm()
    if form.validate_on_submit():
        if form.add.data:
            if bool(form.title.data) and bool(form.professors.data):
                prof_list = [prof.strip("\r") for prof in form.professors.data.split('\n')]
                if prof_list[-1] == '':
                    del prof_list[-1]
                check = True
                for prof in prof_list:
                    if Professor.load(prof) is None:
                        check = False
                if check:
                    project_dict = {
                        'title': form.title.data,
                        'professor_list': set(prof_list),
                        'start_date': form.start.data,
                        'end_date': form.end.data,
                        'description': form.text_description.data
                    }
                    project_value.add(project_dict)
                    flash('Project added', 'success')
                    commit()
                else:
                    flash('Bad emails', 'danger')
            else:
                flash('Empty field', 'danger')
            return redirect(url_for('project.project'))
        else:
            for index in range(len(form.project_list)):
                if form.project_list[index].save.data:
                    if bool(form.project_list[index].title.data) and bool(
                            form.project_list[index].professors.data):
                        prof_list = [prof.strip("\r") for prof in form.project_list[index].professors.data.split('\n')]
                        if prof_list[-1] == '':
                            del prof_list[-1]
                        check = True
                        for prof in prof_list:
                            if Professor.load(prof) is None:
                                check = False
                        if check:
                            project_dict = {
                                'title': form.project_list[index].title.data,
                                'professor_list': set(prof_list),
                                'start_date': form.project_list[index].start.data,
                                'end_date': form.project_list[index].end.data,
                                'description': form.project_list[index].text_description.data
                            }
                            project_value.update(index, project_dict)
                            commit()
                            flash('Updated successfully', 'success')
                        else:
                            flash('Bad emails', 'danger')
                    else:
                        flash('Empty field', 'danger')
                    return redirect(url_for('project.project'))
                if form.project_list[index].delete.data:
                    project_value.delete(index)
                    commit()
                    flash('Deleted successfully', 'success')
                    return redirect(url_for('project.project'))
    return render_template('project.html', form=form)
