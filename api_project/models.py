from __future__ import annotations


class Movie:
    def __init__(self, movie_id: int, title: str, genres: str):
        self.id = movie_id
        self.title = title
        self.genres = genres

    def to_dict(self) -> dict:
        return {"id": self.id, "title": self.title, "genres": self.genres}


class Rating:
    def __init__(self, user_id: int, movie_id: int, rating: float):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating

    def to_dict(self) -> dict:
        return {"user_id": self.user_id, "movie_id": self.movie_id, "rating": self.rating}


class Link:
    def __init__(self, movie_id: int, imdb_id: str, tmdb_id: str | None):
        self.movie_id = movie_id
        self.imdb_id = imdb_id
        self.tmdb_id = tmdb_id

    def to_dict(self) -> dict:
        return {"movie_id": self.movie_id, "imdb_id": self.imdb_id, "tmdb_id": self.tmdb_id}


class Tag:
    def __init__(self, user_id: int, movie_id: int, tag: str):
        self.user_id = user_id
        self.movie_id = movie_id
        self.tag = tag

    def to_dict(self) -> dict:
        return {"user_id": self.user_id, "movie_id": self.movie_id, "tag": self.tag}