from typing import List

from db import execute, fetch


class Internship:
    def __init__(self, uid: int, intern_list: List[dict]):
        self.id = uid
        self.intern_list = intern_list

    def update(self, index, intern_dict):
        if intern_dict['start_date'] != self.intern_list[index]['start_date'] or intern_dict['end_date'] != \
                self.intern_list[index]['end_date']:
            self.delete(index)
        self.add(intern_dict)

    def delete(self, index):
        execute("""DELETE FROM internship_table
                            WHERE student_id = %s AND
                            internship_start_date = %s AND
                            internship_end_date = %s""",
                (self.id, self.intern_list[index]['start_date'], self.intern_list[index]['end_date']))

    def add(self, intern_list):
        execute("""INSERT INTO internship_table
                                VALUES (%s, %s, %s, %s, %s, %s)
                                ON DUPLICATE KEY UPDATE
                                student_id = VALUES(student_id),
                                internship_start_date = VALUES(internship_start_date),
                                internship_end_date = VALUES(internship_end_date),
                                internship_organization = VALUES(internship_organization),
                                internship_designation = VALUES(internship_designation),
                                internship_description = VALUES(internship_description)""",
                (self.id, intern_list['start_date'], intern_list['end_date'], intern_list['organization'],
                 intern_list['designation'], intern_list['description']))

    @staticmethod
    def load(uid: int):
        execute('SELECT * FROM internship_table WHERE student_id = %s', (uid,))
        data = fetch()
        if len(data) == 0:
            return Internship(uid, [])
        entry_list = []
        for entry in data:
            entry_dict = {
                'start_date': entry['internship_start_date'],
                'end_date': entry['internship_end_date'],
                'organization': entry['internship_organization'],
                'designation': entry['internship_designation'],
                'description': entry['internship_description']
            }
            entry_list.append(entry_dict)
        return Internship(uid, entry_list)
