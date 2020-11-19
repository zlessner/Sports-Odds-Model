from urllib.request import urlretrieve as retrieve
from moneyline.moneylineNFL import theOddsAPIGames
from moneyline.moneylineSoccer import gameDate, gameWeek
import csv
import time
from datetime import datetime
import pandas as pd
# from nflPredictionTracker import predictionTracker


stringGameDate = str(gameDate)
stringGameWeek= str(gameWeek)

url = 'https://projects.fivethirtyeight.com/nfl-api/nfl_elo_latest.csv'

url2 = 'https://thepredictiontracker.com/nflpredictions.csv'

retrieve(url,'nfl.csv')

f = open('nfl.csv', 'r')

retrieve(url2,'nfl2.csv')

f2 = open('nfl2.csv', 'r')



reader = csv.reader(f)
next(reader)


reader2 = csv.reader(f2)
next(reader2)




fullList=[]

fullList2=[]

#Parse CSV file for sport, teams, and odds for both 538 and thepredictiontracker

for row in reader:
    fullList.append([row[0], row[4], row[5], row[20], row[21]])


for row2 in reader2:
    fullList2.append([row2[3], row2[2], float(row2[72]), 1-float(row2[72])])


predictionTracker = []

for i in range(len(fullList2)):
    if fullList2[i][0] != fullList2[i-1][0]:
        predictionTracker.append(fullList2[i])



FiveThirtyEightGames=[]



#Making sure the game occurs in that NFL week

for game in fullList:
    if game[0] >= stringGameDate and game[0] <= stringGameWeek:
        FiveThirtyEightGames.append(game)




