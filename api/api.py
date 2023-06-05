"""This file can contain the code related to accessing the movie database API, making requests, and fetching movie data"""
import requests

# Change this
API_KEY = "YOUR_API_KEY"

def fetch_movies(genre=None, min_rating=None, min_year=None, max_year=None):
    '''Retrieves information from iMDb movie api?'''
    url = "Api link here"
    params = {
        "api_key": API_KEY,
        "language": "en-US",
        "sort_by": "popularity.desc",
        "include_adult": "false",
        "include_video": "false"
    }

    if genre:
        params["with_genres"] = genre

    if min_rating:
        params[""]