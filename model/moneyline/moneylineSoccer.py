# pylint: disable=E0401

import requests
import json
import os
from API_Keys.vars import headers
import datetime

url = "https://odds.p.rapidapi.com/v1/odds"

#Retrieve API from Odds URL above

#change sport to just soccer to view other leagues' sport_key to then change to individual league -- uncomment print (eventsAPI) in model.py

#soccer_germany_bundesliga
#soccer_germany_bundesliga2
#soccer_belgium_first_div
#soccer_epl
#soccer_efl_champ
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


#change sport to any of the different soccer leagues above

querystring = {"sport":"soccer_epl","region":"us","mkt":"h2h"}

response = requests.request("GET", url, headers=headers, params=querystring)

sportsList = response.text

#Put into JSON format

gamesList = json.loads(sportsList)

theOddsAPIGames = gamesList['data']

gameDate = datetime.date.today()

gameWeek = gameDate + datetime.timedelta(7)

futureGame = gameDate + datetime.timedelta(9)

# change date for all games right here -- uncomment below to go to tomorrow's games

# gameDate = gameDate + datetime.timedelta(1)

now = datetime.datetime.now()

nowTime = (now.strftime("%Y-%m-%d %H:%M:%S"))

