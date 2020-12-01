from urllib.request import urlretrieve as retrieve
from moneyline.moneylineMLB import theOddsAPIGames
from moneyline.moneylineSoccer import stringGameDate
import csv
import time
from datetime import datetime


url = 'https://projects.fivethirtyeight.com/mlb-api/mlb_elo_latest.csv'

retrieve(url,'mlb.csv')

f = open('mlb.csv', 'r')

reader = csv.reader(f)
next(reader)

fullList=[]

#Parse CSV file for sport, teams, and odds

for row in reader:
        fullList.append([row[0], row[4], row[5], float(row[20]),float(row[21])])

FiveThirtyEightGames=[]

for game in fullList:
    if game[0] == stringGameDate:
        FiveThirtyEightGames.append(game)


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

#Adding first team to AlphaAPI, second team to BetaAPI, first teams odds to OddsA, and second team odds to OddsB

for i in eventsAPI:
    if (datetime.utcfromtimestamp((eventsAPI[i][1][0])-30000).strftime('%Y-%m-%d') == stringGameDate):
        AlphaAPI.append(eventsAPI[i][2][0][0])
        BetaAPI.append(eventsAPI[i][2][0][1])
        OddsA.append(eventsAPI[i][3][0]['h2h'][0])
        OddsB.append(eventsAPI[i][3][0]['h2h'][1])



#Matching up 538 teams with sports betting API teams
#Performing calculations to see if expected value of winnings on a $100 dollar bet is over $10 (10% return)

teamsToBetMLB=[]

for i in range(len(AlphaAPI)):
    for j in range(len(FiveThirtyEightGames)):
        try:
            if (AlphaAPI[i]).lower() == (FiveThirtyEightGames[j][1].lower()):
                homeAlphaOdds = int((((OddsA[i])-1)*100)*(float(FiveThirtyEightGames[j][3]))-(100*(1-(float(FiveThirtyEightGames[j][3])))))
                if (homeAlphaOdds>5):
                    teamsToBetMLB.append({AlphaAPI[i]: homeAlphaOdds})
        except KeyError:
            continue

        try:    
            if (BetaAPI[i]).lower() == (FiveThirtyEightGames[j][2].lower()):
                awayBetaOdds = int((((OddsB[i])-1)*100)*(float(FiveThirtyEightGames[j][4]))-(100*(1-(float(FiveThirtyEightGames[j][4])))))
                if (awayBetaOdds>5):
                    teamsToBetMLB.append({BetaAPI[i]: awayBetaOdds})
        except KeyError:
            continue

        try:
            if (AlphaAPI[i]).lower() == (FiveThirtyEightGames[j][2].lower()):
                awayAlphaOdds = int((((OddsA[i])-1)*100)*(float(FiveThirtyEightGames[j][4]))-(100*(1-(float(FiveThirtyEightGames[j][4])))))
                if (awayAlphaOdds>5):
                    teamsToBetMLB.append({AlphaAPI[i]: awayAlphaOdds})
        except KeyError:
            continue

        try:    
            if (BetaAPI[i]).lower() == (FiveThirtyEightGames[j][1].lower()):
                homeBetaOdds = int((((OddsB[i])-1)*100)*(float(FiveThirtyEightGames[j][3]))-(100*(1-(float(FiveThirtyEightGames[j][3])))))
                if (homeBetaOdds>5):
                    teamsToBetMLB.append({BetaAPI[i]: homeBetaOdds})
        except KeyError:
            continue


 #Comment the below in if just want results for this one model   

print(teamsToBetMLB)

