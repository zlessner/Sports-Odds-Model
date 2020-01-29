import requests
import json
import os
from API_Keys.vars import headers
import datetime

url = "https://odds.p.rapidapi.com/v1/odds"

#change sport to just soccer to view other leagues' sport_key to then change to individual league -- unccomment print (eventsAPI) in model.py

#soccer_efl_champ
#soccer_germany_bundesliga2
#soccer_epl

querystring = {"sport":"soccer_germany_bundesliga2","region":"us","mkt":"h2h"}

response = requests.request("GET", url, headers=headers, params=querystring)

sportsList = response.text

gamesList = json.loads(sportsList)

theOddsAPIGames = gamesList['data']

today = datetime.date.today()

tomorrow = today + datetime.timedelta(1)

