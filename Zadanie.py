import random
import itertools
from movie import Movie
from series import Series


    
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
def get_movies():
    list_to_sort = [i for i in base_list if i.__class__.__name__ == 'Movie']
    list_to_sort = sorted(list_to_sort, key=lambda Movie: Movie.title)
    for i in list_to_sort:
        print(i)

# Function to print objects from class only Series       
def get_series():
    list_to_sort = [i for i in base_list if i.__class__.__name__ == 'Series']
    list_to_sort = sorted(list_to_sort, key=lambda Series: Series.title)
    for i in list_to_sort:
        print(i)

search_list=[]
# Search function
def search(name):
    for i in base_list:
        if str(i.title) == name:
            print(i)

# decorator for generating views
def generate_multi(func):
    def wrap(*args):
        for i in range(10):
            func(*args)       
    return wrap

# Generate random views
@generate_multi
def generate_views():
    i = random.choice(base_list)
    j = random.choice(range(101))
    i.play(j)
    #print(i)
    #print(i.current_views)

# print out the top title by views
def top_titles(amount, content_type):
    top = [i for i in base_list if i.__class__.__name__ == content_type.__name__]
    top = sorted(top, key=lambda movie: movie.current_views, reverse=True)
    n=0
    for i in top:
        print(f"{i}, views = {i.current_views}")
        n=+1
        if n == amount:
            break

def print_help():
    print("List of available commands:\n movie list - print out all movies in the list\n series list - print out all series list\n "
        "generate random views - it will generate fake views for random items in library list\n search - it will find what u want\n " 
        "top titles - it will print out top titles of movies or series\n exit - terminate program")

# Available commands
def task():
    while True:
        task1 = input("What would you like to do? ")
        if task1 == "help_me":
            print_help()
        
        elif task1 == "movie list":
            get_movies()
        
        elif task1 == "series list":
            get_series()
        
        elif task1 == "generate random views":
            print("generated random views")
            generate_views()
        
        elif task1 == "search":
            name = input("What are you looking for? ")
            search(name)
        
        elif task1 == "top titles":
            name=input("Top series or movies ")
            a=input("How long shall the list be? ")
            if name == "movies":
                top_titles(a, Movie)
            elif name == "series":
                top_titles(a, Series)
        
        elif task1 == "exit":
            print("bye")
            break
        else:
            print("there is no such command, type help_me for list of available commands")

# Call out the program
if __name__ == "__main__":
    print("Hello! I am a simple program to do some stuff. Wanna check me out? Type in help_me for commands ;)")
    task()


    





        