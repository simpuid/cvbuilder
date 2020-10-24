from db import execute, fetch


class Student:
    def __init__(self, uid: int, name: str, phone: str, email: str, dob: str, branch: str, minor: str, year: str):
        self.id = uid
        self.name = name
        self.phone = phone
        self.email = email
        self.dob = dob
        self.branch = branch
        self.minor = minor
        self.year = year

    def save(self):
        execute("""INSERT INTO student_table
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                student_id = VALUES(student_id),
                student_name = VALUES(student_name),
                student_phone = VALUES(student_phone),
                student_email = VALUES(student_email),
                student_dob = VALUES(student_dob),
                student_branch = VALUES(student_branch),
                student_minor = VALUES(student_minor),
                student_year = VALUES(student_year)""",
                (self.id, self.name, self.phone, self.email, self.dob, self.branch, self.minor, self.year))

    @staticmethod
    def load(uid: int):
        execute('SELECT * FROM student_table WHERE student_id = %s', (uid,))
        data = fetch()
        if len(data) == 0:
            return None
        return Student(
            data[0]['student_id'],
            data[0]['student_name'],
            data[0]['student_phone'],
            data[0]['student_email'],
            data[0]['student_dob'],
            data[0]['student_branch'],
            data[0]['student_minor'],
            data[0]['student_year'],
        )
