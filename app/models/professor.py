from db import fetch, execute, commit


class Professor:
    def __init__(self, uid: int, name: str, department: str, email: str, phone: str):
        self.id = uid
        self.name = name
        self.department = department
        self.email = email
        self.phone = phone

    def save(self):
        execute("""INSERT INTO professor_table
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        professor_id = VALUES(professor_id),
        professor_name = VALUES(professor_name),
        professor_department = VALUES(professor_department),
        professor_email = VALUES(professor_email),
        professor_phone = VALUES(professor_phone)""",
                (self.id, self.name, self.department, self.email, self.phone))

    @staticmethod
    def load(uid: int):
        execute('SELECT * FROM professor_table WHERE professor_id = %s', (uid,))
        data = fetch()
        if len(data) == 0:
            return None
        return Professor(data[0]['professor_id'], data[0]['professor_name'], data[0]['professor_department'],
                         data[0]['professor_email'], data[0]['professor_phone'])


def populate_professors():
    Professor(0, 'Prof A', 'Dept X', 'a@x.org', '9876543210').save()
    Professor(1, 'Prof B', 'Dept X', 'b@x.org', '0123456789').save()
    Professor(2, 'Prof C', 'Dept Y', 'c@y.org', '0246813579').save()
    Professor(3, 'Prof D', 'Dept Y', 'd@y.org', '1032547698').save()
    Professor(4, 'Prof E', 'Dept Z', 'e@z.org', '1122334455').save()
    Professor(5, 'Prof F', 'Dept Z', 'f@z.org', '6942069420').save()
    commit()
