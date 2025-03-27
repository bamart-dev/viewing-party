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
    user_watched = []
    for movie in user_data["watched"]:
        user_watched.append(movie["title"])

    friends_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in friends_watched:
                friends_watched.append(movie["title"])

    user_watched_set = set(user_watched)
    friends_watched_set = set(friends_watched)

    unique_movies_watched_user_only = user_watched_set - friends_watched_set

    unique_movies_watched_user_only_list = []
    for movie in user_data["watched"]:
        if movie["title"] in unique_movies_watched_user_only:
            unique_movies_watched_user_only_list.append(movie)

    return unique_movies_watched_user_only_list

def get_friends_unique_watched(user_data):
    user_watched = []
    for movie in user_data["watched"]:
        user_watched.append(movie["title"])

    friends_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in friends_watched:
                friends_watched.append(movie["title"])

    user_watched_set = set(user_watched)
    friends_watched_set = set(friends_watched)

    unique_movies_watched_friends_only = friends_watched_set - user_watched_set

    seen_titles = []
    unique_movies_watched_friends_only_list = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] in unique_movies_watched_friends_only and movie["title"] not in seen_titles:
                unique_movies_watched_friends_only_list.append(movie)
                seen_titles.append(movie["title"])
    
    return unique_movies_watched_friends_only_list

# ------------- WAVE 4 --------------------
def get_available_recs(user_data):
    user_watched = []
    for movie in user_data["watched"]:
        user_watched.append(movie["title"])

    subscriptions = user_data["subscriptions"]
    
    friends_watched_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_watched_movies:
                friends_watched_movies.append(movie)

    rec_movies = []
    for movie in friends_watched_movies:
        if movie["title"] not in user_watched and movie["host"] in subscriptions:
            rec_movies.append(movie)

    return rec_movies

# ------------- WAVE 5 --------------------
def get_new_rec_by_genre(user_data):
    user_watched = []
    for movie in user_data["watched"]:
        user_watched.append(movie["title"])

    friends_watched_movies = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_watched_movies:
                friends_watched_movies.append(movie)
                
    genre_count = {}
    most_watched_genre = ""
    if not user_data["watched"]:
        return []

    for movie in user_data["watched"]:
        if movie["genre"] not in genre_count:
            genre_count[movie["genre"]] = 1
        else:
            genre_count[movie["genre"]] += 1
    most_watched_genre = max(genre_count, key=genre_count.get)

    genre_recommendations = []
    for movie in friends_watched_movies:
        if movie["title"] not in user_watched and movie["genre"] == most_watched_genre:
            genre_recommendations.append(movie)

    return genre_recommendations

def get_rec_from_favorites(user_data):
    friends_watched = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.add(movie["title"])

    user_watched = set()
    for movie in user_data["watched"]:
        user_watched.append(movie["title"])

    if not user_data["friends"]:
        fav_recommendations = []
        for movie in user_data["favorites"]:
            if movie["title"] not in user_watched:
                fav_recommendations.append(movie)
        return fav_recommendations
    
    fav_recommendations = []
    for movie in user_data["favorites"]:
        if movie["title"] not in friends_watched:
            fav_recommendations.append(movie)

    return fav_recommendations
