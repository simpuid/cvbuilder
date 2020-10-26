from typing import List

from db import execute, fetch


class ExtraCurricular:
    def __init__(self, uid: int, ec_list: List[dict]):
        self.id = uid
        self.ec_list = ec_list

    def update(self, index, ec_dict):
        if ec_dict['title'] != self.ec_list[index]['title'] or ec_dict['start'] != self.ec_list[index]['start'] or \
                ec_dict['end'] != self.ec_list[index]['end']:
            self.delete(index)
        self.add(ec_dict)

    def delete(self, index):
        execute("""DELETE FROM extra_curricular_table
                            WHERE student_id = %s AND
                            extra_curricular_title = %s AND
                            extra_curricular_start_date = %s AND
                            extra_curricular_end_date = %s""",
                (self.id, self.ec_list[index]['title'], self.ec_list[index]['start'], self.ec_list[index]['end']))

    def add(self, ec_list):
        execute("""INSERT INTO extra_curricular_table
                                VALUES (%s, %s, %s, %s, %s)
                                ON DUPLICATE KEY UPDATE
                                student_id = VALUES(student_id),
                                extra_curricular_title = VALUES(extra_curricular_title),
                                extra_curricular_start_date = VALUES(extra_curricular_start_date),
                                extra_curricular_end_date = VALUES(extra_curricular_end_date),
                                extra_curricular_description = VALUES(extra_curricular_description)""",
                (self.id, ec_list['title'], ec_list['start'], ec_list['end'],
                 ec_list['text_description']))

    @staticmethod
    def load(uid: int):
        execute('SELECT * FROM extra_curricular_table WHERE student_id = %s', (uid,))
        data = fetch()
        if len(data) == 0:
            return ExtraCurricular(uid, [])
        entry_list = []
        for entry in data:
            entry_dict = {
                'title': entry['extra_curricular_title'],
                'start': entry['extra_curricular_start_date'],
                'end': entry['extra_curricular_end_date'],
                'text_description': entry['extra_curricular_description']
            }
            entry_list.append(entry_dict)
        return ExtraCurricular(uid, entry_list)
