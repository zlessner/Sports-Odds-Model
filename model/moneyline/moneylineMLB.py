import requests
import json
import os
from API_Keys.vars import headers
import datetime

url = "https://odds.p.rapidapi.com/v1/odds"

#Retrieve API from Odds URL above

querystring = {"sport":"baseball_mlb","region":"us","mkt":"h2h"}

response = requests.request("GET", url, headers=headers, params=querystring)

sportsList = response.text

#Put into JSON fomat

gamesList = json.loads(sportsList)

theOddsAPIGames = gamesList['data']

# Slightly alter names so API teams are the same as 538 teams

for i in range(len(theOddsAPIGames)):
    for j in range(len(theOddsAPIGames[i]['sites'])):
        if (theOddsAPIGames[i]['teams'][0] == 'Arizona Diamondbacks'):
            theOddsAPIGames[i]['teams'][0] = 'ARI'

        if (theOddsAPIGames[i]['teams'][0] == 'Atlanta Braves'):
            theOddsAPIGames[i]['teams'][0] = 'ATL'

        if (theOddsAPIGames[i]['teams'][0] == 'Baltimore Orioles'):
            theOddsAPIGames[i]['teams'][0] = 'BAL'

        if (theOddsAPIGames[i]['teams'][0] == 'Boston Red Sox'):
            theOddsAPIGames[i]['teams'][0] = 'BOS'

        if (theOddsAPIGames[i]['teams'][0] == 'Chicago White Sox'):
            theOddsAPIGames[i]['teams'][0] = 'CHW'

        if (theOddsAPIGames[i]['teams'][0] == 'Chicago Cubs'):
            theOddsAPIGames[i]['teams'][0] = 'CHC'

        if (theOddsAPIGames[i]['teams'][0] == 'Cincinnati Reds'):
            theOddsAPIGames[i]['teams'][0] = 'CIN'

        if (theOddsAPIGames[i]['teams'][0] == 'Cleveland Indians'):
            theOddsAPIGames[i]['teams'][0] = 'CLE'

        if (theOddsAPIGames[i]['teams'][0] == 'Colorado Rockies'):
            theOddsAPIGames[i]['teams'][0] = 'COL'

        if (theOddsAPIGames[i]['teams'][0] == 'Detroit Tigers'):
            theOddsAPIGames[i]['teams'][0] = 'DET'

        if (theOddsAPIGames[i]['teams'][0] == 'Houston Astros'):
            theOddsAPIGames[i]['teams'][0] = 'HOU'

        if (theOddsAPIGames[i]['teams'][0] == 'Kansas City Royals'):
            theOddsAPIGames[i]['teams'][0] = 'KCR'

        if (theOddsAPIGames[i]['teams'][0] == 'Los Angeles Angels'):
            theOddsAPIGames[i]['teams'][0] = 'ANA'

        if (theOddsAPIGames[i]['teams'][0] == 'Los Angeles Dodgers'):
            theOddsAPIGames[i]['teams'][0] = 'LAD'

        if (theOddsAPIGames[i]['teams'][0] == 'Miami Marlins'):
            theOddsAPIGames[i]['teams'][0] = 'FLA'

        if (theOddsAPIGames[i]['teams'][0] == 'Milwaukee Brewers'):
            theOddsAPIGames[i]['teams'][0] = 'MIL'

        if (theOddsAPIGames[i]['teams'][0] == 'Minnesota Twins'):
            theOddsAPIGames[i]['teams'][0] = 'MIN'

        if (theOddsAPIGames[i]['teams'][0] == 'New York Yankees'):
            theOddsAPIGames[i]['teams'][0] = 'NYY'

        if (theOddsAPIGames[i]['teams'][0] == 'New York Mets'):
            theOddsAPIGames[i]['teams'][0] = 'NYM'

        if (theOddsAPIGames[i]['teams'][0] == 'Oakland Athletics'):
            theOddsAPIGames[i]['teams'][0] = 'OAK'

        if (theOddsAPIGames[i]['teams'][0] == 'Philadelphia Phillies'):
            theOddsAPIGames[i]['teams'][0] = 'PHI'

        if (theOddsAPIGames[i]['teams'][0] == 'Pittsburgh Pirates'):
            theOddsAPIGames[i]['teams'][0] = 'PIT'

        if (theOddsAPIGames[i]['teams'][0] == 'San Diego Padres'):
            theOddsAPIGames[i]['teams'][0] = 'SDP'

        if (theOddsAPIGames[i]['teams'][0] == 'San Francisco Giants'):
            theOddsAPIGames[i]['teams'][0] = 'SFG'

        if (theOddsAPIGames[i]['teams'][0] == 'Seattle Mariners'):
            theOddsAPIGames[i]['teams'][0] = 'SEA'

        if (theOddsAPIGames[i]['teams'][0] == 'St. Louis Cardinals'):
            theOddsAPIGames[i]['teams'][0] = 'STL'

        if (theOddsAPIGames[i]['teams'][0] == 'Tampa Bay Rays'):
            theOddsAPIGames[i]['teams'][0] = 'TBD'

        if (theOddsAPIGames[i]['teams'][0] == 'Texas Rangers'):
            theOddsAPIGames[i]['teams'][0] = 'TEX'

        if (theOddsAPIGames[i]['teams'][0] == 'Toronto Blue Jays'):
            theOddsAPIGames[i]['teams'][0] = 'TOR'

        if (theOddsAPIGames[i]['teams'][0] == 'Washington Nationals'):
            theOddsAPIGames[i]['teams'][0] = 'WSN'

        if (theOddsAPIGames[i]['teams'][1] == 'Arizona Diamondbacks'):
            theOddsAPIGames[i]['teams'][1] = 'ARI'

        if (theOddsAPIGames[i]['teams'][1] == 'Atlanta Braves'):
            theOddsAPIGames[i]['teams'][1] = 'ATL'

        if (theOddsAPIGames[i]['teams'][1] == 'Baltimore Orioles'):
            theOddsAPIGames[i]['teams'][1] = 'BAL'

        if (theOddsAPIGames[i]['teams'][1] == 'Boston Red Sox'):
            theOddsAPIGames[i]['teams'][1] = 'BOS'

        if (theOddsAPIGames[i]['teams'][1] == 'Chicago White Sox'):
            theOddsAPIGames[i]['teams'][1] = 'CHW'

        if (theOddsAPIGames[i]['teams'][1] == 'Chicago Cubs'):
            theOddsAPIGames[i]['teams'][1] = 'CHC'

        if (theOddsAPIGames[i]['teams'][1] == 'Cincinnati Reds'):
            theOddsAPIGames[i]['teams'][1] = 'CIN'

        if (theOddsAPIGames[i]['teams'][1] == 'Cleveland Indians'):
            theOddsAPIGames[i]['teams'][1] = 'CLE'

        if (theOddsAPIGames[i]['teams'][1] == 'Colorado Rockies'):
            theOddsAPIGames[i]['teams'][1] = 'COL'

        if (theOddsAPIGames[i]['teams'][1] == 'Detroit Tigers'):
            theOddsAPIGames[i]['teams'][1] = 'DET'

        if (theOddsAPIGames[i]['teams'][1] == 'Houston Astros'):
            theOddsAPIGames[i]['teams'][1] = 'HOU'

        if (theOddsAPIGames[i]['teams'][1] == 'Kansas City Royals'):
            theOddsAPIGames[i]['teams'][1] = 'KCR'

        if (theOddsAPIGames[i]['teams'][1] == 'Los Angeles Angels'):
            theOddsAPIGames[i]['teams'][1] = 'ANA'

        if (theOddsAPIGames[i]['teams'][1] == 'Los Angeles Dodgers'):
            theOddsAPIGames[i]['teams'][1] = 'LAD'

        if (theOddsAPIGames[i]['teams'][1] == 'Miami Marlins'):
            theOddsAPIGames[i]['teams'][1] = 'FLA'

        if (theOddsAPIGames[i]['teams'][1] == 'Milwaukee Brewers'):
            theOddsAPIGames[i]['teams'][1] = 'MIL'

        if (theOddsAPIGames[i]['teams'][1] == 'Minnesota Twins'):
            theOddsAPIGames[i]['teams'][1] = 'MIN'

        if (theOddsAPIGames[i]['teams'][1] == 'New York Yankees'):
            theOddsAPIGames[i]['teams'][1] = 'NYY'

        if (theOddsAPIGames[i]['teams'][1] == 'New York Mets'):
            theOddsAPIGames[i]['teams'][1] = 'NYM'

        if (theOddsAPIGames[i]['teams'][1] == 'Oakland Athletics'):
            theOddsAPIGames[i]['teams'][1] = 'OAK'

        if (theOddsAPIGames[i]['teams'][1] == 'Philadelphia Phillies'):
            theOddsAPIGames[i]['teams'][1] = 'PHI'

        if (theOddsAPIGames[i]['teams'][1] == 'Pittsburgh Pirates'):
            theOddsAPIGames[i]['teams'][1] = 'PIT'

        if (theOddsAPIGames[i]['teams'][1] == 'San Diego Padres'):
            theOddsAPIGames[i]['teams'][1] = 'SDP'

        if (theOddsAPIGames[i]['teams'][1] == 'San Francisco Giants'):
            theOddsAPIGames[i]['teams'][1] = 'SFG'

        if (theOddsAPIGames[i]['teams'][1] == 'Seattle Mariners'):
            theOddsAPIGames[i]['teams'][1] = 'SEA'

        if (theOddsAPIGames[i]['teams'][1] == 'St. Louis Cardinals'):
            theOddsAPIGames[i]['teams'][1] = 'STL'

        if (theOddsAPIGames[i]['teams'][1] == 'Tampa Bay Rays'):
            theOddsAPIGames[i]['teams'][1] = 'TBD'

        if (theOddsAPIGames[i]['teams'][1] == 'Texas Rangers'):
            theOddsAPIGames[i]['teams'][1] = 'TEX'

        if (theOddsAPIGames[i]['teams'][1] == 'Toronto Blue Jays'):
            theOddsAPIGames[i]['teams'][1] = 'TOR'

        if (theOddsAPIGames[i]['teams'][1] == 'Washington Nationals'):
            theOddsAPIGames[i]['teams'][1] = 'WSN'
