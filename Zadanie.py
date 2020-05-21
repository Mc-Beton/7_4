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
        return f"{self.title}, {self.year}"

class Series(Movie):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title} S{self.season}E{self.episode}"
    

Pulp = Movie(title = "Pulp Fiction", year = "1994", typ = "kryminał")
Cher = Series(title = "Cherobyl", year = "2019", typ = "Dramat", season = "01", episode = "03")

base_list = []
base_list.append(Pulp)
base_list.append(Cher)

for i in base_list:
    print(i)



        