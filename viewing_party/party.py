# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_info = {}
    if not title or not genre or not rating:
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
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)

    return user_data


# ------------- WAVE 2 --------------------
def get_watched_avg_rating(user_data):
    ratings_list = []
    if not user_data["watched"]:
        return 0.0
    for movie in user_data["watched"]:
        ratings_list.append(movie["rating"])

    average_rating = sum(ratings_list) / len(ratings_list)
    return average_rating

def get_most_watched_genre(user_data):
    genre_count = {}
    most_watched_genre = ""
    if not user_data["watched"]:
        return None

    for movie in user_data["watched"]:
        if movie["genre"] not in genre_count:
            genre_count[movie["genre"]] = 1
        else:
            genre_count[movie["genre"]] += 1

    most_watched_genre = max(genre_count, key=genre_count.get)
    return most_watched_genre

# ------------- WAVE 3 --------------------
def get_unique_watched(user_data):
# user_data: {
#   "watched": [{}]
#   "friends": [
#       {"watched": [{}]
#       }]
# }
    user_watched = {movie["title"] for movie in user_data["watched"]}
    friends_watched = {
        movie["title"] for friend in user_data["friends"] for movie in friend ["watched"]
    }

    user_watched_set = set(user_watched)
    friends_watched_set = set(friends_watched)

    unique_movies_watched = user_watched - friends_watched

    unique_movies_list = [
            movie for movie in user_data["watched"] if movie["title"] in unique_movies_watched
    ]

    return unique_movies_list

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