for i in range(len(predictionTracker)):
        if (predictionTracker[i][0] == 'Arizona'):
            predictionTracker[i][0] = 'ARI'

        if (predictionTracker[i][0] == 'Atlanta'):
            predictionTracker[i][0] = 'ATL'

        if (predictionTracker[i][0] == 'Baltimore'):
            predictionTracker[i][0] = 'BAL'

        if (predictionTracker[i][0] == 'Buffalo'):
            predictionTracker[i][0] = 'BUF'

        if (predictionTracker[i][0] == 'Carolina'):
            predictionTracker[i][0] = 'CAR'

        if (predictionTracker[i][0] == 'Chicago'):
            predictionTracker[i][0] = 'CHI'

        if (predictionTracker[i][0] == 'Cincinnati'):
            predictionTracker[i][0] = 'CIN'

        if (predictionTracker[i][0] == 'Cleveland'):
            predictionTracker[i][0] = 'CLE'

        if (predictionTracker[i][0] == 'Dallas'):
            predictionTracker[i][0] = 'DAL'

        if (predictionTracker[i][0] == 'Denver'):
            predictionTracker[i][0] = 'DEN'

        if (predictionTracker[i][0] == 'Detroit'):
            predictionTracker[i][0] = 'DET'

        if (predictionTracker[i][0] == 'Green Bay'):
            predictionTracker[i][0] = 'GB'

        if (predictionTracker[i][0] == 'Houston'):
            predictionTracker[i][0] = 'HOU'

        if (predictionTracker[i][0] == 'Indianapolis'):
            predictionTracker[i][0] = 'IND'

        if (predictionTracker[i][0] == 'Jacksonville'):
            predictionTracker[i][0] = 'JAX'

        if (predictionTracker[i][0] == 'Kansas City'):
            predictionTracker[i][0] = 'KC'

        if (predictionTracker[i][0] == 'LA Chargers'):
            predictionTracker[i][0] = 'LAC'

        if (predictionTracker[i][0] == 'LA Rams'):
            predictionTracker[i][0] = 'LAR'

        if (predictionTracker[i][0] == 'Miami'):
            predictionTracker[i][0] = 'MIA'

        if (predictionTracker[i][0] == 'Minnesota'):
            predictionTracker[i][0] = 'MIN'

        if (predictionTracker[i][0] == 'New England'):
            predictionTracker[i][0] = 'NE'

        if (predictionTracker[i][0] == 'New Orleans'):
            predictionTracker[i][0] = 'NO'

        if (predictionTracker[i][0] == 'N.Y. Giants'):
            predictionTracker[i][0] = 'NYG'

        if (predictionTracker[i][0] == 'N.Y. Jets'):
            predictionTracker[i][0] = 'NYJ'

        if (predictionTracker[i][0] == 'Las Vegas'):
            predictionTracker[i][0] = 'OAK'

        if (predictionTracker[i][0] == 'Philadelphia'):
            predictionTracker[i][0] = 'PHI'

        if (predictionTracker[i][0] == 'Pittsburgh'):
            predictionTracker[i][0] = 'PIT'

        if (predictionTracker[i][0] == 'San Francisco'):
            predictionTracker[i][0] = 'SF'

        if (predictionTracker[i][0] == 'Seattle'):
            predictionTracker[i][0] = 'SEA'

        if (predictionTracker[i][0] == 'Tampa Bay'):
            predictionTracker[i][0] = 'TB'

        if (predictionTracker[i][0] == 'Tennessee'):
            predictionTracker[i][0] = 'TEN'

        if (predictionTracker[i][0] == 'Washington'):
            predictionTracker[i][0] = 'WSH'

        if (predictionTracker[i][1] == 'Arizona'):
            predictionTracker[i][1] = 'ARI'

        if (predictionTracker[i][1] == 'Atlanta'):
            predictionTracker[i][1] = 'ATL'

        if (predictionTracker[i][1] == 'Baltimore'):
            predictionTracker[i][1] = 'BAL'

        if (predictionTracker[i][1] == 'Buffalo'):
            predictionTracker[i][1] = 'BUF'

        if (predictionTracker[i][1] == 'Carolina'):
            predictionTracker[i][1] = 'CAR'

        if (predictionTracker[i][1] == 'Chicago'):
            predictionTracker[i][1] = 'CHI'

        if (predictionTracker[i][1] == 'Cincinnati'):
            predictionTracker[i][1] = 'CIN'

        if (predictionTracker[i][1] == 'Cleveland'):
            predictionTracker[i][1] = 'CLE'

        if (predictionTracker[i][1] == 'Dallas'):
            predictionTracker[i][1] = 'DAL'

        if (predictionTracker[i][1] == 'Denver'):
            predictionTracker[i][1] = 'DEN'

        if (predictionTracker[i][1] == 'Detroit'):
            predictionTracker[i][1] = 'DET'

        if (predictionTracker[i][1] == 'Green Bay'):
            predictionTracker[i][1] = 'GB'

        if (predictionTracker[i][1] == 'Houston'):
            predictionTracker[i][1] = 'HOU'

        if (predictionTracker[i][1] == 'Indianapolis'):
            predictionTracker[i][1] = 'IND'

        if (predictionTracker[i][1] == 'Jacksonville'):
            predictionTracker[i][1] = 'JAX'

        if (predictionTracker[i][1] == 'Kansas City'):
            predictionTracker[i][1] = 'KC'

        if (predictionTracker[i][1] == 'LA Chargers'):
            predictionTracker[i][1] = 'LAC'

        if (predictionTracker[i][1] == 'LA Rams'):
            predictionTracker[i][1] = 'LAR'

        if (predictionTracker[i][1] == 'Miami'):
            predictionTracker[i][1] = 'MIA'

        if (predictionTracker[i][1] == 'Minnesota'):
            predictionTracker[i][1] = 'MIN'

        if (predictionTracker[i][1] == 'New England'):
            predictionTracker[i][1] = 'NE'

        if (predictionTracker[i][1] == 'New Orleans'):
            predictionTracker[i][1] = 'NO'

        if (predictionTracker[i][1] == 'N.Y. Giants'):
            predictionTracker[i][1] = 'NYG'

        if (predictionTracker[i][1] == 'N.Y. Jets'):
            predictionTracker[i][1] = 'NYJ'

        if (predictionTracker[i][1] == 'Las Vegas'):
            predictionTracker[i][1] = 'OAK'

        if (predictionTracker[i][1] == 'Philadelphia'):
            predictionTracker[i][1] = 'PHI'

        if (predictionTracker[i][1] == 'Pittsburgh'):
            predictionTracker[i][1] = 'PIT'

        if (predictionTracker[i][1] == 'San Francisco'):
            predictionTracker[i][1] = 'SF'

        if (predictionTracker[i][1] == 'Seattle'):
            predictionTracker[i][1] = 'SEA'

        if (predictionTracker[i][1] == 'Tampa Bay'):
            predictionTracker[i][1] = 'TB'

        if (predictionTracker[i][1] == 'Tennessee'):
            predictionTracker[i][1] = 'TEN'

        if (predictionTracker[i][1] == 'Washington'):
            predictionTracker[i][1] = 'WSH'




