import csv
import os
from flask import Flask, jsonify, request
from models import Movie, Link, Rating, Tag

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

def read_csv_rows(filename):
    path = os.path.join(DATA_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))

@app.get("/")
def hello():
    return jsonify({"hello": "world"})

@app.get("/movies")
def movies():
    rows = read_csv_rows("movies.csv")
    return jsonify([Movie(
        id=int(r["movieId"]),
        title=r["title"],
        genres=r["genres"]
    ).__dict__ for r in rows])

@app.get("/links")
def links():
    rows = read_csv_rows("links.csv")
    return jsonify([Link(
        movieId=int(r["movieId"]),
        imdbId=r.get("imdbId", ""),
        tmdbId=r.get("tmdbId", "")
    ).__dict__ for r in rows])

@app.get("/ratings")
def ratings():
    rows = read_csv_rows("ratings.csv")
    limit = int(request.args.get("limit", 100))
    return jsonify([Rating(
        userId=int(r["userId"]),
        movieId=int(r["movieId"]),
        rating=float(r["rating"]),
        timestamp=int(r["timestamp"])
    ).__dict__ for r in rows[:limit]])

@app.get("/tags")
def tags():
    rows = read_csv_rows("tags.csv")
    limit = int(request.args.get("limit", 100))
    return jsonify([Tag(
        userId=int(r["userId"]),
        movieId=int(r["movieId"]),
        tag=r["tag"],
        timestamp=int(r["timestamp"])
    ).__dict__ for r in rows[:limit]])

if __name__ == "__main__":
    app.run(debug=True)
