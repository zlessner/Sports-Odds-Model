import requests
import json
import os
from API_Keys.vars import headers
import datetime

url = "https://odds.p.rapidapi.com/v1/odds"

#change sport to just soccer to view other leagues' sport_key to then change to individual league -- unccomment print (eventsAPI) in model.py

#soccer_efl_champ
#soccer_germany_bundesliga
#soccer_germany_bundesliga2
#soccer_epl
#soccer_belgium_first_div
#soccer_england_league1
#soccer_england_league2
#soccer_spl
#soccer_portugal_primeira_liga
#soccer_argentina_primera_division
#soccer_mexico_ligamx
#soccer_australia_aleague
#soccer_turkey_super_league
#soccer_spain_la_liga
#soccer_france_ligue_one
#soccer_france_ligue_two
#soccer_italy_serie_a
#soccer_italy_serie_b



querystring = {"sport":"soccer_france_ligue_two","region":"us","mkt":"h2h"}

response = requests.request("GET", url, headers=headers, params=querystring)

sportsList = response.text

gamesList = json.loads(sportsList)

theOddsAPIGames = gamesList['data']

today = datetime.date.today()

# change date for all games right here

# today = today + datetime.timedelta(1)

now = datetime.datetime.now()

nowTime = (now.strftime("%Y-%m-%d %H:%M:%S"))

#adding multiple sports in querystring params
#Fix PL, add CBB