import requests
import json
from .keys import PEXELS_API_KEY


def get_photo(city, state):
    headers = {"Authorization": PEXELS_API_KEY}
    params = {"per_page": 1, "query": city + " " + "state"}
    url = "https://api.pexels.com/v1/search"
    response = requests.get(url, headers=headers, params=params)
    content = json.loads(response.content)
    try:
        return {"picture_url": content["photos"][0]["src"]["original"]}
    except:
        return {"picture_url": None}


def get_weather_data(city, state):
    # Create the URL for the geocoding API with the city and state
    # Make the request
    # Parse the JSON response
    # Get the latitude and longitude from the response

    # Create the URL for the current weather API with the latitude
    #   and longitude
    # Make the request
    # Parse the JSON response
    # Get the main temperature and the weather's description and put
    #   them in a dictionary
    # Return the dictionary
    pass
