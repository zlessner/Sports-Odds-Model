from urllib.request import urlretrieve as retrieve
from moneylineSoccer2 import theOddsAPIGames, nowTime
from moneylineSoccer import today
from modelSoccer import teamsToBet1
from modelNBA import teamsToBetNBA
from modelCBB import teamsToBetCBB
import csv
import time
# import datetime
from datetime import datetime


stringToday = str(today)

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

AlphaAPIx=[]
BetaAPIx=[]
AlphaAPI=[]
BetaAPI=[]

#Can change date

for i in eventsAPI:
    if (datetime.utcfromtimestamp(eventsAPI[i][1][0]).strftime('%Y-%m-%d') == stringToday):
        AlphaAPIx.append(eventsAPI[i][2][0][0])
        BetaAPIx.append(eventsAPI[i][2][0][1])


for i in range(len(AlphaAPIx)):
    AlphaAPI.append(AlphaAPIx[i].replace("Ch\\u00e2teauroux", 'Chateauroux').replace("FC Chambly", 'Chambly Thelle FC').replace("Le Mans FC", 'Le Mans').replace("Rodez AF", 'Rodez').replace("Orl\\u00e9ans", 'Orléans').replace("SM Caen", 'Caen').replace("EA Guingamp", 'Guingamp').replace("AC Ajaccio", 'Ajaccio'))
    BetaAPI.append(BetaAPIx[i].replace("Ch\\u00e2teauroux", 'Chateauroux').replace("FC Chambly", 'Chambly Thelle FC').replace("Le Mans FC", 'Le Mans').replace("Rodez AF", 'Rodez').replace("Orl\\u00e9ans", 'Orléans').replace("SM Caen", 'Caen').replace("EA Guingamp", 'Guingamp').replace("AC Ajaccio", 'Ajaccio'))

# print(AlphaAPI)
# print(BetaAPI)


# # print (range(len(AlphaAPI)))
# print(FiveThirtyEightGames)
# print(FiveThirtyEightGames[0][3])


#Adding teams to bet on, whether to win or draw
teamsToBet2=[nowTime]

for i in range(len(AlphaAPI)):
    for j in range(len(FiveThirtyEightGames)):
        if AlphaAPI[i] == FiveThirtyEightGames[j][2]:
            homeAlphaOdds = int((((eventsAPI[i][3][0]['h2h'][0])-1)*100)*(float(FiveThirtyEightGames[j][4]))-(100*(1-(float(FiveThirtyEightGames[j][4])))))
            homeAlphaDrawOdds = int((((eventsAPI[i][3][0]['h2h'][2])-1)*100)*(float(FiveThirtyEightGames[j][6]))-(100*(1-(float(FiveThirtyEightGames[j][6])))))
            if (homeAlphaOdds>10):
                teamsToBet2.append({AlphaAPI[i]: homeAlphaOdds})
            if (homeAlphaDrawOdds>10):
                teamsToBet2.append({AlphaAPI[i]+ " " + BetaAPI[i] + " Draw": homeAlphaDrawOdds})
            
        if BetaAPI[i] == FiveThirtyEightGames[j][3]:
            awayBetaOdds = int((((eventsAPI[i][3][0]['h2h'][1])-1)*100)*(float(FiveThirtyEightGames[j][5]))-(100*(1-(float(FiveThirtyEightGames[j][5])))))
            if (awayBetaOdds>10):
                teamsToBet2.append({BetaAPI[i]: awayBetaOdds})

        if AlphaAPI[i] == FiveThirtyEightGames[j][3]:
            awayAlphaOdds = int((((eventsAPI[i][3][0]['h2h'][0])-1)*100)*(float(FiveThirtyEightGames[j][5]))-(100*(1-(float(FiveThirtyEightGames[j][5])))))
            awayAlphaDrawOdds = int((((eventsAPI[i][3][0]['h2h'][2])-1)*100)*(float(FiveThirtyEightGames[j][6]))-(100*(1-(float(FiveThirtyEightGames[j][6])))))
            if (awayAlphaOdds>10):
                teamsToBet2.append({AlphaAPI[i]: awayAlphaOdds})
            if (awayAlphaDrawOdds>10):
                teamsToBet2.append({AlphaAPI[i]+ " " + BetaAPI[i] + " Draw": awayAlphaDrawOdds})
            
        if BetaAPI[i] == FiveThirtyEightGames[j][2]:
            homeBetaOdds = int((((eventsAPI[i][3][0]['h2h'][1])-1)*100)*(float(FiveThirtyEightGames[j][4]))-(100*(1-(float(FiveThirtyEightGames[j][4])))))
            if (homeBetaOdds>10):
                teamsToBet2.append({BetaAPI[i]: homeBetaOdds})

            
teamsToBet2.append(teamsToBet1)  
teamsToBet2.append(teamsToBetNBA) 
teamsToBet2.append(teamsToBetCBB) 

print(teamsToBet2)

with open('bets.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([teamsToBet2])

#alphabeitical ordering per group and odds
#use soccer sport codes epl etc. to combine all the ganes
#home team option for sorting? Not sure if there's an away team field
#Because same name is used for multiple teams, teams may repeat twice - see what happens for Man City Man U