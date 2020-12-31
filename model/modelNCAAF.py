from urllib.request import urlretrieve as retrieve
from moneyline.moneylineNCAAF import theOddsAPIGames
from moneyline.moneylineSoccer import stringGameDate, futureNFLGame, pastNFLGame
import csv
import time
from datetime import datetime

stringGameWeek= str(futureNFLGame)
stringGamePast = str(pastNFLGame)


url = 'https://thepredictiontracker.com/ncaapredictions.csv'

retrieve(url,'ncaaf.csv')

f = open('ncaaf.csv', 'r')

reader = csv.reader(f)
next(reader)

fullList=[]

#Parse CSV file for sport, teams, and odds

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

Home = []
Away = []
bestHome = 0
bestAway = 0
bookHome = []
bookAway =[]
bestBookHome = ''
bestBookAway = ''
bestHome = 0
bestAway = 0


# Extracting best odds and sportbook names with best odds
for i in range(len(theOddsAPIGames)):
    if (datetime.utcfromtimestamp(([theOddsAPIGames[i]['commence_time']][0]-30000)).strftime('%Y-%m-%d') == stringGameDate):
    
        for j in range(len(theOddsAPIGames[i]['sites'])):

            # if I wanted to use just one specific sports book use the below code
            # if theOddsAPIGames[i]['sites'][j]['site_key'] == 'mybookieag':
                # print([theOddsAPIGames[i]['sites'][j]['odds']['h2h'][1]])
                # Home.append(([theOddsAPIGames[i]['sites'][j]['odds']['h2h'][1]][0]))

            # if theOddsAPIGames[i]['sites'][j]['site_key'] == 'gtbets':
            #     print([theOddsAPIGames[i]['sites'][j]['odds']['h2h'][1]])


            # if (datetime.utcfromtimestamp(([theOddsAPIGames[i]['commence_time']][0]-30000)).strftime('%Y-%m-%d') == stringGameDate):
                print(datetime.utcfromtimestamp(([theOddsAPIGames[i]['commence_time']][0]-30000)).strftime('%Y-%m-%d'))
            # if (datetime.utcfromtimestamp(([theOddsAPIGames[i]['commence_time']][0]-30000)).strftime('%Y-%m-%d') >= stringGameDate and datetime.utcfromtimestamp(([theOddsAPIGames[i]['commence_time']][0]-30000)).strftime('%Y-%m-%d') <= stringGameWeek):
                eventsAPI[i] = [theOddsAPIGames[i]['sport_key']], [theOddsAPIGames[i]['commence_time']], [theOddsAPIGames[i]['teams']], [theOddsAPIGames[i]['sites'][j]['odds']], [theOddsAPIGames[i]['sites'][j]['site_key']], [theOddsAPIGames[i]['home_team']]
                # break
                if theOddsAPIGames[i]['sites'][j]['site_key'] != 'betfair':
                    if [theOddsAPIGames[i]['sites'][j]['odds']['h2h'][1]][0] > bestHome:
                        bestHome = [theOddsAPIGames[i]['sites'][j]['odds']['h2h'][1]][0]
                        bestBookHome = theOddsAPIGames[i]['sites'][j]['site_key']
                    if [theOddsAPIGames[i]['sites'][j]['odds']['h2h'][0]][0] > bestAway:
                        bestAway = [theOddsAPIGames[i]['sites'][j]['odds']['h2h'][0]][0]
                        bestBookAway = theOddsAPIGames[i]['sites'][j]['site_key']

        Home.append(bestHome)
        Away.append(bestAway)
        bookHome.append(bestBookHome)
        bookAway.append(bestBookAway)
        bestHome = 0
        bestAway = 0

AlphaAPIx=[]
BetaAPIx=[]
AlphaAPI=[]
BetaAPI=[]




#Adding Home team to AlphaAPI, Away team to BetaAPI, Home teams odds to OddsA, and Away team odds to OddsB

for i in eventsAPI:
    if (datetime.utcfromtimestamp((eventsAPI[i][1][0])-30000).strftime('%Y-%m-%d') >= stringGameDate and datetime.utcfromtimestamp((eventsAPI[i][1][0])-30000).strftime('%Y-%m-%d') <= stringGameWeek):
    # if (datetime.utcfromtimestamp((eventsAPI[i][1][0])-30000).strftime('%Y-%m-%d') == stringGameDate):
        AlphaAPIx.append(eventsAPI[i][2][0][0])
        BetaAPIx.append(eventsAPI[i][2][0][1])
        # OddsA.append(eventsAPI[i][3][0]['h2h'][0])
        # OddsB.append(eventsAPI[i][3][0]['h2h'][1])


#Cleaning up API names strings so that they match KenPom names strings
        
