import requests

# Using "streaming availability" website
url = "https://streaming-availability.p.rapidapi.com/v2/search/basic"

querystring = {"country":"us","services":"netflix,hulu.addon.hbo,","output_language":"en","show_type":"movie","genre":"18","show_original_language":"en"}

headers = {
	"X-RapidAPI-Key": "c02b67c0dbmshcf8d74e0c532f95p1fe720jsne8e32f57eff7",
	"X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())