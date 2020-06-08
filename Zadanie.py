import itertools
from movie import Movie
from series import Series
from library import Library
from library import search_list
from library import top_list
from library import seaso


base_list = Library()
list_to_sort=[]
          

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
            base_list.get_movies()
            for i in list_to_sort:
                print(i)
        
        elif task1 == "series list":
            print("List of series in base:")
            base_list.get_series()
            for i in list_to_sort:
                print(i)
        
        elif task1 == "generate random views":
            print("generated random views")
            base_list.generate_views()
        
        elif task1 == "search":
            search_list.clear()
            base_list.search()
            for i in search_list:
                print(i)
        
        elif task1 == "top titles":
            name=input("Top series or movies ")           
            if name == "movies":
                base_list.top_titles(content_type = Movie)
                for i in top_list:
                    print(f"{i} with views {i.current_views}")
            elif name == "series":
                base_list.top_titles(content_type = Series)
                for i in top_list:
                    print(f"{i} with views {i.current_views}")
            else:
                print("There is no such list")

        elif task1 == "play":
            seaso.clear()
            base_list.play_sth()

        elif task1 == "add movie":
            base_list.add_movie()
        
        elif task1 == "add series":
            base_list.add_series()
                         
        elif task1 == "exit":
            print("bye")
            break
        else:
            print("there is no such command, type help_me for list of available commands")

# Call out the program
if __name__ == "__main__":
    print("Hello! I am a simple program to do some stuff. Wanna check me out? Type in help_me for commands ;)")
    task()


    





        