from movie import Movie
from series import Series
import random

top_list=[]
search_list=[]
class Library:
    def __init__(self):       
        self.video_lib = []

    # Function to add movies to base list
    def add_movie(self):
        i = input("What is the title? ")
        j = input("What year was it made? ")
        k = input("What type of movie is it? ")
        self.video_lib.append(Movie(title = i, year = j, gener = k))
    
    # Function to add series to base
    def add_series(self):
        i = input("What is the title? ")
        j = input("What year was it made? ")
        k = input("What type of series is it? ")
        l = int(input("How many seasons does it have? "))
        for s in range(l):
            m = int(input(f"How many episodes does season {s+1} have? "))
            for e in range(m):
                self.video_lib.append(Series(title = i, year = j, gener = k, season = str(s+1), episode = str(e+1)))

    # Function to print objects from class only Movie
    def get_movies(self):
        list_to_sort = [i for i in self.video_lib if i.__class__.__name__ == 'Movie']
        list_to_sort = sorted(list_to_sort, key=lambda Movie: Movie.title)
        for i in list_to_sort:
            print(i)
        return list_to_sort

    # Function to print objects from class only Series       
    def get_series(self):
        list_to_sort = [i for i in self.video_lib if i.__class__.__name__ == 'Series']
        list_to_sort = sorted(list_to_sort, key=lambda Series: Series.title)
        for i in list_to_sort:
            print(i)
        return list_to_sort

    
    # Search function
    def search(self):
        by_what = input("Choose what You ar elooking for: title, type, year ")
        if by_what == "title":
            name = input("Type in the title you are looking for ")
            for i in self.video_lib:
                if str(i.title) == name:
                    search_list.append(i)
            return search_list
        if by_what == "type":
            name = input("What type of movie/series you are looking for ")
            for i in self.video_lib:
                if str(i.gener) == name:
                    search_list.append(i)
            return search_list
        if by_what == "year":
            name = input("What year of production you are looking for ")
            for i in self.video_lib:
                if str(i.year) == name:
                    search_list.append(i)
            return search_list

    # Top x movies/seriesshown by current_views
    def top_titles(self, content_type):
        top = [i for i in self.video_lib if i.__class__.__name__ == content_type.__name__]
        top = sorted(top, key=lambda content_type: content_type.current_views, reverse=True)
        n=0
        a=int(input("How long shall the list be? "))
        top_list = top[:a]
        for i in top_list:
            print(f"{i} with views {i.current_views}")
        return top_list
        
    
    def generate_views(self):
        for k in range(10):
            i = random.choice(self.video_lib)
            j = random.choice(range(101))
            i.play(j)
            #print(i)
            #print(i.current_views)
    
    def play_sth(self):
        a = input("What movie/seires would you like to watch? ")
        for i in self.video_lib:
            if str(i.title) == a:
                if i.__class__ == Movie:
                    i.play()
                    print(f"You've seen this for the {i.current_views} time")
                    break
                elif i.__class__ == Series:
                    seas = input("Which season would You like to watch? ")
                    if str(i.season) == seas:
                        epi = input("Which episode? ")
                        if str(i.episode) == epi:
                            i.play()
                            print(f"You've seen this for the {i.current_views} time")
                    break
                        