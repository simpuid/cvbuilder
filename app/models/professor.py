from db import fetch, execute, commit


class Professor:
    def __init__(self, email: str, name: str, department: str, phone: str):
        self.email = email
        self.name = name
        self.department = department
        self.phone = phone

    def save(self):
        execute("""INSERT INTO professor_table
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        professor_name = VALUES(professor_name),
        professor_department = VALUES(professor_department),
        professor_email = VALUES(professor_email),
        professor_phone = VALUES(professor_phone)""",
                (self.email, self.name, self.department, self.phone))

    @staticmethod
    def load(uid: int):
        execute('SELECT * FROM professor_table WHERE professor_id = %s', (uid,))
        data = fetch()
        if len(data) == 0:
            return None
        return Professor(data[0]['professor_email'],
                         data[0]['professor_name'],
                         data[0]['professor_department'],
                         data[0]['professor_phone'])


def populate_professors():
    Professor('a@x.org', 'Prof A', 'Dept X', '9876543210').save()
    Professor('b@x.org', 'Prof B', 'Dept X', '0123456789').save()
    Professor('c@y.org', 'Prof C', 'Dept Y', '0246813579').save()
    Professor('d@y.org', 'Prof D', 'Dept Y', '1032547698').save()
    Professor('e@z.org', 'Prof E', 'Dept Z', '1122334455').save()
    Professor('f@z.org', 'Prof F', 'Dept Z', '6942069420').save()
    commit()
