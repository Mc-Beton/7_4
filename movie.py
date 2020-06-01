# Define classes
class Movie:
    def __init__(self, title, year, typ):
        self.title = title
        self.year = year
        self.typ = typ

        #variables
        self._current_views = 0

    def play(self, step=1):
        self.current_views += step

    def __str__(self):
        return f"{self.title}, {self.year}, {self.typ}"

    @property
    def current_views(self):
        return self._current_views
    
    @current_views.setter
    def current_views(self, value):
        self._current_views = value