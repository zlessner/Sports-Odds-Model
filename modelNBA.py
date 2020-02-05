from urllib.request import urlretrieve as retrieve
from moneylineNBA import theOddsAPIGames
from moneylineSoccer import gameDate
import csv
import time
from datetime import datetime


stringGameDate = str(gameDate)

url = 'https://projects.fivethirtyeight.com/nba-model/nba_elo_latest.csv'

retrieve(url,'nba.csv')

f = open('nba.csv', 'r')

reader = csv.reader(f)
next(reader)

fullList=[]

#home team float(row[20])
for row in reader:
        fullList.append([row[0], row[4], row[5], float(row[20]),float(row[21])])

FiveThirtyEightGames=[]

#Can change date

for game in fullList:
    if game[0] == stringGameDate:
        FiveThirtyEightGames.append(game)

# print (FiveThirtyEightGames)

# print(FiveThirtyEightGames, "\n")

# for odds in FiveThirtyEightGames:
#     if (odds[4]>.5):
#         print(odds[2])

eventsAPI = {}

for i in range(len(theOddsAPIGames)):
    for j in range(len(theOddsAPIGames[i]['sites'])):
        eventsAPI[i] = [theOddsAPIGames[i]['sport_key']], [theOddsAPIGames[i]['commence_time']], [theOddsAPIGames[i]['teams']], [theOddsAPIGames[i]['sites'][j]['odds']]
        break

# print(eventsAPI[1][1][0][1])

# print (eventsAPI)

AlphaAPI=[]
BetaAPI=[]

#Can change date

for i in eventsAPI:
    if (datetime.utcfromtimestamp((eventsAPI[i][1][0])-30000).strftime('%Y-%m-%d') == stringGameDate):
        AlphaAPI.append(eventsAPI[i][2][0][0])
        BetaAPI.append(eventsAPI[i][2][0][1])

# # print (range(len(AlphaAPI)))
# print(FiveThirtyEightGames)
# print(FiveThirtyEightGames[0][3])


#Adding teams to bet on
teamsToBetNBA=[]

for i in range(len(AlphaAPI)):
    for j in range(len(FiveThirtyEightGames)):
        try:
            if (AlphaAPI[i]).lower() == (FiveThirtyEightGames[j][1].lower()):
                homeAlphaOdds = int((((eventsAPI[i][3][0]['h2h'][0])-1)*100)*(float(FiveThirtyEightGames[j][3]))-(100*(1-(float(FiveThirtyEightGames[j][3])))))
                if (homeAlphaOdds>10):
                    teamsToBetNBA.append({AlphaAPI[i]: homeAlphaOdds})
        except KeyError:
            continue

        try:    
            if (BetaAPI[i]).lower() == (FiveThirtyEightGames[j][2].lower()):
                awayBetaOdds = int((((eventsAPI[i][3][0]['h2h'][1])-1)*100)*(float(FiveThirtyEightGames[j][4]))-(100*(1-(float(FiveThirtyEightGames[j][4])))))
                if (awayBetaOdds>10):
                    teamsToBetNBA.append({BetaAPI[i]: awayBetaOdds})
        except KeyError:
            continue

        try:
            if (AlphaAPI[i]).lower() == (FiveThirtyEightGames[j][2].lower()):
                awayAlphaOdds = int((((eventsAPI[i][3][0]['h2h'][0])-1)*100)*(float(FiveThirtyEightGames[j][4]))-(100*(1-(float(FiveThirtyEightGames[j][4])))))
                if (awayAlphaOdds>10):
                    teamsToBetNBA.append({AlphaAPI[i]: awayAlphaOdds})
        except KeyError:
            continue

        try:    
            if (BetaAPI[i]).lower() == (FiveThirtyEightGames[j][1].lower()):
                homeBetaOdds = int((((eventsAPI[i][3][0]['h2h'][1])-1)*100)*(float(FiveThirtyEightGames[j][3]))-(100*(1-(float(FiveThirtyEightGames[j][3])))))
                if (homeBetaOdds>10):
                    teamsToBetNBA.append({BetaAPI[i]: homeBetaOdds})
        except KeyError:
            continue
    
# print(teamsToBetNBA)

#alphabeitical ordering per group and odds
#use soccer sport codes epl etc. to combine all the ganes
#home team option for sorting? Not sure if there's an away team field
#Because same name is used for multiple teams, teams may repeat twice - see what happens for Man City Man U
#turn into classes?