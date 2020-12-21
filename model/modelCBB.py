from moneyline.moneylineCBB import theOddsAPIGames
from moneyline.moneylineSoccer import stringGameDate, stringYesterdayDate, nowTime
import time
from datetime import datetime
from kenpompy.utils import login
from kenpompy.FanMatch import FanMatch
from API_Keys.vars import kpUser, kpPass


browser = login(kpUser, kpPass)
fm = FanMatch(browser, date = stringGameDate)

fmPast = FanMatch(browser, date = stringYesterdayDate)

# Parse sports betting API for sport, game time, teams, and odds

# Eventually bring in thepredictiontracker once season starts

eventsAPI = {}

home = []
away = []
bestHome = 0
bestAway = 0
bookHome = []
bookAway =[]
# put all home and away odds (from all books) per game into array

for i in range(len(theOddsAPIGames)):
    for j in range(len(theOddsAPIGames[i]['sites'])):
        
        # if theOddsAPIGames[i]['sites'][j]['site_key'] == 'mybookieag':
            # print([theOddsAPIGames[i]['sites'][j]['odds']['h2h'][1]])
            # home.append(([theOddsAPIGames[i]['sites'][j]['odds']['h2h'][1]][0]))

        # if theOddsAPIGames[i]['sites'][j]['site_key'] == 'gtbets':
        #     print([theOddsAPIGames[i]['sites'][j]['odds']['h2h'][1]])


        eventsAPI[i] = [theOddsAPIGames[i]['sport_key']], [theOddsAPIGames[i]['commence_time']], [theOddsAPIGames[i]['teams']], [theOddsAPIGames[i]['sites'][j]['odds']], [theOddsAPIGames[i]['sites'][j]['site_key']]
        break

# print(home)

# print(eventsAPI)

for i in range(len(theOddsAPIGames)):
    if (datetime.utcfromtimestamp((eventsAPI[i][1][0]-30000)).strftime('%Y-%m-%d') == stringGameDate):
        for j in range(len(theOddsAPIGames[i]['sites'])):
            # print(theOddsAPIGames[i]['sites'][j]['site_key'])
            # print([theOddsAPIGames[i]['sites'][j]['odds']['h2h'][1]][0])
            if [theOddsAPIGames[i]['sites'][j]['odds']['h2h'][1]][0] > bestHome:
                bestHome = [theOddsAPIGames[i]['sites'][j]['odds']['h2h'][1]][0]
                bestBookHome = theOddsAPIGames[i]['sites'][j]['site_key']
            if [theOddsAPIGames[i]['sites'][j]['odds']['h2h'][0]][0] > bestAway:
                bestAway = [theOddsAPIGames[i]['sites'][j]['odds']['h2h'][0]][0]
                bestBookAway = theOddsAPIGames[i]['sites'][j]['site_key']
        # print("----")
        home.append(bestHome)
        away.append(bestAway)
        bookHome.append(bestBookHome)
        bookAway.append(bestBookAway)
        bestHome = 0
        bestAway = 0




# sites=[]
# for i in range(len(theOddsAPIGames)):
#         sites.append([theOddsAPIGames[i]])
        
# for i in range(len(theOddsAPIGames)):
#     for j in range(len(theOddsAPIGames)):
#         print(sites[j][j]['sites'][j]['site_key'])


AlphaAPIx=[]
BetaAPIx=[]
AlphaAPI=[]
BetaAPI=[]
# OddsA=[]
# OddsB=[]

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


# print(home)
# print(away)
# print(OddsB)
# print(OddsA)
# print(bookHome)
# print(bookAway)


#Cleaning up API names strings so that they match KenPom names strings
        