for i in range(len(AlphaAPIx)):
    AlphaAPI.append(AlphaAPIx[i].rsplit(' ', 1)[0].replace(' State', ' St.').replace('Northern Illinois', 'Northern Ill.').replace('Central Michigan', 'Central Mich.').replace(' Wolf', '').replace(' Black', '').replace(' Sun', '').replace(' Red', '').replace(' Ragin', '').replace(' Blue', '').replace(' Tar', '').replace(' Green', '').replace('UL Monroe', 'Louisiana-Monroe').replace(' Golden', '').replace(' Thundering', '').replace(' Fighting', '').replace(' Nittany', '').replace('UTSA', 'Texas-San Antonio').replace(' Horned', '').replace(' Mean', '').replace(' Scarlet', '').replace(' Rainbow', '').replace(' Crimson', ''))
    BetaAPI.append(BetaAPIx[i].rsplit(' ', 1)[0].replace(' State', ' St.').replace('Northern Illinois', 'Northern Ill.').replace('Central Michigan', 'Central Mich.').replace(' Wolf', '').replace(' Black', '').replace(' Sun', '').replace(' Red', '').replace(' Ragin', '').replace(' Blue', '').replace(' Tar', '').replace(' Green', '').replace('UL Monroe', 'Louisiana-Monroe').replace(' Golden', '').replace(' Thundering', '').replace(' Fighting', '').replace(' Nittany', '').replace('UTSA', 'Texas-San Antonio').replace(' Horned', '').replace(' Mean', '').replace(' Scarlet', '').replace(' Rainbow', '').replace(' Crimson', ''))



#Matching up thepredictiontracker teams with sports betting API teams
#Performing calculations to see if expected value of winnings on a $100 dollar bet is over $10 (10% return)

teamsToBetCFB=[]
potential_winnings=[]
winning_odds=[]
winning_book=[]

for i in range(len(AlphaAPI)):
    for j in range(len(CFB_weekly_games)):
        try:
            if (AlphaAPI[i]).lower() == (CFB_weekly_games[j][0].lower()):
                homeAlphaOdds = int((((Away[i])-1)*100)*(float(CFB_weekly_games[j][2]))-(100*(1-(float(CFB_weekly_games[j][2])))))
                if (homeAlphaOdds>7):
                    teamsToBetCFB.append({AlphaAPI[i]: homeAlphaOdds})
                    potential_winnings.append(int(((Away[i])-1)*100))
                    winning_odds.append(float(CFB_weekly_games[j][2]))
                    winning_book.append(bookAway[i])
        except KeyError:
            continue

        try:    
            if (BetaAPI[i]).lower() == (CFB_weekly_games[j][1].lower()):
                awayBetaOdds = int((((Home[i])-1)*100)*(float(CFB_weekly_games[j][3]))-(100*(1-(float(CFB_weekly_games[j][3])))))
                if (awayBetaOdds>7):
                    teamsToBetCFB.append({BetaAPI[i]: awayBetaOdds})
                    potential_winnings.append(int(((Home[i])-1)*100))
                    winning_odds.append(float(CFB_weekly_games[j][3]))
                    winning_book.append(bookHome[i])
        except KeyError:
            continue

        try:
            if (AlphaAPI[i]).lower() == (CFB_weekly_games[j][1].lower()):
                awayAlphaOdds = int((((Away[i])-1)*100)*(float(CFB_weekly_games[j][3]))-(100*(1-(float(CFB_weekly_games[j][3])))))
                if (awayAlphaOdds>7):
                    teamsToBetCFB.append({AlphaAPI[i]: awayAlphaOdds})
                    potential_winnings.append(int(((Away[i])-1)*100))
                    winning_odds.append(float(CFB_weekly_games[j][3]))
                    winning_book.append(bookAway[i])
        except KeyError:
            continue

        try:    
            if (BetaAPI[i]).lower() == (CFB_weekly_games[j][0].lower()):
                homeBetaOdds = int((((Home[i])-1)*100)*(float(CFB_weekly_games[j][2]))-(100*(1-(float(CFB_weekly_games[j][2])))))
                if (homeBetaOdds>7):
                    teamsToBetCFB.append({BetaAPI[i]: homeBetaOdds})
                    potential_winnings.append(int(((Home[i])-1)*100))
                    winning_odds.append(float(CFB_weekly_games[j][2]))
                    winning_book.append(bookHome[i])
        except KeyError:
            continue


 #Comment the below in if just want results for this one model   

print(teamsToBetCFB)

print(winning_book)
print(winning_odds)
print(potential_winnings)
print(len(AlphaAPI))
print(len(bookHome))
print(bookHome)



# teams = []

# for i in range(len(teamsToBetCFB)):
#     for key in teamsToBetCFB[i].keys():
#         teams.append(key)


# print(teams)



