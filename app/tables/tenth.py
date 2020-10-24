from db import execute, fetch


class Tenth:
    def __init__(self, uid: int, school_name: str, cgpa: str, board: str, year: str):
        self.id = uid
        self.school_name = school_name
        self.cgpa = cgpa
        self.board = board
        self.year = year

    def save(self):
        execute("""INSERT INTO tenth_table
                VALUES (%s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                student_id = VALUES(student_id),
                tenth_school_name = VALUES(tenth_school_name),
                tenth_cgpa = VALUES(tenth_cgpa),
                tenth_board = VALUES(tenth_board),
                tenth_year = VALUES(tenth_year)""",
                (self.id, self.school_name, self.cgpa, self.board, self.year))

    @staticmethod
    def load(uid: int):
        execute('SELECT * FROM tenth_table WHERE student_id = %s', (uid,))
        data = fetch()
        if len(data) == 0:
            return None
        return Tenth(
            data[0]['student_id'],
            data[0]['tenth_school_name'],
            data[0]['tenth_cgpa'],
            data[0]['tenth_board'],
            data[0]['tenth_year'],
        )
