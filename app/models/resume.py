from db import execute, fetch


class Resume:
    def __init__(self, uid: int, data):
        self.id = uid
        self.data = data

    def save(self):
        execute("""INSERT INTO resume_table
                VALUES (%s, %s)
                ON DUPLICATE KEY UPDATE
                student_id = VALUES(student_id),
                resume_data = VALUES(resume_data)""",
                (self.id, self.data))

    @staticmethod
    def load(uid: int):
        execute('SELECT * FROM resume_table WHERE student_id = %s', (uid,))
        data = fetch()
        if len(data) == 0:
            return None
        return Resume(
            data[0]['student_id'],
            data[0]['resume_data'],
        )
