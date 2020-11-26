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
#soccer_spain_segunda_division
#soccer_france_ligue_one
#soccer_france_ligue_two
#soccer_italy_serie_a
#soccer_italy_serie_b
#soccer_brazil_campeonato
#soccer_usa_mls
#soccer_sweden_allsvenskan
#soccer_russia_premier_league
#soccer_denmark_superliga
#soccer_uefa_champs_league
#soccer_uefa_europa_league
#soccer
#soccer_china_superleague
#soccer_netherlands_eredivisie
#soccer_norway_eliteserien
#soccer_switzerland_superleague



#change sport to any of the different soccer leagues above

soccer = True

sport = "soccer_netherlands_eredivisie"

querystring = {"sport":sport,"region":"us","mkt":"h2h"}

response = requests.request("GET", url, headers=headers, params=querystring)

sportsList = response.text

#Put into JSON format

gamesList = json.loads(sportsList)

theOddsAPIGames = gamesList['data']

gameDate = datetime.date.today()

gameWeek = gameDate + datetime.timedelta(6)

futureGame = gameDate + datetime.timedelta(1)

yesterdayGame = gameDate + datetime.timedelta(0)

pastNFLGame = gameDate + datetime.timedelta(-1)

futureNFLGame = gameDate + datetime.timedelta(4)

# change date for all games right here -- uncomment below to go to tomorrow's games

# gameDate = gameDate + datetime.timedelta(1)

now = datetime.datetime.now()

nowTime = (now.strftime("%Y-%m-%d %H:%M:%S"))


# Change sport to match FiveThirtyEight spelling

if sport == "soccer_epl":
    sport = 'Soccer Barclays Premier League'
if sport == "soccer_efl_champ":
    sport = 'Soccer English League Championship'
if sport == "soccer_england_league1":
    sport = 'Soccer English League One'
if sport == "soccer_england_league2":
    sport = 'Soccer English League Two'
if sport == "soccer_usa_mls":
    sport = 'Soccer Major League Soccer'
if sport == "soccer_uefa_champs_league":
    sport = 'Soccer Champions League'
if sport == "soccer_spain_segunda_division":
    sport = 'Spanish Segunda Division'
if sport == "soccer_spain_la_liga":
    sport = 'Spanish Primera Division'
# Not sure what Greek Super League is listed as
if sport == "XXX":
    sport = 'Greek Super League'
if sport == "soccer_turkey_super_league":
    sport = 'Turkey Super League'
if sport == "soccer_italy_serie_a":
    sport = 'Italy Serie A'
if sport == "soccer_portugal_primeira_liga":
    sport = 'Portuguese Liga'
if sport == "soccer_portugal_primeira_liga":
    sport = 'Portuguese Liga'
if sport == "soccer_netherlands_eredivisie":
    sport = 'Dutch Eredivisie'
if sport == "soccer_netherlands_eredivisie":
    sport = 'Dutch Eredivisie'
if sport == "china_superleague":
    sport = 'Chinese Super League'
if sport == "soccer_norway_eliteserien":
    sport = 'Norwegian Tippeligaen'
if sport == "soccer_switzerland_superleague":
    sport = 'Swiss Raiffeisen Super League'


    
    


    

    