# print(FiveThirtyEightGames)


#averging odds between 538 and thepredictiontracker

for i in range(len(FiveThirtyEightGames)):
    for j in range(len(predictionTracker)):
        if FiveThirtyEightGames[i][1] == predictionTracker[j][0]:
            FiveThirtyEightGames[i][3] = (float(FiveThirtyEightGames[i][3])+predictionTracker[j][2])/2
        if FiveThirtyEightGames[i][2] == predictionTracker[j][1]:
            FiveThirtyEightGames[i][4] = (float(FiveThirtyEightGames[i][4])+predictionTracker[j][3])/2

# print("------")

# print(predictionTracker)

# print("------")

# print(FiveThirtyEightGames)



# Parse Sports Betting API for sport, game time, teams, and odds

eventsAPI = {}

for i in range(len(theOddsAPIGames)):
    for j in range(len(theOddsAPIGames[i]['sites'])):
        eventsAPI[i] = [theOddsAPIGames[i]['sport_key']], [theOddsAPIGames[i]['commence_time']], [theOddsAPIGames[i]['teams']], [theOddsAPIGames[i]['sites'][j]['odds']]
        break


AlphaAPI=[]
BetaAPI=[]
OddsA=[]
OddsB=[]

#Adding first team to AlphaAPI, second team to BetaAPI, first teams odds to OddsA, and second team odds to OddsB for weekly games

for i in eventsAPI:
    if (datetime.utcfromtimestamp((eventsAPI[i][1][0])-30000).strftime('%Y-%m-%d') >= stringGameDate and datetime.utcfromtimestamp((eventsAPI[i][1][0])-30000).strftime('%Y-%m-%d') <= stringGameWeek):
        AlphaAPI.append(eventsAPI[i][2][0][0])
        BetaAPI.append(eventsAPI[i][2][0][1])
        OddsA.append(eventsAPI[i][3][0]['h2h'][0])
        OddsB.append(eventsAPI[i][3][0]['h2h'][1])



#Matching up 538 teams with sports betting API teams
#Performing calculations to see if expected value of winnings on a $100 dollar bet is over $10 (10% return)

teamstobetNFL=[]

for i in range(len(AlphaAPI)):
    for j in range(len(FiveThirtyEightGames)):
        try:
            if (AlphaAPI[i]).lower() == (FiveThirtyEightGames[j][1].lower()):
                homeAlphaOdds = int((((OddsA[i])-1)*100)*(float(FiveThirtyEightGames[j][3]))-(100*(1-(float(FiveThirtyEightGames[j][3])))))
                if (homeAlphaOdds>10):
                    teamstobetNFL.append({AlphaAPI[i]: homeAlphaOdds})
        except KeyError:
            continue

        try:    
            if (BetaAPI[i]).lower() == (FiveThirtyEightGames[j][2].lower()):
                awayBetaOdds = int((((OddsB[i])-1)*100)*(float(FiveThirtyEightGames[j][4]))-(100*(1-(float(FiveThirtyEightGames[j][4])))))
                if (awayBetaOdds>10):
                    teamstobetNFL.append({BetaAPI[i]: awayBetaOdds})
        except KeyError:
            continue

        try:
            if (AlphaAPI[i]).lower() == (FiveThirtyEightGames[j][2].lower()):
                awayAlphaOdds = int((((OddsA[i])-1)*100)*(float(FiveThirtyEightGames[j][4]))-(100*(1-(float(FiveThirtyEightGames[j][4])))))
                if (awayAlphaOdds>10):
                    teamstobetNFL.append({AlphaAPI[i]: awayAlphaOdds})
        except KeyError:
            continue

        try:    
            if (BetaAPI[i]).lower() == (FiveThirtyEightGames[j][1].lower()):
                homeBetaOdds = int((((OddsB[i])-1)*100)*(float(FiveThirtyEightGames[j][3]))-(100*(1-(float(FiveThirtyEightGames[j][3])))))
                if (homeBetaOdds>10):
                    teamstobetNFL.append({BetaAPI[i]: homeBetaOdds})
        except KeyError:
            continue


 #Comment the below in if just want results for this one model   

print(teamstobetNFL)

