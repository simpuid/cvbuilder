from db import execute, commit


class Student(FlaskForm):
    def __init__(self, uid, name, phone, email, dob, branch, minor, year):
        self.id = uid
        self.name = name
        self.phone = phone
        self.email = email
        self.dob = dob
        self.branch = branch
        self.minor = minor
        self.year = year

    def save(self):
        execute('INSERT INTO student_table'
                'VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
                'ON DUPLICATE KEY UPDATE'
                'student_id = VALUES(student_id),'
                'student_name = VALUES(student_name),'
                'student_phone = VALUES(student_phone),'
                'student_email = VALUES(student_email),'
                'student_dob = VALUES(student_dob),'
                'student_branch = VALUES(student_branch),'
                'student_minor = VALUES(student_minor),'
                'student_year = VALUES(student_year)',
                (self.id, self.name, self.phone, self.email, self.dob, self.branch, self.minor, self.year))
