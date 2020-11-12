from urllib.request import urlretrieve as retrieve
from moneyline.moneylineSoccer2 import theOddsAPIGames, nowTime
from moneyline.moneylineSoccer import gameDate
from modelSoccer import teamsToBet1
from modelNBA import teamsToBetNBA
from modelCBB import teamsToBetCBB
from modelNCAAF import teamsToBetCFB
import csv
import time
from datetime import datetime


stringGameDate = str(gameDate)

url = 'https://projects.fivethirtyeight.com/soccer-api/club/spi_matches.csv'

retrieve(url,'soccer.csv')

f = open('soccer.csv', 'r')

reader = csv.reader(f)
next(reader)

fullList=[]


#Parse CSV file for sport, teams, and odds

for row in reader:
        fullList.append([row[1], row[3], row[4], row[5], float(row[8]),float(row[9]),float(row[10])])

FiveThirtyEightGames=[]

#Can change date

for game in fullList:
    if game[0] == stringGameDate:
        FiveThirtyEightGames.append(game)



# Parse Sports Betting API for sport, game time, teams, and odds

eventsAPI = {}

for i in range(len(theOddsAPIGames)):
    for j in range(len(theOddsAPIGames[i]['sites'])):
        eventsAPI[i] = [theOddsAPIGames[i]['sport_key']], [theOddsAPIGames[i]['commence_time']], [theOddsAPIGames[i]['teams']], [theOddsAPIGames[i]['sites'][j]['odds']]
        break



AlphaAPIx=[]
BetaAPIx=[]
AlphaAPI=[]
BetaAPI=[]
OddsA=[]
OddsB=[]
OddsC=[]


#Adding first team to AlphaAPI, second team to BetaAPI, first teams odds to OddsA, second team odds to OddsB, and draw odds to OddsC

for i in eventsAPI:
    if (datetime.utcfromtimestamp(eventsAPI[i][1][0]).strftime('%Y-%m-%d') == stringGameDate):
        AlphaAPIx.append(eventsAPI[i][2][0][0])
        BetaAPIx.append(eventsAPI[i][2][0][1])
        OddsA.append(eventsAPI[i][3][0]['h2h'][0])
        OddsB.append(eventsAPI[i][3][0]['h2h'][1])
        OddsC.append(eventsAPI[i][3][0]['h2h'][2])


#Slightly altering names to match up to 538

for i in range(len(AlphaAPIx)):
    AlphaAPI.append(AlphaAPIx[i].replace("Ch\\u00e2teauroux", 'Chateauroux').replace("FC Chambly", 'Chambly Thelle FC').replace("Le Mans FC", 'Le Mans').replace("Rodez AF", 'Rodez').replace("Orl\\u00e9ans", 'Orléans').replace("SM Caen", 'Caen').replace("EA Guingamp", 'Guingamp').replace("AC Ajaccio", 'Ajaccio').replace("Dijon", 'Dijon FCO').replace("Nîmes Olympique", 'Nimes').replace("Stade de Reims", 'Reims').replace("Saint Etienne", 'St Etienne'))
    BetaAPI.append(BetaAPIx[i].replace("Ch\\u00e2teauroux", 'Chateauroux').replace("FC Chambly", 'Chambly Thelle FC').replace("Le Mans FC", 'Le Mans').replace("Rodez AF", 'Rodez').replace("Orl\\u00e9ans", 'Orléans').replace("SM Caen", 'Caen').replace("EA Guingamp", 'Guingamp').replace("AC Ajaccio", 'Ajaccio').replace("Dijon", 'Dijon FCO').replace("Nîmes Olympique", 'Nimes').replace("Stade de Reims", 'Reims').replace("Saint Etienne", 'St Etienne'))


#Matching up 538 teams with sports betting API teams, whether to win, lose or draw
#Performing calculations to see if expected value of winnings on a $100 dollar bet is over $10 (10% return)

teamsToBet2=[nowTime]

for i in range(len(AlphaAPI)):
    for j in range(len(FiveThirtyEightGames)):
        if AlphaAPI[i] == FiveThirtyEightGames[j][2]:
            homeAlphaOdds = int((((OddsA[i])-1)*100)*(float(FiveThirtyEightGames[j][4]))-(100*(1-(float(FiveThirtyEightGames[j][4])))))
            homeAlphaDrawOdds = int((((OddsC[i])-1)*100)*(float(FiveThirtyEightGames[j][6]))-(100*(1-(float(FiveThirtyEightGames[j][6])))))
            if (homeAlphaOdds>10):
                teamsToBet2.append({AlphaAPI[i]: homeAlphaOdds})
            if (homeAlphaDrawOdds>10):
                teamsToBet2.append({AlphaAPI[i]+ " " + BetaAPI[i] + " Draw": homeAlphaDrawOdds})
            
        if BetaAPI[i] == FiveThirtyEightGames[j][3]:
            awayBetaOdds = int((((OddsB[i])-1)*100)*(float(FiveThirtyEightGames[j][5]))-(100*(1-(float(FiveThirtyEightGames[j][5])))))
            if (awayBetaOdds>10):
                teamsToBet2.append({BetaAPI[i]: awayBetaOdds})

        if AlphaAPI[i] == FiveThirtyEightGames[j][3]:
            awayAlphaOdds = int((((OddsA[i])-1)*100)*(float(FiveThirtyEightGames[j][5]))-(100*(1-(float(FiveThirtyEightGames[j][5])))))
            awayAlphaDrawOdds = int((((OddsC[i])-1)*100)*(float(FiveThirtyEightGames[j][6]))-(100*(1-(float(FiveThirtyEightGames[j][6])))))
            if (awayAlphaOdds>10):
                teamsToBet2.append({AlphaAPI[i]: awayAlphaOdds})
            if (awayAlphaDrawOdds>10):
                teamsToBet2.append({AlphaAPI[i]+ " " + BetaAPI[i] + " Draw": awayAlphaDrawOdds})
            
        if BetaAPI[i] == FiveThirtyEightGames[j][2]:
            homeBetaOdds = int((((OddsB[i])-1)*100)*(float(FiveThirtyEightGames[j][4]))-(100*(1-(float(FiveThirtyEightGames[j][4])))))
            if (homeBetaOdds>10):
                teamsToBet2.append({BetaAPI[i]: homeBetaOdds})


#Appending results from all of the other models in order to print out all of the results
            
teamsToBet2.append(teamsToBet1)  
teamsToBet2.append(teamsToBetNBA) 
teamsToBet2.append(teamsToBetCBB)
teamsToBet2.append(teamsToBetCFB)  

print(teamsToBet2)


#Record results with the run date to the bets.csv file

with open('bets.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([teamsToBet2])
