from db import execute, fetch


class Skill:
    def __init__(self, uid: int, skill_list: list):
        self.id = uid
        self.skill_list = skill_list

    def update(self, index, skill_name):
        if skill_name != self.skill_list[index]:
            execute('DELETE FROM skill_table WHERE student_id = %s AND skill_name = %s',
                    (self.id, self.skill_list[index]))
            if skill_name not in self.skill_list:
                execute('INSERT INTO skill_table VALUES (%s, %s)', (self.id, skill_name))
                self.skill_list[index] = skill_name
            else:
                del self.skill_list[index]

    def delete(self, index):
        execute('DELETE FROM skill_table WHERE student_id = %s AND skill_name = %s', (self.id, self.skill_list[index]))
        del self.skill_list[index]

    def add(self, skill_name):
        if skill_name not in self.skill_list:
            execute('INSERT INTO skill_table VALUES (%s, %s)', (self.id, skill_name))
            self.skill_list.append(skill_name)

    @staticmethod
    def load(uid: int):
        execute('SELECT * FROM skill_table WHERE student_id = %s', (uid,))
        data = fetch()
        if len(data) == 0:
            return Skill(uid, [])
        skill_list = [entry['skill_name'] for entry in data]
        return Skill(uid, skill_list)
