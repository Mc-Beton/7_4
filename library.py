from movie import Movie
from series import Series
import random
import csv

top_list=[]
search_list=[]
seaso=[]
class Library:
    def __init__(self):       
        self.video_lib = []
    


    # Function to add movies to base list
    def add_movie(self, i, j, k):
        self.video_lib.append(Movie(title = i, year = j, gener = k))
        with open('movie_lib.csv', 'a', newline='') as csvfile:
            fieldnames = ['Title', 'Year', 'Type']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writerow({'Title':i, 'Year':j, 'Type':k})
    
    # Function to add series to base
    def add_series(self, i, j, k, h, n):
        self.video_lib.append(Series(title = i, year = j, gener = k, season = h, episode = n))
        with open('series_lib.csv', 'a', newline='') as csvfile:
            fieldnames = ['Title', 'Year', 'Type', 'Seasons', 'Episode']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writerow({'Title':i, 'Year':j, 'Type':k, 'Seasons':h, 'Episode':n})

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
    def search(self, by_what, name):  
        if by_what == "title":
            for i in self.video_lib:
                if str(i.title) == name:
                    search_list.append(i)
            return search_list
        if by_what == "type":
            for i in self.video_lib:
                if str(i.gener) == name:
                    search_list.append(i)
            return search_list
        if by_what == "year":
            for i in self.video_lib:
                if str(i.year) == name:
                    search_list.append(i)
            return search_list

    # Top x movies/seriesshown by current_views
    def top_titles(self, content_type, amount):
        top = [i for i in self.video_lib if i.__class__.__name__ == content_type.__name__]
        top = sorted(top, key=lambda content_type: content_type.current_views, reverse=True)
        top_list = top[:amount]
        for i in top_list:
            print(f"{i} with views {i.current_views}")
        return top_list
        
        
    def play_sth(self, a):
        for i in self.video_lib:
            if str(i.title) == a:
                seaso.append(i)
        for i in seaso:
            if isinstance(i, Series):
                seas = input("Which season would You like to watch? ")
                epi = input("Which episode? ")
                for k in seaso:
                    if str(k.season) == seas and str(k.episode) == epi:
                        k.play()
                        print(f"You've seen this for the {k.current_views} time")
                break
            elif isinstance(i, Movie):
                i.play()
                print(f"You've seen this for the {i.current_views} time")
                break
                
"""
                    
"""                    