from app.home.models.Home import Home

class HomeController():
    def __init__(self):
        self.home = Home()

    def get_home(self):
        return self.home.get_home()