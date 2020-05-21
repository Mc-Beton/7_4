import itertools

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
Aven = Movie(title= "Avengers", year = "2012", typ = "Sci-Fi")
Fri = Series(title = "Friends", year = "1999", typ = "komedia", season = "06", episode = "04")

base_list = []
base_list.append(Pulp)
base_list.append(Cher)
base_list.append(Aven)
base_list.append(Fri)

list_to_sort=[]

def get_movies(a):
    list_to_sort = [i for i in a if i.__class__.__name__ == 'Movie']
    list_to_sort = sorted(list_to_sort, key=lambda Movie: Movie.title)
    for i in list_to_sort:
        print(i)

        

def get_series(a):
    list_to_sort = [i for i in a if i.__class__.__name__ == 'Series']
    list_to_sort = sorted(list_to_sort, key=lambda Series: Series.title)
    for i in list_to_sort:
        print(i)


get_movies(base_list)
get_series(base_list)
    





        