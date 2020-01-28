import requests
import json
import os
from API_Keys.vars import headers

url = "https://odds.p.rapidapi.com/v1/odds"

#change sport to just soccer to view other leagues' sport_key to then change to individual league

querystring = {"sport":"soccer_efl_champ","region":"us","mkt":"h2h"}

response = requests.request("GET", url, headers=headers, params=querystring)

sportsList = response.text

gamesList = json.loads(sportsList)

theOddsAPIGames = gamesList['data']
