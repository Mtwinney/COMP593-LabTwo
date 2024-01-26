def main():
    return

    # TODO: Step 2 - Create a complex data structure
    about_me = {   
        'full_name': 'Michael Twinney',
        'student_id': 1564,
        'pizza_toppings': [Pepperoni, Cheese, Sausage],
        'movies': [
            {'title': 'Isle Of Dogs', 'genre': 'stop-motion'},
            {'title': 'Django', 'genre': 'Western'}
        ]   
    }                                      


    # TODO: Step 3 - Add another movie to the data structure
    extra_movie = {'title': 'The Dirt', 'genre': 'documentary-esque'}
    added_movie['movies'].append(new_movie)

# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    if 'full_name' in about_me and 'identification' in about_me:
        first_name = about_me['full_name'].split()[0]

        title = 'King'
        print(f"My name is {about_me['full_name']}, but you can call me {title} {first_name}.")
        print(f"My student ID is {about_me['identification']}")
    return
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    if 'pizza_toppings' in about_me:
        about_me['pizza_toppings'].extend(toppings)

        about_me['pizza_toppings'] = sorted([toppings.lower() for topping in about_me['pizza_toppings']])

        print("Added more toppings:", about_me['pizza_toppings'])
   
        toppings = ('Bacon', 'Peppers') 
        

        return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    return
    
if __name__ == '__main__':
    main()
