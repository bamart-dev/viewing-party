# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_info = {}
    if not title and genre and rating:
        return None

    # if title and genre and rating:
    
    movie_info["title"] = title
    movie_info["genre"] = genre
    movie_info["rating"] = rating

    return movie_info

result = create_movie("", "Horror", "5")
print(result)

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    pass

def watch_movie(user_data, title):
    pass
    


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