for i in range(len(AlphaAPIx)):
    AlphaAPI.append(AlphaAPIx[i].replace(' Tar', '').replace(' Bald', '').replace(' Bananna', '').replace(' Big', '').replace(' Black', '').replace(' Blue', '').replace(' Great', '').replace(' River', '').replace(' Green', '').replace(' Golden', '').replace(' Yellow', '').replace(' Fighting', '').replace(' Demon', '').replace(' Red', '').replace(" Runnin'", '').replace(' Nittany', '').replace(' Scarlet', '').replace(' Horned', '').replace(' Rainbow', '').replace(" Fightin'", '').replace(' Thundering', '').replace(' Mean', '').replace(' Purple', '').replace(' Wolf', '').replace(' Mountain', '').replace(' Crimson', '').replace(' Delta', '').replace(' Fighting', '').replace(" Ragin'", '').replace("-", '').replace("Miss ", 'Mississippi '))
    BetaAPI.append(BetaAPIx[i].replace(' Tar', '').replace(' Bald', '').replace(' Bananna', '').replace(' Big', '').replace(' Black', '').replace(' Blue', '').replace(' Great', '').replace(' River', '').replace(' Green', '').replace(' Golden', '').replace(' Yellow', '').replace(' Fighting', '').replace(' Demon', '').replace(' Red', '').replace(" Runnin'", '').replace(' Nittany', '').replace(' Scarlet', '').replace(' Horned', '').replace(' Rainbow', '').replace(" Fightin'", '').replace(' Thundering', '').replace(' Mean', '').replace(' Purple', '').replace(' Wolf', '').replace(' Mountain', '').replace(' Crimson', '').replace(' Delta', '').replace(' Fighting', '').replace(" Ragin'", '').replace("-", '').replace("Miss ", 'Mississippi '))


kpWinnersProj=[]
kpLosersProj=[]
kpWinProb=[]

teamsToBetCBB=[]
potential_winnings=[]
winning_odds=[]
winning_book=[]


#Adding lists for KenPom projected winners, projected losers, and win probability

for i in range(len(fm.fm_df['PredictedWinner'])):
    try:
        kpWinProb.append(float(fm.fm_df['WinProbability'][i][:2])/100)

    except TypeError:
        continue
    
    kpWinnersProj.append(fm.fm_df['PredictedWinner'][i])
    kpLosersProj.append(fm.fm_df['PredictedLoser'][i])


#Matching up KenPom teams with sports betting API teams
#Performing calculations to see if expected value of winnings on a $100 dollar bet is over $10 (10% return)

for i in range(len(AlphaAPI)):
    for j in range(len(kpWinnersProj)):
        try:
            if (AlphaAPI[i]).lower() == (kpWinnersProj[j].lower()):
                homeAlphaOdds = int(((((away[i])-1)*100)*(kpWinProb[j])-(100*(1-(kpWinProb[j])))))
                if (homeAlphaOdds>7):
                    teamsToBetCBB.append({AlphaAPI[i]: homeAlphaOdds})
                    potential_winnings.append(int(((away[i])-1)*100))
                    winning_odds.append(kpWinProb[j])
                    winning_book.append(bookAway[i])
        except KeyError:
            continue

        try:    
            if (BetaAPI[i]).lower() == (kpLosersProj[j].lower()):
                awayBetaOdds = int(((((home[i])-1)*100)*(1-(kpWinProb[j])))-(100*(kpWinProb[j])))
                if (awayBetaOdds>7):
                    teamsToBetCBB.append({BetaAPI[i]: awayBetaOdds})
                    potential_winnings.append(int(((home[i])-1)*100))
                    winning_odds.append(1-kpWinProb[j])
                    winning_book.append(bookHome[i])
        except KeyError:
            continue

        try:    
            if (AlphaAPI[i]).lower() == (kpLosersProj[j].lower()):
                awayAlphaOdds = int(((((away[i])-1)*100)*(1-(kpWinProb[j]))-(100*(kpWinProb[j]))))
                if (awayAlphaOdds>7):
                    teamsToBetCBB.append({AlphaAPI[i]: awayAlphaOdds})
                    potential_winnings.append(int(((away[i])-1)*100))
                    winning_odds.append(1-kpWinProb[j])
                    winning_book.append(bookAway[i])
        except KeyError:
            continue


        try:
            if (BetaAPI[i]).lower() == (kpWinnersProj[j].lower()):
                homeBetaOdds = int(((((home[i])-1)*100)*((kpWinProb[j])))-(100*(1-(kpWinProb[j]))))
                if (homeBetaOdds>7):
                    teamsToBetCBB.append({BetaAPI[i]: homeBetaOdds})
                    potential_winnings.append(int(((home[i])-1)*100))
                    winning_odds.append(kpWinProb[j])
                    winning_book.append(bookHome[i])
        except KeyError:
            continue


 #Comment the below in if just want results for this one model   

print(teamsToBetCBB)

# print(potential_winnings)
# print(winning_book)
