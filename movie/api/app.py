"""This file can contain the code related to accessing the movie database API, making requests, and fetching movie data"""
# import requests
import movie
from flask import request, render_template

# app = Flask(__name__)

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

@movie.app.route("/")
def home():
    context = {
        'first_load': True,
    }
    return render_template("movie.html", **context)


@movie.app.route("/recommend", methods=["POST"])
def recommend():
    genre = request.form.get("genre")
    rating_limit = float(request.form.get("ratingSlider"))
    min_year = int(request.form.get("minSlider"))
    max_year = int(request.form.get("maxSlider"))
    

    context = {
        'movies_avail': True,
        'content': "hello",
    }
    
    return render_template("movie.html", **context)

@movie.app.route("/about")
def about():
    return render_template("about.html")

@movie.app.route("/hanna")
def hanna_page():
    return render_template("hanna.html")

@movie.app.route("/kody")
def kody_page():
    return render_template("kody.html")


if __name__ == "__main__":
    movie.app.run()