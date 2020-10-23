from werkzeug.security import generate_password_hash, check_password_hash
from db import execute, fetch, commit
from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, uid: int, phash: str = ''):
        self.id = uid
        self.hash = phash

    def set_password(self, password):
        self.hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hash, password)

    def apply(self):
        execute('INSERT INTO credential_table VALUES (%s, %s)'
                'ON DUPLICATE KEY UPDATE student_id = VALUES(student_id), hash = VALUES(hash)',
                (self.id, self.hash))

    def delete(self):
        execute('DELETE FROM credential_table WHERE student_id = %s', (self.id,))

    @staticmethod
    def load(uid):
        execute('SELECT * FROM credential_table WHERE student_id = %s', (uid,))
        data = fetch()
        if len(data) == 0:
            return None
        return User(data[0]['student_id'], data[0]['hash'])


def populate_users():
    for i in range(18114000, 18114084 + 1):
        if User.load(i) is None:
            user = User(i)
            user.set_password(f'{i}')
            user.apply()
    commit()
