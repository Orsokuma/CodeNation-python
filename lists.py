movie_list = [
    "Little Shop of Horrors",
    "The Matrix",
    "Star Trek: First Contact"
]
# Get a movie by index, or a random movie
def get_movie(index = False):
    global movie_list
    # Get the amount of entries in the list
    cnt = len(movie_list)
    # If we didn't pass an argument
    if index == False:
        import random
        # Generate a random integer between 0 and item count - 1 (top index)
        rand = random.randint(0, cnt - 1)
        # Return that entry
        return movie_list[rand]
    elif index > cnt - 1: # if we've passed an index higher than our top index
        # Tell 'em no!
        return 'That selection isn\'t available'
    # Default back to returning the entry given
    return movie_list[index]

# Add an entry, duplication prevention
def add_movie(movie_name):
    global movie_list
    # check if the name passed is already in the list (transform to lowercase for sanity)
    if movie_name.lower() in (movie.lower() for movie in movie_list): # can't .lower() a list, so transform with a temp variable
        # it's already in there
        return 'You\'ve already added ' + movie_name + ' to your movie list'
    else:
        # It's not there, add it!
        movie_list.append(movie_name)
        # Let 'em know
        return movie_name + ' added'

# Remove a movie from the list
def remove_movie(movie_name):
    global movie_list
    if (movie_name.lower() not in (movie.lower() for movie in movie_list)):
        return movie_name + ' isn\'t on the list'
    else:
        movie_list.remove(movie_name)
        return movie_name + ' has been removed'

# Get all entries
def get_all_movies():
    global movie_list
    # Start a blank string
    str = '';
    # Loop through the entries
    for entry in movie_list:
        # Append the string with the entry and a newline character
        str += entry + "\n"
    # Remove the final newline character and return it
    return str.rstrip("\n");

def remove_duplicates(list_items):
    return list(dict.fromkeys(list_items))

# Add multiple movies (comma-separated string)
def add_multiple_movies(movie_names):
    global movie_list
    # Split the string by their commas into a list
    movies = movie_names.split(',')
    # Get initial count
    movie_cnt = len(movie_list)
    # Join the lists together
    movie_list.extend(movies)
    # Remove duplicates
    movie_list = remove_duplicates(movie_list)
    diff = len(movie_list) - movie_cnt;
    return str(diff) + ' movie(s) added'

def reverse_movies():
    global movie_list
    return movie_list.reverse();

def replace_movie(old_name, new_name):
    global movie_list
    if (old_name.lower() not in (movie.lower() for movie in movie_list)):
        ret = old_name + ' isn\'t in the list. Adding instead'
        add_movie(old_name);
        return ret + "\nAdded"

    movie_index = next(i for i,v in enumerate(movie_list) if v.lower() == old_name.lower())
    print('INDEX:', movie_index)
    if movie_index == False:
        return old_name + ' isn\'t in the list'
    movie_list[movie_index] = new_name
    movie_list = remove_duplicates(movie_list)


print(f"Random movie selected: {get_movie()}\n") # Get a random movie
print(f"Second entry: {get_movie(1)}\n") # Get the second entry
print(f"All movies: {get_all_movies()}\n") # Get a line-separated string of entries
print("Add movie", add_movie("Home Alone"), "\n") # Add a movie to the list
print("Add movie", add_movie("Home Alone"), "\n") # Attempt to re-add the same movie
print(f"All movies: {get_all_movies()}\n") # Get a line-separated string of entries
print("Remove movie", remove_movie('Home Alone'), "\n")
print(f"All movies: {get_all_movies()}\n") # Get a line-separated string of entries
print("Add multiple movies:", add_multiple_movies("Home Alone,Rocky Horror Picture Show,Crouching Tiger; Hidden Dragon,Home Alone,Home Alone"), "\n") # Returns "3 movie(s) added"
print(f"All movies: {get_all_movies()}\n") # Get a line-separated string of entries
print("Flip order: ", reverse_movies(), "\n")
print(f"All movies: {get_all_movies()}\n") # Get a line-separated string of entries
print(f"Random movie selected: ", get_movie(), "\n") # Get a random movie
print(f"Old movie: The Matrix · New movie: Up\n", replace_movie("The Matrix", "Up"), "\n") # Replace an entry
print(f"All movies:\n{get_all_movies()}\n") # Get a line-separated string of entries
print(f"Old movie: Up · New movie: The Matrix\n", replace_movie("up", "The Matrix"), "\n") # Replace an entry
print(f"All movies:\n{get_all_movies()}\n") # Get a line-separated string of entries

