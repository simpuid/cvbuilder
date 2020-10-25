from typing import List

from db import execute, fetch


class Language:
    def __init__(self, uid: int, language_list: List[dict]):
        self.id = uid
        self.language_list = language_list

    def update(self, index, language_dict):
        if language_dict['language_name'] != self.language_list[index]['language_name']:
            self.delete(index)
        self.add(language_dict)

    def delete(self, index):
        execute('DELETE FROM language_table WHERE student_id = %s AND language_name = %s',
                (self.id, self.language_list[index]['language_name']))

    def add(self, language_dict):
        execute("""INSERT INTO language_table
                                VALUES (%s, %s, %s, %s, %s)
                                ON DUPLICATE KEY UPDATE
                                student_id = VALUES(student_id),
                                language_name = VALUES(language_name),
                                speaking = VALUES(speaking),
                                reading = VALUES(reading),
                                writing = VALUES(writing)""",
                (self.id, language_dict['language_name'], language_dict['speaking'], language_dict['reading'],
                 language_dict['writing']))

    @staticmethod
    def load(uid: int):
        execute('SELECT * FROM language_table WHERE student_id = %s', (uid,))
        data = fetch()
        if len(data) == 0:
            return Language(uid, [])
        entry_list = []
        for entry in data:
            entry_dict = {
                'language_name': entry['language_name'],
                'speaking': entry['speaking'],
                'reading': entry['reading'],
                'writing': entry['writing']
            }
            entry_list.append(entry_dict)
        return Language(uid, entry_list)
