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

First = []
Second = []
bestFirst = 0
bestSecond = 0
bookFirst = []
bookSecond = []
totalLeft = []
totalRight = []
bestBookFirst = ''
bestBookSecond = ''
bestFirst = 0
bestSecond = 0
totalFirst = 0
totalSecond = 0
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
                    # First.append(([theOddsAPIGames[i]['sites'][j]['odds']['h2h'][1]][0]))

                # if theOddsAPIGames[i]['sites'][j]['site_key'] == 'gtbets':
                #     print([theOddsAPIGames[i]['sites'][j]['odds']['h2h'][1]])


                
                eventsAPI[i] = [theOddsAPIGames[i]['sport_key']], [theOddsAPIGames[i]['commence_time']], [theOddsAPIGames[i]['teams']], [theOddsAPIGames[i]['sites'][j]['odds']], [theOddsAPIGames[i]['sites'][j]['site_key']]
                # break
                if theOddsAPIGames[i]['sites'][j]['site_key'] == 'betfair':
                    if siteCount != 1:
                        siteCount = siteCount - 1
                if theOddsAPIGames[i]['sites'][j]['site_key'] != 'betfair':
                    totalFirst = totalFirst + [theOddsAPIGames[i]['sites'][j]['odds']['h2h'][0]][0]
                    totalSecond = totalSecond + [theOddsAPIGames[i]['sites'][j]['odds']['h2h'][1]][0]
                    if [theOddsAPIGames[i]['sites'][j]['odds']['h2h'][1]][0] > bestFirst:
                        bestFirst = [theOddsAPIGames[i]['sites'][j]['odds']['h2h'][1]][0]
                        bestBookFirst = theOddsAPIGames[i]['sites'][j]['site_key']
                    if [theOddsAPIGames[i]['sites'][j]['odds']['h2h'][0]][0] > bestSecond:
                        bestSecond = [theOddsAPIGames[i]['sites'][j]['odds']['h2h'][0]][0]
                        bestBookSecond = theOddsAPIGames[i]['sites'][j]['site_key']

            First.append(bestFirst)
            Second.append(bestSecond)
            bookFirst.append(bestBookFirst)
            bookSecond.append(bestBookSecond)
            # if siteCount == 0:
            #     siteCount = 1
            totalLeft.append((totalFirst-siteCount)/siteCount)
            # print(totalFirst)
            totalRight.append((totalSecond-siteCount)/siteCount)
            bestFirst = 0
            bestSecond = 0
            totalFirst = 0
            totalSecond = 0



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

#Adding first team to AlphaAPI, second team to BetaAPI, first teams odds to OddsA, and second team odds to OddsB

for i in eventsAPI:
    if (datetime.utcfromtimestamp((eventsAPI[i][1][0]-30000)).strftime('%Y-%m-%d') == stringGameDate):
        AlphaAPIx.append(eventsAPI[i][2][0][0].replace('St ', 'St. ').rsplit(' ', 1)[0])
        BetaAPIx.append(eventsAPI[i][2][0][1].replace('St ', 'St. ').rsplit(' ', 1)[0])
        # OddsA.append(eventsAPI[i][3][0]['h2h'][0])
        # OddsB.append(eventsAPI[i][3][0]['h2h'][1])


# print(First)
# print(Second)
# print(OddsB)
# print(OddsA)
# print(bookFirst)
# print(bookSecond)


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
                FirstAlphaOdds = int(((((Second[i])-1)*100)*(kpWinProb[j])-(100*(kpLoseProb[j]))))
                if (FirstAlphaOdds>7):
                    teamsToBetCBB.append({AlphaAPI[i]: round(FirstAlphaOdds)})
                    potential_winnings.append(int(((Second[i])-1)*100))
                    winning_odds.append(kpWinProb[j])
                    winning_book.append(bookSecond[i])
        except KeyError:
            continue

        try:    
            if (BetaAPI[i]).lower() == (kpLosersProj[j].lower()):
                # kpLoseProb[j] = (kpLoseProb[j] + noVigRight[i])/2
                # kpWinProb[j] = 1-kpLoseProb[j]
                SecondBetaOdds = int(((((First[i])-1)*100)*(kpLoseProb[j])))-(100*(kpWinProb[j]))
                if (SecondBetaOdds>7):
                    teamsToBetCBB.append({BetaAPI[i]: round(SecondBetaOdds)})
                    potential_winnings.append(int(((First[i])-1)*100))
                    winning_odds.append(kpLoseProb[j])
                    winning_book.append(bookFirst[i])
        except KeyError:
            continue

        try:    
            if (AlphaAPI[i]).lower() == (kpLosersProj[j].lower()):
                # kpLoseProb[j] = (kpLoseProb[j] + noVigLeft[i])/2
                # kpWinProb[j] = 1-kpLoseProb[j]
                SecondAlphaOdds = int(((((Second[i])-1)*100)*(kpLoseProb[j]))-(100*(kpWinProb[j])))
                if (SecondAlphaOdds>7):
                    teamsToBetCBB.append({AlphaAPI[i]: round(SecondAlphaOdds)})
                    potential_winnings.append(int(((Second[i])-1)*100))
                    winning_odds.append(kpLoseProb[j])
                    winning_book.append(bookSecond[i])
        except KeyError:
            continue


        try:
            if (BetaAPI[i]).lower() == (kpWinnersProj[j].lower()):
                # kpWinProb[j] = (kpWinProb[j] + noVigRight[i])/2
                # kpLoseProb[j] = 1-kpWinProb[j]
                FirstBetaOdds = int(((((First[i])-1)*100)*((kpWinProb[j])))-(100*(kpLoseProb[j])))
                if (FirstBetaOdds>7):
                    teamsToBetCBB.append({BetaAPI[i]: round(FirstBetaOdds)})
                    potential_winnings.append(int(((First[i])-1)*100))
                    winning_odds.append(kpWinProb[j])
                    winning_book.append(bookFirst[i])
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