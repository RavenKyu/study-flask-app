from study_flask_app.app.db import User

user_info = [
    ('John', 'john@gmail.com', "123"),
    ('Deokyu', 'deokyu@vivans.net', "456"),
    ('Suyeon', 'suyeon@vivans.net', "789")
]

users = [User(*user) for user in user_info]
