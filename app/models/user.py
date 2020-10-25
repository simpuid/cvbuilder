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

    def save(self):
        execute('INSERT INTO user_table VALUES (%s, %s)'
                'ON DUPLICATE KEY UPDATE user_id = VALUES(user_id), user_hash = VALUES(user_hash)',
                (self.id, self.hash))

    @staticmethod
    def load(uid: int):
        execute('SELECT * FROM user_table WHERE user_id = %s', (uid,))
        data = fetch()
        if len(data) == 0:
            return None
        return User(data[0]['user_id'], data[0]['user_hash'])


def populate_users():
    for i in range(100, 200 + 1):
        user = User(i)
        user.set_password(f'{i}')
        user.save()
    commit()
