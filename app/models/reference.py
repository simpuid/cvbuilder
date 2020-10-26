from db import execute, fetch


class Reference:
    def __init__(self, uid: int, ref_list: list):
        self.id = uid
        self.ref_list = ref_list

    def update(self, index, professor_email):
        if professor_email != self.ref_list[index]:
            self.delete(index)
        self.add(professor_email)

    def delete(self, index):
        execute("""DELETE FROM reference_table
                            WHERE student_id = %s AND
                            professor_email = %s""",
                (self.id, self.ref_list[index]))

    def add(self, professor_email):
        execute("""INSERT INTO reference_table
                                VALUES (%s, %s)
                                ON DUPLICATE KEY UPDATE
                                student_id = VALUES(student_id),
                                professor_email = VALUES(professor_email)""",
                (self.id, professor_email))

    @staticmethod
    def load(uid: int):
        execute('SELECT * FROM reference_table WHERE student_id = %s', (uid,))
        data = fetch()
        if len(data) == 0:
            return Reference(uid, [])
        entry_list = [entry['professor_email'] for entry in data]
        return Reference(uid, entry_list)
