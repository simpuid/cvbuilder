from typing import List

from db import execute, fetch


class Reference:
    def __init__(self, uid: int, ref_list: List[dict]):
        self.id = uid
        self.ref_list = ref_list

    def update(self, index, ref_dict):
        if ref_dict['student_id'] != self.ref_list[index]['student_id'] or ref_dict['professor_email'] != \
                self.ref_list[index]['professor_email']:
            self.delete(index)
        self.add(ref_dict)

    def delete(self, index):
        execute("""DELETE FROM reference_table
                            WHERE student_id = %s AND
                            professor_email = %s""",
                (self.id, self.ref_list[index]['student_id'], self.ref_list[index]['professor_email']))

    def add(self, ref_list):
        execute("""INSERT INTO reference_table
                                VALUES (%s, %s)
                                ON DUPLICATE KEY UPDATE
                                student_id = VALUES(student_id),
                                professor_email = VALUES(professor_email)""",
                (self.id, ref_list['student_id'], ref_list['professor_email']))

    @staticmethod
    def load(uid: int):
        execute('SELECT * FROM reference_table WHERE student_id = %s', (uid,))
        data = fetch()
        if len(data) == 0:
            return Reference(uid, [])
        entry_list = []
        for entry in data:
            entry_dict = {
                'student_id': entry['student_id'],
                'professor_email': entry['professor_email'],
            }
            entry_list.append(entry_dict)
        return Reference(uid, entry_list)
