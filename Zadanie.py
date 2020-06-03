import random
import itertools
from movie import Movie
from series import Series
#from library import Library


    
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

# add a movie to base
def add_movie():
    i = input("What is the title ")
    j = input("What year was it made ")
    k = input("What type of movie is it? ")
    base_list.append(Movie(title = i, year = j, typ = k))

#add full series to base
def add_series():
    i = input("What is the title ")
    j = input("What year was it made ")
    k = input("What type of series is it? ")
    l = int(input("How many seasons does it have? "))
    for s in range(l):
        m = int(input(f"How many episodes does season {s+1} have? "))
        for e in range(m):
            base_list.append(Series(title = i, year = j, typ = k, season = s+1, episode = e+1))

# Function to print objects from class only Movie
def get_movies():
    list_to_sort = [i for i in base_list if i.__class__.__name__ == 'Movie']
    list_to_sort = sorted(list_to_sort, key=lambda Movie: Movie.title)
    for i in list_to_sort:
        print(i)
    return list_to_sort

# Function to print objects from class only Series       
def get_series():
    list_to_sort = [i for i in base_list if i.__class__.__name__ == 'Series']
    list_to_sort = sorted(list_to_sort, key=lambda Series: Series.title)
    for i in list_to_sort:
        print(i)
    return list_to_sort

search_list=[]
# Search function
def search():
    by_what = input("Choose what You ar elooking for: title, type, year ")
    if by_what == "title":
        name = input("Type in the title you are looking for ")
        for i in base_list:
            if str(i.title) == name:
                search_list.append(i)
        return search_list
    if by_what == "type":
        name = input("What type of movie/series you are looking for ")
        for i in base_list:
            if str(i.typ) == name:
                search_list.append(i)
        return search_list
    if by_what == "year":
        name = input("What year of production you are looking for ")
        for i in base_list:
            if str(i.year) == name:
                search_list.append(i)
        return search_list

            

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
top_list=[]
def top_titles(amount, content_type):
    top = [i for i in base_list if i.__class__.__name__ == content_type.__name__]
    top = sorted(top, key=lambda movie: movie.current_views, reverse=True)
    n=0
    for i in top:
        top_list.append(i)
        n=+1
        if n == amount:
            break
    return(top_list)

def print_help():
    print("List of available commands:\n movie list - print out all movies in the list\n series list - print out all series list\n "
        "generate random views - it will generate fake views for random items in library list\n search - it will find what u want\n " 
        "top titles - it will print out top titles of movies or series\n exit - terminate program\n add movie - You may add a movie to base"
        " list\n add series - You may add series with full list of episodes in each season\n play - add a view for a movie\episode")

# Available commands
def task():
    while True:
        task1 = input("What would you like to do? ")
        if task1 == "help_me":
            print_help()
        
        elif task1 == "movie list":
            print("List of movies in base:")
            get_movies()
            for i in list_to_sort:
                print(i)
        
        elif task1 == "series list":
            print("List of series in base:")
            get_series()
            for i in list_to_sort:
                print(i)
        
        elif task1 == "generate random views":
            print("generated random views")
            generate_views()
        
        elif task1 == "search":
            search_list.clear()
            search()
            for i in search_list:
                print(i)
        
        elif task1 == "top titles":
            name=input("Top series or movies ")
            a=input("How long shall the list be? ")
            if name == "movies":
                top_titles(a, Movie)
                for i in top_list:
                    print(i)
            elif name == "series":
                top_titles(a, Series)
                for i in top_list:
                    print(i)
            else:
                print("There is no such list")

        elif task1 == "play":
            a = input("What movie/seires would you like to watch? ")
            for i in base_list:
                if a == str(i.title):
                    i.play()
                    print(f"You've seen this for the {i.current_views} time")
                    break
                
        elif task1 == "add movie":
            add_movie()
        
        elif task1 == "add series":
            add_series()
                         
        elif task1 == "exit":
            print("bye")
            break
        else:
            print("there is no such command, type help_me for list of available commands")

# Call out the program
if __name__ == "__main__":
    print("Hello! I am a simple program to do some stuff. Wanna check me out? Type in help_me for commands ;)")
    task()


    





        