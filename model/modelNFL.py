from urllib.request import urlretrieve as retrieve
from moneyline.moneylineNFL import theOddsAPIGames
from moneyline.moneylineSoccer import gameWeek, pastNFLGame, futureNFLGame, stringGameDate, stringYesterdayDate 
import csv
import time
from datetime import datetime
import pandas as pd
from nflPredictionTracker import predictionTracker


stringGameWeek= str(futureNFLGame)
stringGamePast = str(pastNFLGame)


url = 'https://projects.fivethirtyeight.com/nfl-api/nfl_elo_latest.csv'

retrieve(url,'nfl.csv')
f = open('nfl.csv', 'r')

reader = csv.reader(f)
next(reader)


fullList=[]


#Parse CSV file for sport, teams, and odds for 538
for row in reader:
    fullList.append([row[0], row[4], row[5], row[20], row[21], row[22], row[23], row[28], row[29], row[24]])



FiveThirtyEightGames=[]



#Making sure the game occurs in that NFL week

for game in fullList:
    if game[0] >= stringGamePast and game[0] <= stringGameWeek:
        FiveThirtyEightGames.append(game)



FiveThirtyEightGamesYesterday=[]

for game in fullList:
    if game[0] == stringYesterdayDate:
        FiveThirtyEightGamesYesterday.append(game)





for i in range(len(FiveThirtyEightGamesYesterday)):
    if len(FiveThirtyEightGamesYesterday[i][7])>0:
        FiveThirtyEightGamesYesterday[i][7] = float(FiveThirtyEightGamesYesterday[i][7])
    
    if len(FiveThirtyEightGamesYesterday[i][8])>0:
        FiveThirtyEightGamesYesterday[i][8] = float(FiveThirtyEightGamesYesterday[i][8])



for i in range(len(FiveThirtyEightGamesYesterday)):

    if FiveThirtyEightGamesYesterday[i][7] > FiveThirtyEightGamesYesterday[i][8]:
        FiveThirtyEightGamesYesterday[i][9] = FiveThirtyEightGamesYesterday[i][1]

    elif FiveThirtyEightGamesYesterday[i][7] < FiveThirtyEightGamesYesterday[i][8]:
        FiveThirtyEightGamesYesterday[i][9] = FiveThirtyEightGamesYesterday[i][2]

    else:
        FiveThirtyEightGamesYesterday[i][9] = "Draw"



# print(predictionTracker)
# print("------------")


# print(FiveThirtyEightGames)
# print("------------")


#averging odds between 538 and thepredictiontracker

for i in range(len(FiveThirtyEightGames)):
    for j in range(len(predictionTracker)):
        if FiveThirtyEightGames[i][1] == predictionTracker[j][0]:
            FiveThirtyEightGames[i][3] = (float(FiveThirtyEightGames[i][3])+predictionTracker[j][2])/2
        if FiveThirtyEightGames[i][2] == predictionTracker[j][1]:
            FiveThirtyEightGames[i][4] = (float(FiveThirtyEightGames[i][4])+predictionTracker[j][3])/2



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
potential_winnings=[]
winning_odds=[]

for i in range(len(AlphaAPI)):
    for j in range(len(FiveThirtyEightGames)):
        try:
            if (AlphaAPI[i]).lower() == (FiveThirtyEightGames[j][1].lower()):
                homeAlphaOdds = int((((OddsA[i])-1)*100)*(float(FiveThirtyEightGames[j][3]))-(100*(1-(float(FiveThirtyEightGames[j][3])))))
                if (homeAlphaOdds>10):
                    teamstobetNFL.append({AlphaAPI[i]: homeAlphaOdds})
                    potential_winnings.append(int(((OddsA[i])-1)*100))
                    winning_odds.append(float(FiveThirtyEightGames[j][3]))
        except KeyError:
            continue

        try:    
            if (BetaAPI[i]).lower() == (FiveThirtyEightGames[j][2].lower()):
                awayBetaOdds = int((((OddsB[i])-1)*100)*(float(FiveThirtyEightGames[j][4]))-(100*(1-(float(FiveThirtyEightGames[j][4])))))
                if (awayBetaOdds>10):
                    teamstobetNFL.append({BetaAPI[i]: awayBetaOdds})
                    potential_winnings.append(int(((OddsB[i])-1)*100))
                    winning_odds.append(float(FiveThirtyEightGames[j][4]))
        except KeyError:
            continue

        try:
            if (AlphaAPI[i]).lower() == (FiveThirtyEightGames[j][2].lower()):
                awayAlphaOdds = int((((OddsA[i])-1)*100)*(float(FiveThirtyEightGames[j][4]))-(100*(1-(float(FiveThirtyEightGames[j][4])))))
                if (awayAlphaOdds>10):
                    teamstobetNFL.append({AlphaAPI[i]: awayAlphaOdds})
                    potential_winnings.append(int(((OddsA[i])-1)*100))
                    winning_odds.append(float(FiveThirtyEightGames[j][4]))
        except KeyError:
            continue

        try:    
            if (BetaAPI[i]).lower() == (FiveThirtyEightGames[j][1].lower()):
                homeBetaOdds = int((((OddsB[i])-1)*100)*(float(FiveThirtyEightGames[j][3]))-(100*(1-(float(FiveThirtyEightGames[j][3])))))
                if (homeBetaOdds>10):
                    teamstobetNFL.append({BetaAPI[i]: homeBetaOdds})
                    potential_winnings.append(int(((OddsB[i])-1)*100))
                    winning_odds.append(float(FiveThirtyEightGames[j][3]))
        except KeyError:
            continue


 #Comment the below in if just want results for this one model   

print(teamstobetNFL)

