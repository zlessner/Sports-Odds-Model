from moneyline.moneylineCBB import theOddsAPIGames
from moneyline.moneylineSoccer import stringGameDate, stringYesterdayDate, nowTime
import time
from datetime import datetime
from kenpompy.utils import login
from kenpompy.FanMatch import FanMatch
from API_Keys.vars import kpUser, kpPass
import numpy as np


browser = login(kpUser, kpPass)
fm = FanMatch(browser, date = stringGameDate)

fmPast = FanMatch(browser, date = stringYesterdayDate)


#Adding lists for KenPom projected winners, projected losers, and win probability


kpWinnersProj=[]
kpLosersProj=[]
kpWinProb=[]
kpLoseProb= []

for i in range(len(fm.fm_df['PredictedWinner'])):
    try:
        kpWinProb.append(float(fm.fm_df['WinProbability'][i][:2])/100)

    except TypeError:
        continue
    
    kpWinnersProj.append(fm.fm_df['PredictedWinner'][i])
    kpLosersProj.append(fm.fm_df['PredictedLoser'][i])


for i in range(len(kpWinProb)):
    kpLoseProb.append(1-kpWinProb[i])








# Parse sports betting API for sport, game time, teams, and odds

# Eventually bring in thepredictiontracker once season starts

eventsAPI = {}

Home = []
Away = []
bestHome = 0
bestAway = 0
bookHome = []
bookAway = []
totalLeft = []
totalRight = []
bestBookHome = ''
bestBookAway = ''
bestHome = 0
bestAway = 0
totalHome = 0
totalAway = 0
siteCount = 0


# Extracting best odds and sportbook names with best odds
for i in range(len(theOddsAPIGames)):
    if (datetime.utcfromtimestamp(([theOddsAPIGames[i]['commence_time']][0]-30000)).strftime('%Y-%m-%d') == stringGameDate):

        if len(theOddsAPIGames[i]['sites']) > 0:
            siteCount = len(theOddsAPIGames[i]['sites'])
        
            for j in range(siteCount):

                # if I wanted to use just one specific sports book use the below code
                # if theOddsAPIGames[i]['sites'][j]['site_key'] == 'mybookieag':
                    # print([theOddsAPIGames[i]['sites'][j]['odds']['h2h'][1]])
                    # Home.append(([theOddsAPIGames[i]['sites'][j]['odds']['h2h'][1]][0]))

                # if theOddsAPIGames[i]['sites'][j]['site_key'] == 'gtbets':
                #     print([theOddsAPIGames[i]['sites'][j]['odds']['h2h'][1]])


                
                eventsAPI[i] = [theOddsAPIGames[i]['sport_key']], [theOddsAPIGames[i]['commence_time']], [theOddsAPIGames[i]['teams']], [theOddsAPIGames[i]['sites'][j]['odds']], [theOddsAPIGames[i]['sites'][j]['site_key']], [theOddsAPIGames[i]['home_team']]
                # break
                if theOddsAPIGames[i]['sites'][j]['site_key'] == 'betfair':
                    if siteCount != 1:
                        siteCount = siteCount - 1
                if theOddsAPIGames[i]['sites'][j]['site_key'] != 'betfair':
                    totalHome = totalHome + [theOddsAPIGames[i]['sites'][j]['odds']['h2h'][0]][0]
                    totalAway = totalAway + [theOddsAPIGames[i]['sites'][j]['odds']['h2h'][1]][0]
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
            # if siteCount == 0:
            #     siteCount = 1
            totalLeft.append((totalHome-siteCount)/siteCount)
            # print(totalHome)
            totalRight.append((totalAway-siteCount)/siteCount)
            bestHome = 0
            bestAway = 0
            totalHome = 0
            totalAway = 0



for i in range(len(totalLeft)):
    if totalLeft[i] > 0:
        totalLeft[i] = (100/(100+(totalLeft[i]*100)))
        totalRight[i] = (100/(100+(totalRight[i]*100)))


noVigLeft = []
noVigRight = []

for i in range(len(totalLeft)):
    if totalLeft[i] != -1:
        noVigLeft.append(totalLeft[i]/(totalLeft[i]+ totalRight[i]))
        noVigRight.append(totalRight[i]/(totalLeft[i]+ totalRight[i]))


