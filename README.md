# **Movie/Series Library**

It's a simple program to store basic info about movies and series and register how many times a particular position has been viewed.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system. 
Just clone or download the files into a folder and it's ready to be used.

## How to use it.
Here You'll find how to turn on the program and a list of available commands You may use.
### Turn it on in CMD
In the proper directory of dwonloaded files type in:
> python zadanie.py

And there shows up the first line greeting us with a tip, how to get started.
### List of available commands.
- help_me - prints out all available commands You may use in this program
- movie list - prints out all movies which were provided to the program
- series list - prints out all movies which were provided to the program
- generate random views - it will generate fake views for random items in the library list
- search - prints out desired items from the library of movies and series. It will ask You by which criteria You would like to search:
      - title - it will search by the name of a movie or series
      - year - it will search by the year of production
      - type - it will search by the type of movie/series
- top titles - it will print out top list of movies or series in accordance to their current views
- add movie - You can add movies to your library. It will ask you for the title, year of production and type of movie You want to add.
- add series - You can add full series to your library. It will ask you for the title, year of production and type of series You want to add. As weel it will ask how many seasons does the the series have and how many episodes are there in each season. Each episode will be added as a seperate position in the library.
- play - if You're watch a movie or series, you may track how many times You have seen this particular content. For series it will ask for the season and episode you want to tick.
- exit - turn of the program

## Getting started/examples
First of all, this is currently a project which **doesn't store information for later use** (doesn't save the given information in a file), so it's only to check whether all the given commands really work.
### Examples
Lets turn it on:
    **python zadanie.py**

And there we get greetings from the program and a small assist how get started.
    Hello! I am a simple program to do some stuff. Wanna check me out? Type in help_me for commands ;)
    What would you like to do? 

Lets start with "**movie list**".
    List of movies in base:
    What would you like to do?

As You can see there is nothing in this list (as mentioned above), lets add something to our library:
> **add movie**

Here we will be asked some questions about the content we want to add, lets say we like the first Avengers:
> What is the title? **Avengers** 
>What year was it made? **2012**
>What type of movie is it? **Sci Fi**

And here we go. Our first position in our library. Lets check it out if it's still there:
> **movie list**
>List of movies in base:
>Avengers, 2012, Sci Fi

Lest try some series:
> **add series**

Here we go again just like with a movie but it will ask for more information:
> What is the title? **Dark**
>What year was it made? **2018**
>What type of series is it? **Sci Fi**
>How many seasons does it have? **2**
>How many episodes does season 1 have? **6**
>How many episodes does season 2 have? **7**

And how does it look like in our library:
> **series list**
>List of series in base:
>Dark S1E1
>Dark S1E2
>Dark S1E3
>Dark S1E4
>Dark S1E5
>Dark S1E6
>Dark S2E1
>Dark S2E2
>Dark S2E3
>Dark S2E4
>Dark S2E5
>Dark S2E6
>Dark S2E7

Now we are watching someting, lets say the Avengers:
>**play**
> What movie/seires would you like to watch? 

Type in the title of movie:
> **Avengers**
> You've seen this for the 1 time

Lets do it again:
What would you like to do? **play**
What movie/seires would you like to watch? **Avengers**
You've seen this for the 2 time

What if We want cheat a bit make some random views in our library?
> **generate random views**

Lets do it a couple of times:
> **generate random views**
...

Now we can check out which content is the most popular in our library:
> **top titles**
> Top series or movies?

Lets go for series:
> **series**
>How long shall the list be? **4**
>Dark S2E7 with views 155
>Dark S2E5 with views 81
>Dark S1E5 with views 67
>Dark S2E1 with views 52

And finaly "search"
> **search**
> Choose what You ar elooking for: title, type, year

Try "type":
> **type**
>What type of movie/series you are looking for **Sci Fi**
>Dark S1E1
>Dark S1E2
>Dark S1E3
>Dark S1E4
>Dark S1E5
>Dark S1E6
>Dark S2E1
>Dark S2E2
>Dark S2E3
>Dark S2E4
>Dark S2E5
>Dark S2E6
>Dark S2E7
>Avengers, 2012, Sci Fi

I guess we are done with some examples. ;)

## Later updates.
Soon the program will be provided with saving the library for later use and maybe more attractive in Tkinter.

## Authors
Filip Gabrys - Initial work
With help from his mentor from the Kodilla course.
