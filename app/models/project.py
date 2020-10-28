from typing import List

from db import execute, fetch


class Project:
    def __init__(self, uid: int, project_list: List[dict]):
        self.id = uid
        self.project_list = project_list

    def update(self, index, project_dict):
        if project_dict['title'] != self.project_list[index]['title']:
            self.delete(index)
        self.add(project_dict)

    def delete(self, index):
        execute("""DELETE FROM project_table
                            WHERE student_id = %s AND
                            project_title = %s""",
                (self.id, self.project_list[index]['title']))
        execute("""DELETE FROM project_professor_table
                                WHERE student_id = %s AND
                                project_title = %s""",
                (self.id, self.project_list[index]['title']))

    def update_helper(self, project_dict, prof_set):
        execute("""UPDATE project_table 
                        SET 
                            project_description = %s,
                            project_start_date = %s,
                            project_end_date = %s
                        WHERE
                            student_id = %s AND
                            project_title = %s""",
                (project_dict['description'], project_dict['start_date'], project_dict['end_date'], self.id,
                 project_dict['title']))
        for prof in project_dict['professor_list'] - prof_set:
            execute("""INSERT INTO project_professor_table
                                    VALUES (%s, %s, %s)""",
                    (self.id, project_dict['title'], prof))
        for prof in prof_set - project_dict['professor_list']:
            execute("""DELETE FROM project_professor_table
                                        WHERE student_id = %s AND
                                        project_title = %s AND
                                        professor_email = %s""",
                    (self.id, project_dict['title'], prof))

    def add_helper(self, project_dict):
        execute("""INSERT INTO project_table
                                VALUES (%s, %s, %s, %s, %s)""",
                (self.id, project_dict['title'], project_dict['description'], project_dict['start_date'],
                 project_dict['end_date']))
        for prof in project_dict['professor_list']:
            execute("""INSERT INTO project_professor_table
                                    VALUES (%s, %s, %s)""",
                    (self.id, project_dict['title'], prof))

    def add(self, project_dict):
        check = True
        for project in self.project_list:
            if project['title'] == project_dict['title']:
                self.update_helper(project_dict, project['professor_list'])
                check = not check
        if check:
            self.add_helper(project_dict)

    @staticmethod
    def load(uid: int):
        execute('SELECT * FROM project_table WHERE student_id = %s', (uid,))
        data = fetch()
        if len(data) == 0:
            return Project(uid, [])
        entry_list = []
        for entry in data:
            execute('SELECT * FROM project_professor_table WHERE student_id = %s AND project_title = %s',
                    (uid, entry['project_title']))
            prof_data = fetch()
            prof_set = set()
            for prof in prof_data:
                prof_set.add(prof['professor_email'])
            entry_dict = {
                'start_date': entry['project_start_date'],
                'end_date': entry['project_end_date'],
                'title': entry['project_title'],
                'description': entry['project_description'],
                'professor_list': prof_set
            }
            entry_list.append(entry_dict)
        return Project(uid, entry_list)
