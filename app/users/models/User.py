class User():
    def __init__(self):
        self.users = []

    def get_users(self):
        self.users = {
            '1': {'id': 1, 'name': 'Emeka Augustne', 'email': 'emoney@gmail.com'},
            '2': {'id': 2, 'name': 'Ogena Tega', 'email': 'tega@gmail.com'}
        }
        return self.users