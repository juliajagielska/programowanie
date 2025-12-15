from flask import Flask, jsonify, render_template_string
import sqlite3
from pathlib import Path

app = Flask(__name__)

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "database" / "movies.db"


def get_conn():
    return sqlite3.connect(DB_PATH)


def fetch_all(table_name: str, limit: int = 200):
    conn = get_conn()
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name} LIMIT ?", (limit,))
    rows = cur.fetchall()
    conn.close()
    return rows


def rows_to_dicts(rows):
    return [dict(r) for r in rows]


@app.route("/")
def home():
    return """
    <h2>API SQLite</h2>
    <ul>
      <li><a href="/movies">/movies</a></li>
      <li><a href="/links">/links</a></li>
      <li><a href="/ratings">/ratings</a></li>
      <li><a href="/tags">/tags</a></li>
      <li><a href="/tables">/tables (HTML - tabelki)</a></li>
    </ul>
    """


@app.route("/movies")
def movies():
    rows = fetch_all("movies")
    return jsonify(rows_to_dicts(rows))


@app.route("/links")
def links():
    rows = fetch_all("links")
    return jsonify(rows_to_dicts(rows))


@app.route("/ratings")
def ratings():
    rows = fetch_all("ratings")
    return jsonify(rows_to_dicts(rows))


@app.route("/tags")
def tags():
    rows = fetch_all("tags")
    return jsonify(rows_to_dicts(rows))


@app.route("/tables")
def tables():
    tables = ["movies", "links", "ratings", "tags"]

    html = """
    <html>
    <head>
      <meta charset="utf-8"/>
      <title>Tabele SQLite</title>
      <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { border-collapse: collapse; width: 100%; margin-bottom: 40px; }
        th, td { border: 1px solid #ccc; padding: 6px; font-size: 12px; }
        th { position: sticky; top: 0; background: #f2f2f2; }
        h2 { margin-top: 40px; }
        .hint { color:#666; font-size: 12px; }
      </style>
    </head>
    <body>
      <h1>Tabele z bazy SQLite</h1>
      <p class="hint">Pokazuję maksymalnie 200 pierwszych wierszy z każdej tabeli.</p>

      {% for t in tables %}
        <h2>{{ t }}</h2>
        <table>
          <thead>
            <tr>
              {% for col in data[t]["cols"] %}
                <th>{{ col }}</th>
              {% endfor %}
            </tr>
          </thead>
          <tbody>
            {% for row in data[t]["rows"] %}
              <tr>
                {% for col in data[t]["cols"] %}
                  <td>{{ row[col] }}</td>
                {% endfor %}
              </tr>
            {% endfor %}
          </tbody>
        </table>
      {% endfor %}
    </body>
    </html>
    """

    data = {}
    for t in tables:
        rows = fetch_all(t)
        cols = rows[0].keys() if rows else []
        data[t] = {"cols": list(cols), "rows": rows_to_dicts(rows)}

    return render_template_string(html, tables=tables, data=data)


if __name__ == "__main__":
    app.run(debug=True)

