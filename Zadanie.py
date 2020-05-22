import random
import itertools


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
        return f"{self.title}, {self.year}"

    @property
    def current_views(self):
        return self._current_views
    
    @current_views.setter
    def current_views(self, value):
        self._current_views = value


class Series(Movie):
    def __init__(self, season, episode, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.season = season
        self.episode = episode

    def __str__(self):
        return f"{self.title} S{self.season}E{self.episode}"
    
# Define the elements of base_list    
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

# Function to print objects from class only Movie
def get_movies(a):
    list_to_sort = [i for i in a if i.__class__.__name__ == 'Movie']
    list_to_sort = sorted(list_to_sort, key=lambda Movie: Movie.title)
    for i in list_to_sort:
        print(i)

# Function to print objects from class only Series       
def get_series(a):
    list_to_sort = [i for i in a if i.__class__.__name__ == 'Series']
    list_to_sort = sorted(list_to_sort, key=lambda Series: Series.title)
    for i in list_to_sort:
        print(i)

# Search function
def search(a, name):
    for i in a:
        if str(i.title) == name:
            print(i)



# decorator for generating views
def generate_multi(func):
    def wrap(*args):
        for i in range(11):
            func(*args)
            
    return wrap


# Generate random views
@generate_multi
def generate_views(a):
    i = random.choice(a)
    j = random.choice(range(101))
    i.play(j)
    #print(i)
    #print(i.current_views)

generate_views(base_list)


# print out the top title by views
def top_titles(a, amount, content_type):
    top = [i for i in a if i.__class__.__name__ == content_type.__name__]
    top = sorted(top, key=lambda content_type: content_type.current_views, reverse=True)
    n=0
    for i in top:
        print(f"{i}, views = {i.current_views}")
        n=n+1
        if n == amount:
            break

top_titles(base_list, 2, Movie)


    





        