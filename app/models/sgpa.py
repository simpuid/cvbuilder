from typing import List

from db import execute, fetch


class SGPA:
    def __init__(self, uid: int, sg_list: List[dict]):
        self.id = uid
        self.sg_list = sg_list

    def update(self, index, sg_dict):
        if sg_dict['semester'] != self.sg_list[index]['semester']:
            self.delete(index)
        self.add(sg_dict)

    def delete(self, index):
        execute("""DELETE FROM sgpa_table
                            WHERE student_id = %s AND
                            sgpa_semester = %s""",
                (self.id, self.sg_list[index]['semester']))

    def add(self, sg_dict):
        execute("""INSERT INTO sgpa_table
                                VALUES (%s, %s, %s)
                                ON DUPLICATE KEY UPDATE
                                student_id = VALUES(student_id),
                                sgpa_semester = VALUES(sgpa_semester),
                                sgpa_value = VALUES(sgpa_value)""",
                (self.id, sg_dict['semester'], sg_dict['value']))

    @staticmethod
    def load(uid: int):
        execute('SELECT * FROM sgpa_table WHERE student_id = %s', (uid,))
        data = fetch()
        if len(data) == 0:
            return SGPA(uid, [])
        entry_list = []
        for entry in data:
            entry_dict = {
                'semester': entry['sgpa_semester'],
                'value': entry['sgpa_value'],
            }
            entry_list.append(entry_dict)
        return SGPA(uid, entry_list)
