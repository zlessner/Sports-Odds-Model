import requests
import json
import os
from Ignore.vars import headers

url = "https://odds.p.rapidapi.com/v1/odds"

querystring = {"sport":"soccer","region":"us","mkt":"h2h"}

response = requests.request("GET", url, headers=headers, params=querystring)

sportsList = response.text

gamesList = json.loads(sportsList)

workingGames = gamesList['data']
