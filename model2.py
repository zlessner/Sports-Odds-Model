from urllib.request import urlretrieve as retrieve
from moneyline2 import theOddsAPIGames, today, tomorrow
from model import teamsToBetScotland
from modelNBA import teamsToBetNBA
import csv
import time
# import datetime
from datetime import datetime


stringToday = str(today)
stringTomorrow = str(tomorrow)

url = 'https://projects.fivethirtyeight.com/soccer-api/club/spi_matches.csv'

retrieve(url,'soccer.csv')

f = open('soccer.csv', 'r')

reader = csv.reader(f)
next(reader)

fullList=[]

for row in reader:
        fullList.append([row[0], row[2], row[3], row[4], float(row[7]),float(row[8]),float(row[9])])

FiveThirtyEightGames=[]

#Can change date

for game in fullList:
    if game[0] == stringToday:
        FiveThirtyEightGames.append(game)

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
    if (datetime.utcfromtimestamp(eventsAPI[i][1][0]).strftime('%Y-%m-%d') == stringToday):
        AlphaAPI.append(eventsAPI[i][2][0][0])
        BetaAPI.append(eventsAPI[i][2][0][1])

# print(AlphaAPI)
# print(BetaAPI)


# # print (range(len(AlphaAPI)))
# print(FiveThirtyEightGames)
# print(FiveThirtyEightGames[0][3])


#Adding teams to bet on, whether to win or draw
teamsToBet=[]

for i in range(len(AlphaAPI)):
    for j in range(len(FiveThirtyEightGames)):
        if AlphaAPI[i][:5] == FiveThirtyEightGames[j][2][:5]:
            homeAlphaOdds = int((((eventsAPI[i][3][0]['h2h'][0])-1)*100)*(float(FiveThirtyEightGames[j][4]))-(100*(1-(float(FiveThirtyEightGames[j][4])))))
            homeAlphaDrawOdds = int((((eventsAPI[i][3][0]['h2h'][2])-1)*100)*(float(FiveThirtyEightGames[j][6]))-(100*(1-(float(FiveThirtyEightGames[j][6])))))
            if (homeAlphaOdds>0):
                teamsToBet.append({AlphaAPI[i]: homeAlphaOdds})
            if (homeAlphaDrawOdds>0):
                teamsToBet.append({AlphaAPI[i]+ " " + BetaAPI[i] + " Draw": homeAlphaDrawOdds})
            
        if BetaAPI[i][:5] == FiveThirtyEightGames[j][3][:5]:
            awayBetaOdds = int((((eventsAPI[i][3][0]['h2h'][1])-1)*100)*(float(FiveThirtyEightGames[j][5]))-(100*(1-(float(FiveThirtyEightGames[j][5])))))
            if (awayBetaOdds>0):
                teamsToBet.append({BetaAPI[i]: awayBetaOdds})

        if AlphaAPI[i][:5] == FiveThirtyEightGames[j][3][:5]:
            awayAlphaOdds = int((((eventsAPI[i][3][0]['h2h'][0])-1)*100)*(float(FiveThirtyEightGames[j][5]))-(100*(1-(float(FiveThirtyEightGames[j][5])))))
            awayAlphaDrawOdds = int((((eventsAPI[i][3][0]['h2h'][2])-1)*100)*(float(FiveThirtyEightGames[j][6]))-(100*(1-(float(FiveThirtyEightGames[j][6])))))
            if (awayAlphaOdds>0):
                teamsToBet.append({AlphaAPI[i]: awayAlphaOdds})
            if (awayAlphaDrawOdds>0):
                teamsToBet.append({AlphaAPI[i]+ " " + BetaAPI[i] + " Draw": awayAlphaDrawOdds})
            
        if BetaAPI[i][:5] == FiveThirtyEightGames[j][2][:5]:
            homeBetaOdds = int((((eventsAPI[i][3][0]['h2h'][1])-1)*100)*(float(FiveThirtyEightGames[j][4]))-(100*(1-(float(FiveThirtyEightGames[j][4])))))
            if (homeBetaOdds>0):
                teamsToBet.append({BetaAPI[i]: homeBetaOdds})

            
teamsToBet.append(teamsToBetScotland)  
teamsToBet.append(teamsToBetNBA) 

print(teamsToBet)

#alphabeitical ordering per group and odds
#use soccer sport codes epl etc. to combine all the ganes
#home team option for sorting? Not sure if there's an away team field
#Because same name is used for multiple teams, teams may repeat twice - see what happens for Man City Man U
#add in draw option