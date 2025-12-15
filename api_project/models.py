from dataclasses import dataclass

@dataclass
class Movie:
    id: int
    title: str
    genres: str

@dataclass
class Link:
    movieId: int
    imdbId: str
    tmdbId: str

@dataclass
class Rating:
    userId: int
    movieId: int
    rating: float
    timestamp: int

@dataclass
class Tag:
    userId: int
    movieId: int
    tag: str
    timestamp: int
