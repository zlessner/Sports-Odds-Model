# pylint: disable=E0401

import requests
import json
from API_Keys.vars import headers 
import datetime

url = "https://odds.p.rapidapi.com/v1/odds"

#Retrieve API from Odds URL above

querystring = {"sport":"basketball_nba","region":"us","mkt":"h2h"}

response = requests.request("GET", url, headers=headers, params=querystring)

sportsList = response.text

#Put into JSON fomat

gamesList = json.loads(sportsList)

theOddsAPIGames = gamesList['data']

#Slightly alter names so API teams are the same as 538 teams

for i in range(len(theOddsAPIGames)):
    for j in range(len(theOddsAPIGames[i]['sites'])):
        if (theOddsAPIGames[i]['teams'][0] == 'Chicago Bulls'):
            theOddsAPIGames[i]['teams'][0] = 'CHI'

        if (theOddsAPIGames[i]['teams'][0] == 'Charlotte Hornets'):
            theOddsAPIGames[i]['teams'][0] = 'CHO'

        if (theOddsAPIGames[i]['teams'][0] == 'Denver Nuggets'):
            theOddsAPIGames[i]['teams'][0] = 'DEN'

        if (theOddsAPIGames[i]['teams'][0] == 'Detroit Pistons'):
            theOddsAPIGames[i]['teams'][0] = 'DET'

        if (theOddsAPIGames[i]['teams'][0] == 'Golden State Warriors'):
            theOddsAPIGames[i]['teams'][0] = 'GSW'

        if (theOddsAPIGames[i]['teams'][0] == 'Los Angeles Clippers'):
            theOddsAPIGames[i]['teams'][0] = 'LAC'

        if (theOddsAPIGames[i]['teams'][0] == 'Los Angeles Lakers'):
            theOddsAPIGames[i]['teams'][0] = 'LAL'

        if (theOddsAPIGames[i]['teams'][0] == 'Miami Heat'):
            theOddsAPIGames[i]['teams'][0] = 'MIA'

        if (theOddsAPIGames[i]['teams'][0] == 'Milwaukee Bucks'):
            theOddsAPIGames[i]['teams'][0] = 'MIL'

        if (theOddsAPIGames[i]['teams'][0] == 'Minnesota Timberwolves'):
            theOddsAPIGames[i]['teams'][0] = 'MIN'

        if (theOddsAPIGames[i]['teams'][0] == 'New Orleans Pelicans'):
            theOddsAPIGames[i]['teams'][0] = 'NOP'

        if (theOddsAPIGames[i]['teams'][0] == 'New York Knicks'):
            theOddsAPIGames[i]['teams'][0] = 'NYK'

        if (theOddsAPIGames[i]['teams'][0] == 'Oklahoma City Thunder'):
            theOddsAPIGames[i]['teams'][0] = 'OKC'

        if (theOddsAPIGames[i]['teams'][0] == 'Philadelphia 76ers'):
            theOddsAPIGames[i]['teams'][0] = 'PHI'

        if (theOddsAPIGames[i]['teams'][0] == 'Phoenix Suns'):
            theOddsAPIGames[i]['teams'][0] = 'PHO'

        if (theOddsAPIGames[i]['teams'][0] == 'Sacramento Kings'):
            theOddsAPIGames[i]['teams'][0] = 'SAC'

        if (theOddsAPIGames[i]['teams'][0] == 'San Antonio Spurs'):
            theOddsAPIGames[i]['teams'][0] = 'SAS'

        if (theOddsAPIGames[i]['teams'][0] == 'Atlanta Hawks'):
            theOddsAPIGames[i]['teams'][0] = 'ATL'

        if (theOddsAPIGames[i]['teams'][0] == 'Boston Celtics'):
            theOddsAPIGames[i]['teams'][0] = 'BOS'

        if (theOddsAPIGames[i]['teams'][0] == 'Brooklyn Nets'):
            theOddsAPIGames[i]['teams'][0] = 'BRK'

        if (theOddsAPIGames[i]['teams'][0] == 'Cleveland Cavaliers'):
            theOddsAPIGames[i]['teams'][0] = 'CLE'

        if (theOddsAPIGames[i]['teams'][0] == 'Dallas Mavericks'):
            theOddsAPIGames[i]['teams'][0] = 'DAL'

        if (theOddsAPIGames[i]['teams'][0] == 'Houston Rockets'):
            theOddsAPIGames[i]['teams'][0] = 'HOU'

        if (theOddsAPIGames[i]['teams'][0] == 'Indiana Pacers'):
            theOddsAPIGames[i]['teams'][0] = 'IND'

        if (theOddsAPIGames[i]['teams'][0] == 'Memphis Grizzlies'):
            theOddsAPIGames[i]['teams'][0] = 'MEM'

        if (theOddsAPIGames[i]['teams'][0] == 'Orlando Magic'):
            theOddsAPIGames[i]['teams'][0] = 'ORL'

        if (theOddsAPIGames[i]['teams'][0] == 'Portland Trail Blazers'):
            theOddsAPIGames[i]['teams'][0] = 'POR'

        if (theOddsAPIGames[i]['teams'][0] == 'Toronto Raptors'):
            theOddsAPIGames[i]['teams'][0] = 'TOR'

        if (theOddsAPIGames[i]['teams'][0] == 'Utah Jazz'):
            theOddsAPIGames[i]['teams'][0] = 'UTA'

        if (theOddsAPIGames[i]['teams'][0] == 'Washington Wizards'):
            theOddsAPIGames[i]['teams'][0] = 'WAS'

        if (theOddsAPIGames[i]['teams'][1] == 'Chicago Bulls'):
            theOddsAPIGames[i]['teams'][1] = 'CHI'

        if (theOddsAPIGames[i]['teams'][1] == 'Charlotte Hornets'):
            theOddsAPIGames[i]['teams'][1] = 'CHO'

        if (theOddsAPIGames[i]['teams'][1] == 'Denver Nuggets'):
            theOddsAPIGames[i]['teams'][1] = 'DEN'

        if (theOddsAPIGames[i]['teams'][1] == 'Detroit Pistons'):
            theOddsAPIGames[i]['teams'][1] = 'DET'

        if (theOddsAPIGames[i]['teams'][1] == 'Golden State Warriors'):
            theOddsAPIGames[i]['teams'][1] = 'GSW'

        if (theOddsAPIGames[i]['teams'][1] == 'Los Angeles Clippers'):
            theOddsAPIGames[i]['teams'][1] = 'LAC'

        if (theOddsAPIGames[i]['teams'][1] == 'Los Angeles Lakers'):
            theOddsAPIGames[i]['teams'][1] = 'LAL'

        if (theOddsAPIGames[i]['teams'][1] == 'Miami Heat'):
            theOddsAPIGames[i]['teams'][1] = 'MIA'

        if (theOddsAPIGames[i]['teams'][1] == 'Milwaukee Bucks'):
            theOddsAPIGames[i]['teams'][1] = 'MIL'

        if (theOddsAPIGames[i]['teams'][1] == 'Minnesota Timberwolves'):
            theOddsAPIGames[i]['teams'][1] = 'MIN'

        if (theOddsAPIGames[i]['teams'][1] == 'New Orleans Pelicans'):
            theOddsAPIGames[i]['teams'][1] = 'NOP'

        if (theOddsAPIGames[i]['teams'][1] == 'New York Knicks'):
            theOddsAPIGames[i]['teams'][1] = 'NYK'

        if (theOddsAPIGames[i]['teams'][1] == 'Oklahoma City Thunder'):
            theOddsAPIGames[i]['teams'][1] = 'OKC'

        if (theOddsAPIGames[i]['teams'][1] == 'Philadelphia 76ers'):
            theOddsAPIGames[i]['teams'][1] = 'PHI'

        if (theOddsAPIGames[i]['teams'][1] == 'Phoenix Suns'):
            theOddsAPIGames[i]['teams'][1] = 'PHO'

        if (theOddsAPIGames[i]['teams'][1] == 'Sacramento Kings'):
            theOddsAPIGames[i]['teams'][1] = 'SAC'

        if (theOddsAPIGames[i]['teams'][1] == 'San Antonio Spurs'):
            theOddsAPIGames[i]['teams'][1] = 'SAS'

        if (theOddsAPIGames[i]['teams'][1] == 'Atlanta Hawks'):
            theOddsAPIGames[i]['teams'][1] = 'ATL'

        if (theOddsAPIGames[i]['teams'][1] == 'Boston Celtics'):
            theOddsAPIGames[i]['teams'][1] = 'BOS'

        if (theOddsAPIGames[i]['teams'][1] == 'Brooklyn Nets'):
            theOddsAPIGames[i]['teams'][1] = 'BRK'

        if (theOddsAPIGames[i]['teams'][1] == 'Cleveland Cavaliers'):
            theOddsAPIGames[i]['teams'][1] = 'CLE'

        if (theOddsAPIGames[i]['teams'][1] == 'Dallas Mavericks'):
            theOddsAPIGames[i]['teams'][1] = 'DAL'

        if (theOddsAPIGames[i]['teams'][1] == 'Houston Rockets'):
            theOddsAPIGames[i]['teams'][1] = 'HOU'

        if (theOddsAPIGames[i]['teams'][1] == 'Indiana Pacers'):
            theOddsAPIGames[i]['teams'][1] = 'IND'

        if (theOddsAPIGames[i]['teams'][1] == 'Memphis Grizzlies'):
            theOddsAPIGames[i]['teams'][1] = 'MEM'

        if (theOddsAPIGames[i]['teams'][1] == 'Orlando Magic'):
            theOddsAPIGames[i]['teams'][1] = 'ORL'

        if (theOddsAPIGames[i]['teams'][1] == 'Portland Trail Blazers'):
            theOddsAPIGames[i]['teams'][1] = 'POR'

        if (theOddsAPIGames[i]['teams'][1] == 'Toronto Raptors'):
            theOddsAPIGames[i]['teams'][1] = 'TOR'

        if (theOddsAPIGames[i]['teams'][1] == 'Utah Jazz'):
            theOddsAPIGames[i]['teams'][1] = 'UTA'

        if (theOddsAPIGames[i]['teams'][1] == 'Washington Wizards'):
            theOddsAPIGames[i]['teams'][1] = 'WAS'

        if (theOddsAPIGames[i]['home_team'] == 'Chicago Bulls'):
            theOddsAPIGames[i]['home_team'] = 'CHI'

        if (theOddsAPIGames[i]['home_team'] == 'Charlotte Hornets'):
            theOddsAPIGames[i]['home_team'] = 'CHO'

        if (theOddsAPIGames[i]['home_team'] == 'Denver Nuggets'):
            theOddsAPIGames[i]['home_team'] = 'DEN'

        if (theOddsAPIGames[i]['home_team'] == 'Detroit Pistons'):
            theOddsAPIGames[i]['home_team'] = 'DET'

        if (theOddsAPIGames[i]['home_team'] == 'Golden State Warriors'):
            theOddsAPIGames[i]['home_team'] = 'GSW'

        if (theOddsAPIGames[i]['home_team'] == 'Los Angeles Clippers'):
            theOddsAPIGames[i]['home_team'] = 'LAC'

        if (theOddsAPIGames[i]['home_team'] == 'Los Angeles Lakers'):
            theOddsAPIGames[i]['home_team'] = 'LAL'

        if (theOddsAPIGames[i]['home_team'] == 'Miami Heat'):
            theOddsAPIGames[i]['home_team'] = 'MIA'

        if (theOddsAPIGames[i]['home_team'] == 'Milwaukee Bucks'):
            theOddsAPIGames[i]['home_team'] = 'MIL'

        if (theOddsAPIGames[i]['home_team'] == 'Minnesota Timberwolves'):
            theOddsAPIGames[i]['home_team'] = 'MIN'

        if (theOddsAPIGames[i]['home_team'] == 'New Orleans Pelicans'):
            theOddsAPIGames[i]['home_team'] = 'NOP'

        if (theOddsAPIGames[i]['home_team'] == 'New York Knicks'):
            theOddsAPIGames[i]['home_team'] = 'NYK'

        if (theOddsAPIGames[i]['home_team'] == 'Oklahoma City Thunder'):
            theOddsAPIGames[i]['home_team'] = 'OKC'

        if (theOddsAPIGames[i]['home_team'] == 'Philadelphia 76ers'):
            theOddsAPIGames[i]['home_team'] = 'PHI'

        if (theOddsAPIGames[i]['home_team'] == 'Phoenix Suns'):
            theOddsAPIGames[i]['home_team'] = 'PHO'

        if (theOddsAPIGames[i]['home_team'] == 'Sacramento Kings'):
            theOddsAPIGames[i]['home_team'] = 'SAC'

        if (theOddsAPIGames[i]['home_team'] == 'San Antonio Spurs'):
            theOddsAPIGames[i]['home_team'] = 'SAS'

        if (theOddsAPIGames[i]['home_team'] == 'Atlanta Hawks'):
            theOddsAPIGames[i]['home_team'] = 'ATL'

        if (theOddsAPIGames[i]['home_team'] == 'Boston Celtics'):
            theOddsAPIGames[i]['home_team'] = 'BOS'

        if (theOddsAPIGames[i]['home_team'] == 'Brooklyn Nets'):
            theOddsAPIGames[i]['home_team'] = 'BRK'

        if (theOddsAPIGames[i]['home_team'] == 'Cleveland Cavaliers'):
            theOddsAPIGames[i]['home_team'] = 'CLE'

        if (theOddsAPIGames[i]['home_team'] == 'Dallas Mavericks'):
            theOddsAPIGames[i]['home_team'] = 'DAL'

        if (theOddsAPIGames[i]['home_team'] == 'Houston Rockets'):
            theOddsAPIGames[i]['home_team'] = 'HOU'

        if (theOddsAPIGames[i]['home_team'] == 'Indiana Pacers'):
            theOddsAPIGames[i]['home_team'] = 'IND'

        if (theOddsAPIGames[i]['home_team'] == 'Memphis Grizzlies'):
            theOddsAPIGames[i]['home_team'] = 'MEM'

        if (theOddsAPIGames[i]['home_team'] == 'Orlando Magic'):
            theOddsAPIGames[i]['home_team'] = 'ORL'

        if (theOddsAPIGames[i]['home_team'] == 'Portland Trail Blazers'):
            theOddsAPIGames[i]['home_team'] = 'POR'

        if (theOddsAPIGames[i]['home_team'] == 'Toronto Raptors'):
            theOddsAPIGames[i]['home_team'] = 'TOR'

        if (theOddsAPIGames[i]['home_team'] == 'Utah Jazz'):
            theOddsAPIGames[i]['home_team'] = 'UTA'

        if (theOddsAPIGames[i]['home_team'] == 'Washington Wizards'):
            theOddsAPIGames[i]['home_team'] = 'WAS'

