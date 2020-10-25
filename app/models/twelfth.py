from db import execute, fetch


class Twelfth:
    def __init__(self, uid: int, school_name: str, cgpa: str, board: str, year: str):
        self.id = uid
        self.school_name = school_name
        self.cgpa = cgpa
        self.board = board
        self.year = year

    def save(self):
        execute("""INSERT INTO twelfth_table
                VALUES (%s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                student_id = VALUES(student_id),
                twelfth_school_name = VALUES(twelfth_school_name),
                twelfth_cgpa = VALUES(twelfth_cgpa),
                twelfth_board = VALUES(twelfth_board),
                twelfth_year = VALUES(twelfth_year)""",
                (self.id, self.school_name, self.cgpa, self.board, self.year))

    @staticmethod
    def load(uid: int):
        execute('SELECT * FROM twelfth_table WHERE student_id = %s', (uid,))
        data = fetch()
        if len(data) == 0:
            return None
        return Twelfth(
            data[0]['student_id'],
            data[0]['twelfth_school_name'],
            data[0]['twelfth_cgpa'],
            data[0]['twelfth_board'],
            data[0]['twelfth_year'],
        )