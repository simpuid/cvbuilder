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
        execute('INSERT INTO app_user VALUES (%s, %s)'
                'ON DUPLICATE KEY UPDATE id = VALUES(id), hash = VALUES(hash)', (self.id, self.hash))

    def delete(self):
        execute('DELETE FROM app_user WHERE client.id = %s', (self.id,))

    @staticmethod
    def load(uid):
        execute('SELECT * FROM app_user WHERE id = %s', (uid,))
        data = fetch()
        if len(data) == 0:
            return None
        return User(data[0]['id'], data[0]['hash'])


def populate_users():
    for i in range(18114000, 18114084 + 1):
        if User.load(i) is None:
            user = User(i)
            user.set_password(f'{i}')
            user.apply()
    commit()
