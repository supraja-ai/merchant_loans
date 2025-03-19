from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, username):
        super().__init__()
        self.username = username
        self.id = username
