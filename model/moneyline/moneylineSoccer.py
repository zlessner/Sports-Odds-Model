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
#soccer_japan_j_league



#change sport to any of the different soccer leagues above

soccer = True

sport = "soccer_efl_champ"

querystring = {"sport":sport,"region":"us","mkt":"h2h"}

response = requests.request("GET", url, headers=headers, params=querystring)

sportsList = response.text

#Put into JSON format

gamesList = json.loads(sportsList)

theOddsAPIGames = gamesList['data']

gameDate = datetime.date.today()

gameWeek = gameDate + datetime.timedelta(6)

futureGame = gameDate + datetime.timedelta(1)

futureGameMDY = (futureGame.strftime("%-m/%-d/%y"))

yesterdayGame = gameDate + datetime.timedelta(0)

yesterdayGameMDY = (yesterdayGame.strftime("%-m/%-d/%y"))

stringGameDate = str(futureGame)

stringYesterdayDate = str(yesterdayGame)

stringGameDateMDY = str(futureGameMDY)

stringYesterdayDateMDY = str(yesterdayGameMDY)

pastNFLGame = gameDate + datetime.timedelta(0)

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
if sport == "soccer_uefa_europa_league":
    sport = 'Soccer UEFA Europa League'
if sport == "soccer_spain_segunda_division":
    sport = 'Soccer Spanish Segunda Division'
if sport == "soccer_spain_la_liga":
    sport = 'Soccer Spanish Primera Division'
# Not sure what Greek Super League is listed as
if sport == "XXX":
    sport = 'Soccer Greek Super League'
if sport == "soccer_turkey_super_league":
    sport = 'Soccer Turkey Super League'
if sport == "soccer_italy_serie_a":
    sport = 'Soccer Italy Serie A'
if sport == "soccer_italy_serie_b":
    sport = 'Soccer Italy Serie B'
if sport == "soccer_portugal_primeira_liga":
    sport = 'Soccer Portuguese Liga'
if sport == "soccer_netherlands_eredivisie":
    sport = 'Soccer Dutch Eredivisie'
if sport == "soccer_belgium_first_div":
    sport = 'Soccer Belgian Jupiler League'
if sport == "china_superleague":
    sport = 'Soccer Chinese Super League'
if sport == "soccer_norway_eliteserien":
    sport = 'Soccer Norwegian Tippeligaen'
if sport == "soccer_switzerland_superleague":
    sport = 'Soccer Swiss Raiffeisen Super League'
if sport == "soccer_denmark_superliga":
    sport = 'Soccer Danish SAS-Ligaen'
if sport == "soccer_sweden_allsvenskan":
    sport = 'Soccer Swedish Allsvenskan'
if sport == "soccer":
    sport = 'Soccer'
if sport == "soccer_germany_bundesliga":
    sport = 'Soccer German Bundesliga'
if sport == "soccer_germany_bundesliga2":
    sport = 'Soccer German Bundesliga 2'
if sport == "soccer_russia_premier_league":
    sport = 'Soccer Russian Premier Liga'
if sport == "soccer_france_ligue_one":
    sport = 'Soccer French Ligue 1'
if sport == "soccer_france_ligue_two":
    sport = 'Soccer French Ligue 2'
if sport == "soccer_argentina_primera_division":
    sport = 'Soccer Argentina Primera Division'
if sport == "soccer_brazil_campeonato":
    sport = 'Soccer Brasileiro S√©rie A'
if sport == "soccer_japan_j_league":
    sport = 'Soccer Japanese J League'
if sport == "soccer_mexico_ligamx":
    sport = 'Soccer Mexican Primera Division Torneo Clausura'
if sport == "soccer_spl":
    sport = 'Soccer Scottish Premiership'
    
    
    
    

# Comment sport out if soccer
# sport = 'CFB'  
    

