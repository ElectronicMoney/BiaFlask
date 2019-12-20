class Home():
    def __init__(self):
        self.home = {}

    def get_home(self):
        self.home = {
            'title': 'Welcome to BiaFlask Blog!',
            'description': 'The BiaFlask is a blogging framework!'
        }
        return self.home