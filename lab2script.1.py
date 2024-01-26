import os
import sys

def main():
    # TODO: Step 2 - Create a complex data structure
    about_me = {   
        'full_name': 'Michael Twinney',
        'student_id': 1564,
        'pizza_toppings': ['Pepperoni', 'Cheese', 'Sausage'],
        'movies': [
            {'title': 'Isle Of Dogs', 'genre': 'stop-motion'},
            {'title': 'Django', 'genre': 'Western'}
        ]   
    }                                      

    # TODO: Step 3 - Add another movie to the data structure
    extra_movie = {'title': 'The Dirt', 'genre': 'documentary-esque'}
    about_me['movies'].append(extra_movie)

    # Call the functions to print the information
    print_student_name_and_id(about_me)
    add_pizza_toppings(about_me, ('Bacon', 'Peppers'))
    print_pizza_toppings(about_me)
    print_movie_genres(about_me)
    print_movie_titles(about_me['movies'])

# TODO: Step 4 - Function that prints student name and ID    
def print_student_name_and_id(about_me):
    if 'full_name' in about_me and 'student_id' in about_me:
        first_name = about_me['full_name'].split()[0]

        title = 'King'
        print(f"My name is {about_me['full_name']}, but you can call me {title} {first_name}.")
        print(f"My student ID is {about_me['student_id']}")
        print()

# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    if 'pizza_toppings' in about_me:
        about_me['pizza_toppings'].extend(toppings)
        about_me['pizza_toppings'] = sorted([topping.lower() for topping in about_me['pizza_toppings']])

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    if 'pizza_toppings' in about_me:
        print("My favourite pizza toppings are:")
        for topping in about_me['pizza_toppings']:
            print(f"- {topping}")
        print()

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    if 'movies' in about_me:
        genres = [movie['genre'] for movie in about_me['movies']]
        if len(genres) == 1:
            print(f"I like to watch {genres[0]} movies.")
        else:
            print("I like to watch", end=" ")
            for i in range(len(genres) - 1):
                print(f"{genres[i]}, ", end ="")

            print(f"and {genres[-1]} movies.")

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    if movie_list:
        movie_titles = [movie['title'].title() for movie in movie_list]
        if len(movie_titles) == 1:
            print(f"Some of my favourite movies are {movie_titles[0]}!")
        else:
            print("Some of my favourite movies are", end=" ")
            for i in range(len(movie_titles) - 1):
                print(f"{movie_titles[i]}, ", end="")
            print(f"and {movie_titles[-1]}!")

if __name__ == '__main__':
    main()
