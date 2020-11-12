# pylint: disable=E0401

import requests
import json
from API_Keys.vars import headers
import datetime

url = "https://odds.p.rapidapi.com/v1/odds"

#Retrieve API from Odds URL above

querystring = {"sport":"basketball_ncaab","region":"us","mkt":"h2h"}

response = requests.request("GET", url, headers=headers, params=querystring)

sportsList = response.text

#Put into JSON format

gamesList = json.loads(sportsList)

theOddsAPIGames = gamesList['data']