from urllib.request import urlretrieve as retrieve
from moneyline.moneylineNBA import theOddsAPIGames
from moneyline.moneylineSoccer import stringGameDate, stringYesterdayDate 
import csv
import time
from datetime import datetime


url = 'https://projects.fivethirtyeight.com/nba-model/nba_elo_latest.csv'

retrieve(url,'nba.csv')

f = open('nba.csv', 'r')

reader = csv.reader(f)
next(reader)

fullList=[]

#Parse CSV file for sport, teams, and odds

# Eventually bring in thepredictiontracker once season starts

for row in reader:
        fullList.append([row[0], row[4], row[5], float(row[20]),float(row[21]), row[6], row[7], row[22], row[23], row[8]])

FiveThirtyEightGames=[]

for game in fullList:
    if game[0] == stringGameDate:
        FiveThirtyEightGames.append(game)


FiveThirtyEightGamesYesterday=[]
playedTeams = []

for game in fullList:
    if game[0] == stringYesterdayDate:
        FiveThirtyEightGamesYesterday.append(game)





for i in range(len(FiveThirtyEightGamesYesterday)):
    if len(FiveThirtyEightGamesYesterday[i][7])>0:
        FiveThirtyEightGamesYesterday[i][7] = float(FiveThirtyEightGamesYesterday[i][7])
        playedTeams.append(FiveThirtyEightGamesYesterday[i][3])
        playedTeams.append(FiveThirtyEightGamesYesterday[i][2])

    if len(FiveThirtyEightGamesYesterday[i][8])>0:
        FiveThirtyEightGamesYesterday[i][8] = float(FiveThirtyEightGamesYesterday[i][8])


for i in range(len(FiveThirtyEightGamesYesterday)):

    if FiveThirtyEightGamesYesterday[i][7] > FiveThirtyEightGamesYesterday[i][8]:
        FiveThirtyEightGamesYesterday[i][9] = FiveThirtyEightGamesYesterday[i][1]

    elif FiveThirtyEightGamesYesterday[i][7] < FiveThirtyEightGamesYesterday[i][8]:
        FiveThirtyEightGamesYesterday[i][9] = FiveThirtyEightGamesYesterday[i][2]



# Parse Sports Betting API for sport, game time, teams, and odds

eventsAPI = {}

for i in range(len(theOddsAPIGames)):
    for j in range(len(theOddsAPIGames[i]['sites'])):
        # if theOddsAPIGames[i]['sites'][j]['site_key'] == 'betrivers':
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

teamsToBetNBA=[]
potential_winnings=[]
winning_odds=[]

for i in range(len(AlphaAPI)):
    for j in range(len(FiveThirtyEightGames)):
        try:
            if (AlphaAPI[i]).lower() == (FiveThirtyEightGames[j][1].lower()):
                homeAlphaOdds = int((((OddsA[i])-1)*100)*(float(FiveThirtyEightGames[j][3]))-(100*(1-(float(FiveThirtyEightGames[j][3])))))
                if (homeAlphaOdds>7):
                    teamsToBetNBA.append({AlphaAPI[i]: homeAlphaOdds})
                    potential_winnings.append(int(((OddsA[i])-1)*100))
                    winning_odds.append(float(FiveThirtyEightGames[j][3]))
        except KeyError:
            continue

        try:    
            if (BetaAPI[i]).lower() == (FiveThirtyEightGames[j][2].lower()):
                awayBetaOdds = int((((OddsB[i])-1)*100)*(float(FiveThirtyEightGames[j][4]))-(100*(1-(float(FiveThirtyEightGames[j][4])))))
                if (awayBetaOdds>7):
                    teamsToBetNBA.append({BetaAPI[i]: awayBetaOdds})
                    potential_winnings.append(int(((OddsB[i])-1)*100))
                    winning_odds.append(float(FiveThirtyEightGames[j][4]))
        except KeyError:
            continue

        try:
            if (AlphaAPI[i]).lower() == (FiveThirtyEightGames[j][2].lower()):
                awayAlphaOdds = int((((OddsA[i])-1)*100)*(float(FiveThirtyEightGames[j][4]))-(100*(1-(float(FiveThirtyEightGames[j][4])))))
                if (awayAlphaOdds>7):
                    teamsToBetNBA.append({AlphaAPI[i]: awayAlphaOdds})
                    potential_winnings.append(int(((OddsA[i])-1)*100))
                    winning_odds.append(float(FiveThirtyEightGames[j][4]))
        except KeyError:
            continue

        try:    
            if (BetaAPI[i]).lower() == (FiveThirtyEightGames[j][1].lower()):
                homeBetaOdds = int((((OddsB[i])-1)*100)*(float(FiveThirtyEightGames[j][3]))-(100*(1-(float(FiveThirtyEightGames[j][3])))))
                if (homeBetaOdds>7):
                    teamsToBetNBA.append({BetaAPI[i]: homeBetaOdds})
                    potential_winnings.append(int(((OddsB[i])-1)*100))
                    winning_odds.append(float(FiveThirtyEightGames[j][3]))
        except KeyError:
            continue


 #Comment the below in if just want results for this one model   

print(teamsToBetNBA)

