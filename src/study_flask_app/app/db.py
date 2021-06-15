from flask_login import UserMixin
from werkzeug.security import generate_password_hash


class User(UserMixin):
    _id = 0

    def __init__(self, name, email, password):
        User._id += 1
        self.id = User._id
        self.name = name
        self.email = email
        self.password = User.generate_password_hash(password)

    @staticmethod
    def generate_password_hash(password):
        return generate_password_hash(password, method='sha256')

    def __repr__(self):
        return f"{self.id}:{self.name}:{self.email}:{self.password}"

