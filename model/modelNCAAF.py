from urllib.request import urlretrieve as retrieve
from moneyline.moneylineNCAAF import theOddsAPIGames
from moneyline.moneylineSoccer import gameDate
import csv
import time
from datetime import datetime


stringGameDate = str(gameDate)

url = 'https://thepredictiontracker.com/ncaapredictions.csv'

retrieve(url,'ncaaf.csv')

f = open('ncaaf.csv', 'r')

reader = csv.reader(f)
next(reader)

fullList=[]

#Parse CSV file for sport, teams, and odds

# for row in reader:
#         fullList.append([row[0], row[4], row[5], float(row[20]),float(row[21])])

# float(1-row([42]))

# No date needed to filter in this model because CFB games are on week by week basis
for row in reader:
        fullList.append([row[3], row[2], float(row[71]), 1-float(row[71])])

CFB_weekly_games=[]

for game in fullList:
    # if game[0] == stringGameDate:
    CFB_weekly_games.append(game)

# print(CFB_weekly_games)

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




#Adding first team to AlphaAPI, second team to BetaAPI, first teams odds to OddsA, and second team odds to OddsB

for i in eventsAPI:
    # if (datetime.utcfromtimestamp((eventsAPI[i][1][0])-30000).strftime('%Y-%m-%d') == stringGameDate):
    AlphaAPIx.append(eventsAPI[i][2][0][0])
    BetaAPIx.append(eventsAPI[i][2][0][1])
    OddsA.append(eventsAPI[i][3][0]['h2h'][0])
    OddsB.append(eventsAPI[i][3][0]['h2h'][1])


#Cleaning up API names strings so that they match KenPom names strings
        
for i in range(len(AlphaAPIx)):
    AlphaAPI.append(AlphaAPIx[i].rsplit(' ', 1)[0].replace(' State', ' St.').replace('Northern Illinois', 'Northern Ill.').replace('Central Michigan', 'Central Mich.').replace(' Wolf', '').replace(' Black', '').replace(' Sun', '').replace(' Red', '').replace(' Ragin', '').replace(' Blue', '').replace(' Tar', '').replace(' Green', '').replace('UL Monroe', 'Louisiana-Monroe').replace(' Golden', '').replace(' Thundering', '').replace(' Fighting', '').replace(' Nittany', '').replace('UTSA', 'Texas-San Antonio').replace(' Horned', '').replace(' Mean', '').replace(' Scarlet', '').replace(' Rainbow', '').replace(' Crimson', ''))
    BetaAPI.append(BetaAPIx[i].rsplit(' ', 1)[0].replace(' State', ' St.').replace('Northern Illinois', 'Northern Ill.').replace('Central Michigan', 'Central Mich.').replace(' Wolf', '').replace(' Black', '').replace(' Sun', '').replace(' Red', '').replace(' Ragin', '').replace(' Blue', '').replace(' Tar', '').replace(' Green', '').replace('UL Monroe', 'Louisiana-Monroe').replace(' Golden', '').replace(' Thundering', '').replace(' Fighting', '').replace(' Nittany', '').replace('UTSA', 'Texas-San Antonio').replace(' Horned', '').replace(' Mean', '').replace(' Scarlet', '').replace(' Rainbow', '').replace(' Crimson', ''))



#Matching up thepredictiontracker teams with sports betting API teams
#Performing calculations to see if expected value of winnings on a $100 dollar bet is over $10 (10% return)

teamsToBetCFB=[]

for i in range(len(AlphaAPI)):
    for j in range(len(CFB_weekly_games)):
        try:
            if (AlphaAPI[i]).lower() == (CFB_weekly_games[j][0].lower()):
                homeAlphaOdds = int((((OddsA[i])-1)*100)*(float(CFB_weekly_games[j][2]))-(100*(1-(float(CFB_weekly_games[j][2])))))
                if (homeAlphaOdds>10):
                    teamsToBetCFB.append({AlphaAPI[i]: homeAlphaOdds})
        except KeyError:
            continue

        try:    
            if (BetaAPI[i]).lower() == (CFB_weekly_games[j][1].lower()):
                awayBetaOdds = int((((OddsB[i])-1)*100)*(float(CFB_weekly_games[j][3]))-(100*(1-(float(CFB_weekly_games[j][3])))))
                if (awayBetaOdds>10):
                    teamsToBetCFB.append({BetaAPI[i]: awayBetaOdds})
        except KeyError:
            continue

        try:
            if (AlphaAPI[i]).lower() == (CFB_weekly_games[j][1].lower()):
                awayAlphaOdds = int((((OddsA[i])-1)*100)*(float(CFB_weekly_games[j][3]))-(100*(1-(float(CFB_weekly_games[j][3])))))
                if (awayAlphaOdds>10):
                    teamsToBetCFB.append({AlphaAPI[i]: awayAlphaOdds})
        except KeyError:
            continue

        try:    
            if (BetaAPI[i]).lower() == (CFB_weekly_games[j][0].lower()):
                homeBetaOdds = int((((OddsB[i])-1)*100)*(float(CFB_weekly_games[j][2]))-(100*(1-(float(CFB_weekly_games[j][2])))))
                if (homeBetaOdds>10):
                    teamsToBetCFB.append({BetaAPI[i]: homeBetaOdds})
        except KeyError:
            continue


 #Comment the below in if just want results for this one model   

print(teamsToBetCFB)



# teams = []

# for i in range(len(teamsToBetCFB)):
#     for key in teamsToBetCFB[i].keys():
#         teams.append(key)


# print(teams)



