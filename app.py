"""This file can contain the code related to accessing the movie database API, making requests, and fetching movie data"""
import requests
from flask import Flask, request, render_template

app = Flask(__name__)

# Change this
# API_KEY = "YOUR_API_KEY"

# def fetch_movies(genre=None, min_rating=None, min_year=None, max_year=None):
#     '''Retrieves information from iMDb movie api?'''
#     url = "Api link here"
#     params = {
#         "api_key": API_KEY,
#         "language": "en-US",
#         "sort_by": "popularity.desc",
#         "include_adult": "false",
#         "include_video": "false"
#     }

#     if genre:
#         params["with_genres"] = genre

#     if min_rating:
#         params[""]

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():
    genre = request.form.get("genre")
    rating_limit = float(request.form.get("ratingSlider"))
    min_year = int(request.form.get("minSlider"))
    max_year = int(request.form.get("maxSlider"))
    print("HELLO!")

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run()