AlphaAPIx=[]
BetaAPIx=[]
AlphaAPI=[]
BetaAPI=[]

FiveThirtyEightGamesYesterday = fmPast.fm_df['Winner']

loserTeams = fmPast.fm_df['Loser']

playedTeams = FiveThirtyEightGamesYesterday.append(loserTeams, ignore_index=True)

# print(playedTeams)

#Adding Home team to AlphaAPI, Away team to BetaAPI, Home teams odds to OddsA, and Away team odds to OddsB

# for i in eventsAPI:
#     if (datetime.utcfromtimestamp((eventsAPI[i][1][0]-30000)).strftime('%Y-%m-%d') == stringGameDate):
#         if eventsAPI[i][2][0][1] == eventsAPI[i][5][0]:
#             print(eventsAPI[i][2][0][1])
#             print(eventsAPI[i][5][0])
#             AlphaAPIx.append(eventsAPI[i][2][0][1].replace('St ', 'St. ').rsplit(' ', 1)[0])
#             BetaAPIx.append(eventsAPI[i][2][0][0].replace('St ', 'St. ').rsplit(' ', 1)[0])
#         # OddsA.append(eventsAPI[i][3][0]['h2h'][0])
#         # OddsB.append(eventsAPI[i][3][0]['h2h'][1])
#         # else:
#         #     AlphaAPIx.append(eventsAPI[i][2][0][0].replace('St ', 'St. ').rsplit(' ', 1)[0])
#         #     BetaAPIx.append(eventsAPI[i][2][0][1].replace('St ', 'St. ').rsplit(' ', 1)[0])




for i in eventsAPI:
    if (datetime.utcfromtimestamp((eventsAPI[i][1][0]-30000)).strftime('%Y-%m-%d') == stringGameDate):
        AlphaAPIx.append(eventsAPI[i][2][0][0].replace('St ', 'St. ').rsplit(' ', 1)[0])
        BetaAPIx.append(eventsAPI[i][2][0][1].replace('St ', 'St. ').rsplit(' ', 1)[0])
        # OddsA.append(eventsAPI[i][3][0]['h2h'][0])
        # OddsB.append(eventsAPI[i][3][0]['h2h'][1])



# print(Home)
# print(Away)
# print(OddsB)
# print(OddsA)
# print(bookHome)
# print(bookAway)


#Cleaning up API names strings so that they match KenPom names strings
        
for i in range(len(AlphaAPIx)):
    AlphaAPI.append(AlphaAPIx[i].replace(' Tar', '').replace(' Bald', '').replace(' Bananna', '').replace(' Big', '').replace(' Black', '').replace(' Blue', '').replace(' Great', '').replace(' River', '').replace(' Green', '').replace(' Golden', '').replace(' Yellow', '').replace(' Fighting', '').replace(' Demon', '').replace(' Red', '').replace(" Runnin'", '').replace(' Nittany', '').replace(' Scarlet', '').replace(' Horned', '').replace(' Rainbow', '').replace(" Fightin'", '').replace(' Thundering', '').replace(' Mean', '').replace(' Purple', '').replace(' Wolf', '').replace(' Mountain', '').replace(' Crimson', '').replace(' Delta', '').replace(' Fighting', '').replace(" Ragin'", '').replace("-", '').replace("Miss ", 'Mississippi ').replace(' Demons', '').replace(' Anteaters', '').replace('Arkansas-Little', 'Little').replace('ArkansasLittle', 'Little'))
    BetaAPI.append(BetaAPIx[i].replace(' Tar', '').replace(' Bald', '').replace(' Bananna', '').replace(' Big', '').replace(' Black', '').replace(' Blue', '').replace(' Great', '').replace(' River', '').replace(' Green', '').replace(' Golden', '').replace(' Yellow', '').replace(' Fighting', '').replace(' Demon', '').replace(' Red', '').replace(" Runnin'", '').replace(' Nittany', '').replace(' Scarlet', '').replace(' Horned', '').replace(' Rainbow', '').replace(" Fightin'", '').replace(' Thundering', '').replace(' Mean', '').replace(' Purple', '').replace(' Wolf', '').replace(' Mountain', '').replace(' Crimson', '').replace(' Delta', '').replace(' Fighting', '').replace(" Ragin'", '').replace("-", '').replace("Miss ", 'Mississippi ').replace(' Demons', '').replace(' Anteaters', '').replace('Arkansas-Little', 'Little').replace('ArkansasLittle', 'Little'))




