from app.users.models.User import User

class UserController():
    def __init__(self):
        self.users = User()

    def get_users(self):
        return self.users.get_users()