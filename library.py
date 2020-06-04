from movie import Movie
from series import Series

top_list=[]
search_list=[]
class Library:
    def __init__(self):       
        self.video_lib = []

    def add_movie(self):
        i = input("What is the title? ")
        j = input("What year was it made? ")
        k = input("What type of movie is it? ")
        self.video_lib.append(Movie(title = i, year = j, typ = k))
    
    def add_series(self):
        i = input("What is the title? ")
        j = input("What year was it made? ")
        k = input("What type of series is it? ")
        l = int(input("How many seasons does it have? "))
        for s in range(l):
            m = int(input(f"How many episodes does season {s+1} have? "))
            for e in range(m):
                self.video_lib.append(Series(title = i, year = j, typ = k, season = str(s+1), episode = str(e+1)))

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
                if str(i.typ) == name:
                    search_list.append(i)
            return search_list
        if by_what == "year":
            name = input("What year of production you are looking for ")
            for i in self.video_lib:
                if str(i.year) == name:
                    search_list.append(i)
            return search_list

    
    def top_titles(self, amount, content_type):
        top = [i for i in self.video_lib if i.__class__.__name__ == content_type.__name__]
        top = sorted(top, key=lambda movie: movie.current_views, reverse=True)
        n=0
        for i in top:
            top_list.append(i)
            n=+1
            if n == amount:
                break
        return(top_list)