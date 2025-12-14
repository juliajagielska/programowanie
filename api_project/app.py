from __future__ import annotations

import csv
from pathlib import Path
from fastapi import FastAPI, HTTPException

from models import Movie, Rating, Link, Tag

app = FastAPI(title="Movies API")

DATA_DIR = Path(__file__).parent / "data"
MOVIES_CSV = DATA_DIR / "movies.csv"
RATINGS_CSV = DATA_DIR / "ratings.csv"
LINKS_CSV = DATA_DIR / "links.csv"
TAGS_CSV = DATA_DIR / "tags.csv"


def _require_file(path: Path) -> None:
    if not path.exists():
        raise HTTPException(status_code=404, detail=f"File not found: {path.name} (put it in data/)")


@app.get("/")
def root():
    return {"status": "ok"}


@app.get("/movies")
def get_movies():
    _require_file(MOVIES_CSV)
    movies: list[dict] = []

    with MOVIES_CSV.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        # oczekiwane kolumny: movieId,title,genres
        for row in reader:
            movie = Movie(
                movie_id=int(row["movieId"]),
                title=row["title"],
                genres=row["genres"],
            )
            movies.append(movie.to_dict())

    return movies


@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    _require_file(MOVIES_CSV)

    with MOVIES_CSV.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row["movieId"]) == movie_id:
                return Movie(
                    movie_id=int(row["movieId"]),
                    title=row["title"],
                    genres=row["genres"],
                ).to_dict()

    raise HTTPException(status_code=404, detail="Movie not found")


@app.get("/ratings")
def get_ratings():
    _require_file(RATINGS_CSV)
    ratings: list[dict] = []

    with RATINGS_CSV.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        # oczekiwane kolumny: userId,movieId,rating
        for row in reader:
            r = Rating(
                user_id=int(row["userId"]),
                movie_id=int(row["movieId"]),
                rating=float(row["rating"]),
            )
            ratings.append(r.to_dict())

    return ratings


@app.get("/movies/{movie_id}/ratings")
def get_movie_ratings(movie_id: int):
    _require_file(RATINGS_CSV)
    out: list[dict] = []

    with RATINGS_CSV.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if int(row["movieId"]) == movie_id:
                out.append(
                    Rating(
                        user_id=int(row["userId"]),
                        movie_id=int(row["movieId"]),
                        rating=float(row["rating"]),
                    ).to_dict()
                )

    if not out:
        raise HTTPException(status_code=404, detail="No ratings for this movie")

    return out


@app.get("/links")
def get_links():
    _require_file(LINKS_CSV)
    links: list[dict] = []

    with LINKS_CSV.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        # oczekiwane kolumny: movieId,imdbId,tmdbId
        for row in reader:
            tmdb_raw = row.get("tmdbId", "")
            tmdb_val = tmdb_raw if tmdb_raw not in ("", None) else None
            link = Link(
                movie_id=int(row["movieId"]),
                imdb_id=str(row["imdbId"]),
                tmdb_id=str(tmdb_val) if tmdb_val is not None else None,
            )
            links.append(link.to_dict())

    return links


@app.get("/tags")
def get_tags():
    _require_file(TAGS_CSV)
    tags: list[dict] = []

    with TAGS_CSV.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        # oczekiwane kolumny: userId,movieId,tag
        for row in reader:
            t = Tag(
                user_id=int(row["userId"]),
                movie_id=int(row["movieId"]),
                tag=row["tag"],
            )
            tags.append(t.to_dict())

    return tags