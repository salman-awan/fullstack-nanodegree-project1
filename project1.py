import fresh_tomatoes
import media
import datetime

# Instances of Movie class for my favorite movies
interstellar = media.Movie(
    "Interstellar",
    "http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_SX214_AL_.jpg",  # noqa
    "http://www.youtube.com/watch?v=ePbKGoIGAXY",
    ["Matthew McConaughey", "Anne Hathaway"],
    datetime.date(2014, 11, 7),
    "A team of explorers travel through a wormhole in space in an attempt to \
    ensure humanity's survival.")

inception = media.Movie(
    "Inception",
    "http://ia.media-imdb.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SX214_AL_.jpg",  # noqa
    "http://www.youtube.com/watch?v=8hP9D6kZseM",
    ["Leonardo DiCaprio", "Joseph Gordon-Levitt"],
    datetime.date(2010, 7, 16),
    "A thief who steals corporate secrets through use of dream-sharing \
    technology is given the inverse task of planting an idea into the mind of \
    a CEO.")

dark_knight = media.Movie(
    "The Dark Knight",
    "http://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY317_CR0,0,214,317_AL_.jpg",  # noqa
    "http://www.youtube.com/watch?v=yQ5U8suTUw0",
    ["Christian Bale", "Heath Ledger"],
    datetime.date(2008, 7, 18),
    "When the menace known as the Joker wreaks havoc and chaos on the people \
    of Gotham, the caped crusader must come to terms with one of the greatest \
    psychological tests of his ability to fight injustice.")

memento = media.Movie(
    "Memento",
    "http://ia.media-imdb.com/images/M/MV5BMTc4MjUxNDAwN15BMl5BanBnXkFtZTcwMDMwNDg3OA@@._V1_SY317_CR12,0,214,317_AL_.jpg",  # noqa
    "http://www.youtube.com/watch?v=0vS0E9bBSL0",
    ["Guy Pearce", "Carrie-Anne Moss"],
    datetime.date(2001, 5, 25),
    "A man creates a strange system to help him remember things; so he can \
    hunt for the murderer of his wife without his short-term memory loss \
    being an obstacle.")

fight_club = media.Movie(
    "Fight Club",
    "http://ia.media-imdb.com/images/M/MV5BMjIwNTYzMzE1M15BMl5BanBnXkFtZTcwOTE5Mzg3OA@@._V1_SX214_AL_.jpg",  # noqa
    "http://www.youtube.com/watch?v=SUXWAEX2jlg",
    ["Brad Pitt", "Edward Norton"],
    datetime.date(1999, 10, 15),
    "An insomniac office worker, looking for a way to change his life, crosses \
    paths with a devil-may-care soap maker, forming an underground fight club \
    that evolves into something much, much more...")

pulp_fiction = media.Movie(
    "Pulp Fiction",
    "http://ia.media-imdb.com/images/M/MV5BMjE0ODk2NjczOV5BMl5BanBnXkFtZTYwNDQ0NDg4._V1_SY317_CR4,0,214,317_AL_.jpg",  # noqa
    "http://www.youtube.com/watch?v=wZBfmBvvotE",
    ["John Travolta", "Uma Thurman", "Samuel L. Jackson"],
    datetime.date(1994, 10, 14),
    "The lives of two mob hit men, a boxer, a gangster's wife, and a pair of \
    diner bandits intertwine in four tales of violence and redemption.")

# A list of my favorite movies
movies = [interstellar, inception, dark_knight, memento, fight_club,
          pulp_fiction]

# call the open_movies_page function passing the list of my favorite movies
fresh_tomatoes.open_movies_page(movies)
