from movie import Movie
from series import Series

base_list = []
class Library(Series, Movie):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        

    def add_movie(self):
        i = input("What is the title? ")
        j = input("What year was it made? ")
        k = input("What type of movie is it? ")
        base_list.append(Movie(title = i, year = j, typ = k))
    
    def add_series(self):
        i = input("What is the title? ")
        j = input("What year was it made? ")
        k = input("What type of movie is it? ")
        l = int(input("How many seasons does it have? "))
        for s in range(l):
            m = int(input(f"How many episodes does season {s+1} have? "))
            for e in range(m):
                base_list.append(Series(title = i, year = j, typ = k, season = str(s+1), episode = str(e+1)))
