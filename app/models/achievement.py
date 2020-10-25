from db import execute, fetch


class Achievement:
    def __init__(self, uid: int, achievement_list: list):
        self.id = uid
        self.achievement_list = achievement_list

    def update(self, index, achievement_description):
        if achievement_description != self.achievement_list[index]:
            execute('DELETE FROM achievement_table WHERE student_id = %s AND achievement_description = %s',
                    (self.id, self.achievement_list[index]))
            if achievement_description not in self.achievement_list:
                execute('INSERT INTO achievement_table VALUES (%s, %s)', (self.id, achievement_description))
                self.achievement_list[index] = achievement_description
            else:
                del self.achievement_list[index]

    def delete(self, index):
        execute('DELETE FROM achievement_table WHERE student_id = %s AND achievement_description = %s',
                (self.id, self.achievement_list[index]))
        del self.achievement_list[index]

    def add(self, achievement_description):
        if achievement_description not in self.achievement_list:
            execute('INSERT INTO achievement_table VALUES (%s, %s)', (self.id, achievement_description))
            self.achievement_list.append(achievement_description)

    @staticmethod
    def load(uid: int):
        execute('SELECT * FROM achievement_table WHERE student_id = %s', (uid,))
        data = fetch()
        if len(data) == 0:
            return Achievement(uid, [])
        achievement_list = [entry['achievement_description'] for entry in data]
        return Achievement(uid, achievement_list)