teamsToBetCBB=[]
potential_winnings=[]
winning_odds=[]
winning_book=[]



print(kpWinProb)
print(kpLoseProb)




midDayWinProb = []
midDayLoseProb = []










set_2 = frozenset(playedTeams)
midDayWinnersProj = [x for x in kpWinnersProj if x not in set_2]
midDayLosersProj = [x for x in kpLosersProj if x not in set_2]

print(midDayWinnersProj)
print(midDayLosersProj)




#Matching up KenPom teams with sports betting API teams - from best odds for sportsbooks available
#Performing calculations to see if expected value of winnings on a $100 dollar bet is over $20 (20% return)

for i in range(len(AlphaAPI)):
    for j in range(len(kpWinnersProj)):
        try:
            if (AlphaAPI[i]).lower() == (kpWinnersProj[j].lower()):
                # kpWinProb[j] = (kpWinProb[j] + noVigLeft[i])/2
                # kpLoseProb[j] = 1-kpWinProb[j]
                HomeAlphaOdds = int(((((Away[i])-1)*100)*(kpWinProb[j])-(100*(kpLoseProb[j]))))
                if (HomeAlphaOdds>7):
                    teamsToBetCBB.append({AlphaAPI[i]: round(HomeAlphaOdds)})
                    potential_winnings.append(int(((Away[i])-1)*100))
                    winning_odds.append(kpWinProb[j])
                    winning_book.append(bookAway[i])
        except KeyError:
            continue

        try:    
            if (BetaAPI[i]).lower() == (kpLosersProj[j].lower()):
                # kpLoseProb[j] = (kpLoseProb[j] + noVigRight[i])/2
                # kpWinProb[j] = 1-kpLoseProb[j]
                AwayBetaOdds = int(((((Home[i])-1)*100)*(kpLoseProb[j])))-(100*(kpWinProb[j]))
                if (AwayBetaOdds>7):
                    teamsToBetCBB.append({BetaAPI[i]: round(AwayBetaOdds)})
                    potential_winnings.append(int(((Home[i])-1)*100))
                    winning_odds.append(kpLoseProb[j])
                    winning_book.append(bookHome[i])
        except KeyError:
            continue

        try:    
            if (AlphaAPI[i]).lower() == (kpLosersProj[j].lower()):
                # kpLoseProb[j] = (kpLoseProb[j] + noVigLeft[i])/2
                # kpWinProb[j] = 1-kpLoseProb[j]
                AwayAlphaOdds = int(((((Away[i])-1)*100)*(kpLoseProb[j]))-(100*(kpWinProb[j])))
                if (AwayAlphaOdds>7):
                    teamsToBetCBB.append({AlphaAPI[i]: round(AwayAlphaOdds)})
                    potential_winnings.append(int(((Away[i])-1)*100))
                    winning_odds.append(kpLoseProb[j])
                    winning_book.append(bookAway[i])
        except KeyError:
            continue


        try:
            if (BetaAPI[i]).lower() == (kpWinnersProj[j].lower()):
                # kpWinProb[j] = (kpWinProb[j] + noVigRight[i])/2
                # kpLoseProb[j] = 1-kpWinProb[j]
                HomeBetaOdds = int(((((Home[i])-1)*100)*((kpWinProb[j])))-(100*(kpLoseProb[j])))
                if (HomeBetaOdds>7):
                    teamsToBetCBB.append({BetaAPI[i]: round(HomeBetaOdds)})
                    potential_winnings.append(int(((Home[i])-1)*100))
                    winning_odds.append(kpWinProb[j])
                    winning_book.append(bookHome[i])
        except KeyError:
            continue


 #Comment the below in if just want results for this one model   

print(teamsToBetCBB)

print(potential_winnings)
print(winning_book)
print(winning_odds)
print(len(AlphaAPI))
print(BetaAPI)
print(len(kpWinnersProj))
print(len(noVigRight))
# print(noVigLeft)
# print(noVigRight)
# print(kpWinProb)
# print(kpLoseProb)

print(noVigLeft)
print(noVigRight)