# pylint: disable=E0401

import requests
import json
from API_Keys.vars import headers
import datetime

url = "https://odds.p.rapidapi.com/v1/odds"

#Retrieve API from Odds URL above

querystring = {"sport":"americanfootball_nfl","region":"us","mkt":"h2h"}

response = requests.request("GET", url, headers=headers, params=querystring)

sportsList = response.text

#Put into JSON fomat

gamesList = json.loads(sportsList)

theOddsAPIGames = gamesList['data']

#Slightly alter names so API teams are the same as 538 teams

for i in range(len(theOddsAPIGames)):
    for j in range(len(theOddsAPIGames[i]['sites'])):
        if (theOddsAPIGames[i]['teams'][0] == 'Arizona Cardinals'):
            theOddsAPIGames[i]['teams'][0] = 'ARI'

        if (theOddsAPIGames[i]['teams'][0] == 'Atlanta Falcons'):
            theOddsAPIGames[i]['teams'][0] = 'ATL'

        if (theOddsAPIGames[i]['teams'][0] == 'Baltimore Ravens'):
            theOddsAPIGames[i]['teams'][0] = 'BAL'

        if (theOddsAPIGames[i]['teams'][0] == 'Buffalo Bills'):
            theOddsAPIGames[i]['teams'][0] = 'BUF'

        if (theOddsAPIGames[i]['teams'][0] == 'Carolina Panthers'):
            theOddsAPIGames[i]['teams'][0] = 'CAR'

        if (theOddsAPIGames[i]['teams'][0] == 'Chicago Bears'):
            theOddsAPIGames[i]['teams'][0] = 'CHI'

        if (theOddsAPIGames[i]['teams'][0] == 'Cincinnati Bengals'):
            theOddsAPIGames[i]['teams'][0] = 'CIN'

        if (theOddsAPIGames[i]['teams'][0] == 'Cleveland Browns'):
            theOddsAPIGames[i]['teams'][0] = 'CLE'

        if (theOddsAPIGames[i]['teams'][0] == 'Dallas Cowboys'):
            theOddsAPIGames[i]['teams'][0] = 'DAL'

        if (theOddsAPIGames[i]['teams'][0] == 'Denver Broncos'):
            theOddsAPIGames[i]['teams'][0] = 'DEN'

        if (theOddsAPIGames[i]['teams'][0] == 'Detroit Lions'):
            theOddsAPIGames[i]['teams'][0] = 'DET'

        if (theOddsAPIGames[i]['teams'][0] == 'Green Bay Packers'):
            theOddsAPIGames[i]['teams'][0] = 'GB'

        if (theOddsAPIGames[i]['teams'][0] == 'Houston Texans'):
            theOddsAPIGames[i]['teams'][0] = 'HOU'

        if (theOddsAPIGames[i]['teams'][0] == 'Indianapolis Colts'):
            theOddsAPIGames[i]['teams'][0] = 'IND'

        if (theOddsAPIGames[i]['teams'][0] == 'Jacksonville Jaguars'):
            theOddsAPIGames[i]['teams'][0] = 'JAX'

        if (theOddsAPIGames[i]['teams'][0] == 'Kansas City Chiefs'):
            theOddsAPIGames[i]['teams'][0] = 'KC'

        if (theOddsAPIGames[i]['teams'][0] == 'Los Angeles Chargers'):
            theOddsAPIGames[i]['teams'][0] = 'LAC'

        if (theOddsAPIGames[i]['teams'][0] == 'Los Angeles Rams'):
            theOddsAPIGames[i]['teams'][0] = 'LAR'

        if (theOddsAPIGames[i]['teams'][0] == 'Miami Dolphins'):
            theOddsAPIGames[i]['teams'][0] = 'MIA'

        if (theOddsAPIGames[i]['teams'][0] == 'Minnesota Vikings'):
            theOddsAPIGames[i]['teams'][0] = 'MIN'

        if (theOddsAPIGames[i]['teams'][0] == 'New England Patriots'):
            theOddsAPIGames[i]['teams'][0] = 'NE'

        if (theOddsAPIGames[i]['teams'][0] == 'New Orleans Saints'):
            theOddsAPIGames[i]['teams'][0] = 'NO'

        if (theOddsAPIGames[i]['teams'][0] == 'New York Giants'):
            theOddsAPIGames[i]['teams'][0] = 'NYG'

        if (theOddsAPIGames[i]['teams'][0] == 'New York Jets'):
            theOddsAPIGames[i]['teams'][0] = 'NYJ'

        if (theOddsAPIGames[i]['teams'][0] == 'Las Vegas Raiders'):
            theOddsAPIGames[i]['teams'][0] = 'OAK'

        if (theOddsAPIGames[i]['teams'][0] == 'Philadelphia Eagles'):
            theOddsAPIGames[i]['teams'][0] = 'PHI'

        if (theOddsAPIGames[i]['teams'][0] == 'Pittsburgh Steelers'):
            theOddsAPIGames[i]['teams'][0] = 'PIT'

        if (theOddsAPIGames[i]['teams'][0] == 'San Francisco 49ers'):
            theOddsAPIGames[i]['teams'][0] = 'SF'

        if (theOddsAPIGames[i]['teams'][0] == 'Seattle Seahawks'):
            theOddsAPIGames[i]['teams'][0] = 'SEA'

        if (theOddsAPIGames[i]['teams'][0] == 'Tampa Bay Buccaneers'):
            theOddsAPIGames[i]['teams'][0] = 'TB'

        if (theOddsAPIGames[i]['teams'][0] == 'Tennessee Titans'):
            theOddsAPIGames[i]['teams'][0] = 'TEN'

        if (theOddsAPIGames[i]['teams'][0] == 'Washington Football Team'):
            theOddsAPIGames[i]['teams'][0] = 'WSH'

        if (theOddsAPIGames[i]['teams'][1] == 'Arizona Cardinals'):
            theOddsAPIGames[i]['teams'][1] = 'ARI'

        if (theOddsAPIGames[i]['teams'][1] == 'Atlanta Falcons'):
            theOddsAPIGames[i]['teams'][1] = 'ATL'

        if (theOddsAPIGames[i]['teams'][1] == 'Baltimore Ravens'):
            theOddsAPIGames[i]['teams'][1] = 'BAL'

        if (theOddsAPIGames[i]['teams'][1] == 'Buffalo Bills'):
            theOddsAPIGames[i]['teams'][1] = 'BUF'

        if (theOddsAPIGames[i]['teams'][1] == 'Carolina Panthers'):
            theOddsAPIGames[i]['teams'][1] = 'CAR'

        if (theOddsAPIGames[i]['teams'][1] == 'Chicago Bears'):
            theOddsAPIGames[i]['teams'][1] = 'CHI'

        if (theOddsAPIGames[i]['teams'][1] == 'Cincinnati Bengals'):
            theOddsAPIGames[i]['teams'][1] = 'CIN'

        if (theOddsAPIGames[i]['teams'][1] == 'Cleveland Browns'):
            theOddsAPIGames[i]['teams'][1] = 'CLE'

        if (theOddsAPIGames[i]['teams'][1] == 'Dallas Cowboys'):
            theOddsAPIGames[i]['teams'][1] = 'DAL'

        if (theOddsAPIGames[i]['teams'][1] == 'Denver Broncos'):
            theOddsAPIGames[i]['teams'][1] = 'DEN'

        if (theOddsAPIGames[i]['teams'][1] == 'Detroit Lions'):
            theOddsAPIGames[i]['teams'][1] = 'DET'

        if (theOddsAPIGames[i]['teams'][1] == 'Green Bay Packers'):
            theOddsAPIGames[i]['teams'][1] = 'GB'

        if (theOddsAPIGames[i]['teams'][1] == 'Houston Texans'):
            theOddsAPIGames[i]['teams'][1] = 'HOU'

        if (theOddsAPIGames[i]['teams'][1] == 'Indianapolis Colts'):
            theOddsAPIGames[i]['teams'][1] = 'IND'

        if (theOddsAPIGames[i]['teams'][1] == 'Jacksonville Jaguars'):
            theOddsAPIGames[i]['teams'][1] = 'JAX'

        if (theOddsAPIGames[i]['teams'][1] == 'Kansas City Chiefs'):
            theOddsAPIGames[i]['teams'][1] = 'KC'

        if (theOddsAPIGames[i]['teams'][1] == 'Los Angeles Chargers'):
            theOddsAPIGames[i]['teams'][1] = 'LAC'

        if (theOddsAPIGames[i]['teams'][1] == 'Los Angeles Rams'):
            theOddsAPIGames[i]['teams'][1] = 'LAR'

        if (theOddsAPIGames[i]['teams'][1] == 'Miami Dolphins'):
            theOddsAPIGames[i]['teams'][1] = 'MIA'

        if (theOddsAPIGames[i]['teams'][1] == 'Minnesota Vikings'):
            theOddsAPIGames[i]['teams'][1] = 'MIN'

        if (theOddsAPIGames[i]['teams'][1] == 'New England Patriots'):
            theOddsAPIGames[i]['teams'][1] = 'NE'

        if (theOddsAPIGames[i]['teams'][1] == 'New Orleans Saints'):
            theOddsAPIGames[i]['teams'][1] = 'NO'

        if (theOddsAPIGames[i]['teams'][1] == 'New York Giants'):
            theOddsAPIGames[i]['teams'][1] = 'NYG'

        if (theOddsAPIGames[i]['teams'][1] == 'New York Jets'):
            theOddsAPIGames[i]['teams'][1] = 'NYJ'

        if (theOddsAPIGames[i]['teams'][1] == 'Las Vegas Raiders'):
            theOddsAPIGames[i]['teams'][1] = 'OAK'

        if (theOddsAPIGames[i]['teams'][1] == 'Philadelphia Eagles'):
            theOddsAPIGames[i]['teams'][1] = 'PHI'

        if (theOddsAPIGames[i]['teams'][1] == 'Pittsburgh Steelers'):
            theOddsAPIGames[i]['teams'][1] = 'PIT'

        if (theOddsAPIGames[i]['teams'][1] == 'San Francisco 49ers'):
            theOddsAPIGames[i]['teams'][1] = 'SF'

        if (theOddsAPIGames[i]['teams'][1] == 'Seattle Seahawks'):
            theOddsAPIGames[i]['teams'][1] = 'SEA'

        if (theOddsAPIGames[i]['teams'][1] == 'Tampa Bay Buccaneers'):
            theOddsAPIGames[i]['teams'][1] = 'TB'

        if (theOddsAPIGames[i]['teams'][1] == 'Tennessee Titans'):
            theOddsAPIGames[i]['teams'][1] = 'TEN'

        if (theOddsAPIGames[i]['teams'][1] == 'Washington Football Team'):
            theOddsAPIGames[i]['teams'][1] = 'WSH'
