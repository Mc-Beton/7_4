from movie import Movie
from series import Series

class Library:
    def __init__(self):

        #variables
        self.base_list = []

    def add_movie(self):
        i = input("What is the title ")
        j = input("What year was it made ")
        k = input("What type of movie is it? ")
        self.base_list.append(Movie(title = i, year = j, typ = k))
    
    def add_series(self):
        i = input("What is the title ")
        j = input("What year was it made ")
        k = input("What type of movie is it? ")
        l = int(input("How many seasons does it have? "))
        for s in range(l):
            m = int(input(f"How many episodes does season {s+1} have? "))
            for e in range(m):
                self.base_list.append(Series(title = i, year = j, typ = k, season = str(s+1), episode = str(e+1)))

    @property
    def base_list_content(self):
        return self.base_list
    