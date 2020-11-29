from moneyline.moneylineCBB import theOddsAPIGames
from moneyline.moneylineSoccer import futureGame, yesterdayGame
import time
from datetime import datetime
from kenpompy.utils import login
from kenpompy.FanMatch import FanMatch
from API_Keys.vars import kpUser, kpPass


stringGameDate = str(futureGame)

stringYesterdayDate = str(yesterdayGame)

browser = login(kpUser, kpPass)
fm = FanMatch(browser, date = stringGameDate)

fmPast = FanMatch(browser, date = stringYesterdayDate)

# Parse sports betting API for sport, game time, teams, and odds

# Eventually bring in thepredictiontracker once season starts

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

FiveThirtyEightGamesYesterday = fmPast.fm_df['Winner']

loserTeams = fmPast.fm_df['Loser']

#Adding first team to AlphaAPI, second team to BetaAPI, first teams odds to OddsA, and second team odds to OddsB

for i in eventsAPI:
    if (datetime.utcfromtimestamp((eventsAPI[i][1][0]-30000)).strftime('%Y-%m-%d') == stringGameDate):
        AlphaAPIx.append(eventsAPI[i][2][0][0].rsplit(' ', 1)[0])
        BetaAPIx.append(eventsAPI[i][2][0][1].rsplit(' ', 1)[0])
        OddsA.append(eventsAPI[i][3][0]['h2h'][0])
        OddsB.append(eventsAPI[i][3][0]['h2h'][1])


#Cleaning up API names strings so that they match KenPom names strings
        
for i in range(len(AlphaAPIx)):
    AlphaAPI.append(AlphaAPIx[i].replace(' Tar', '').replace(' Bald', '').replace(' Bananna', '').replace(' Big', '').replace(' Black', '').replace(' Blue', '').replace(' Great', '').replace(' River', '').replace(' Green', '').replace(' Golden', '').replace(' Yellow', '').replace(' Fighting', '').replace(' Demon', '').replace(' Red', '').replace(" Runnin'", '').replace(' Nittany', '').replace(' Scarlet', '').replace(' Horned', '').replace(' Rainbow', '').replace(" Fightin'", '').replace(' Thundering', '').replace(' Mean', '').replace(' Purple', '').replace(' Wolf', '').replace(' Mountain', '').replace(' Crimson', '').replace(' Delta', '').replace(' Fighting', '').replace(" Ragin'", '').replace("-", '').replace("Miss ", 'Mississippi '))
    BetaAPI.append(BetaAPIx[i].replace(' Tar', '').replace(' Bald', '').replace(' Bananna', '').replace(' Big', '').replace(' Black', '').replace(' Blue', '').replace(' Great', '').replace(' River', '').replace(' Green', '').replace(' Golden', '').replace(' Yellow', '').replace(' Fighting', '').replace(' Demon', '').replace(' Red', '').replace(" Runnin'", '').replace(' Nittany', '').replace(' Scarlet', '').replace(' Horned', '').replace(' Rainbow', '').replace(" Fightin'", '').replace(' Thundering', '').replace(' Mean', '').replace(' Purple', '').replace(' Wolf', '').replace(' Mountain', '').replace(' Crimson', '').replace(' Delta', '').replace(' Fighting', '').replace(" Ragin'", '').replace("-", '').replace("Miss ", 'Mississippi '))


kpWinnersProjx=[]
kpLosersProjx=[]

kpWinnersProj=[]
kpLosersProj=[]
kpWinProb=[]

teamsToBetCBB=[]
potential_winnings=[]
winning_odds=[]

#Adding lists for KenPom projected winners, projected losers, and win probability

for i in range(len(fm.fm_df['PredictedWinner'])):
    try:
        kpWinProb.append(float(fm.fm_df['WinProbability'][i][:2])/100)

    except TypeError:
        continue
    
    kpWinnersProjx.append(fm.fm_df['PredictedWinner'][i])
    kpLosersProjx.append(fm.fm_df['PredictedLoser'][i])
    


for i in range(len(kpWinnersProjx)):
    kpWinnersProj.append(kpWinnersProjx[i].replace('.', ''))
    kpLosersProj.append(kpLosersProjx[i].replace('.', ''))



#Matching up KenPom teams with sports betting API teams
#Performing calculations to see if expected value of winnings on a $100 dollar bet is over $10 (10% return)

for i in range(len(AlphaAPI)):
    for j in range(len(kpWinnersProj)):
        try:
            if (AlphaAPI[i]).lower() == (kpWinnersProj[j].lower()):
                homeAlphaOdds = int(((((OddsA[i])-1)*100)*(kpWinProb[j])-(100*(1-(kpWinProb[j])))))
                if (homeAlphaOdds>10):
                    teamsToBetCBB.append({AlphaAPI[i]: homeAlphaOdds})
                    potential_winnings.append(int(((OddsA[i])-1)*100))
                    winning_odds.append(kpWinProb[j])
        except KeyError:
            continue

        try:    
            if (BetaAPI[i]).lower() == (kpLosersProj[j].lower()):
                awayBetaOdds = int(((((OddsB[i])-1)*100)*(1-(kpWinProb[j])))-(100*(kpWinProb[j])))
                if (awayBetaOdds>10):
                    teamsToBetCBB.append({BetaAPI[i]: awayBetaOdds})
                    potential_winnings.append(int(((OddsB[i])-1)*100))
                    winning_odds.append(1-kpWinProb[j])
        except KeyError:
            continue

        try:    
            if (AlphaAPI[i]).lower() == (kpLosersProj[j].lower()):
                awayAlphaOdds = int(((((OddsA[i])-1)*100)*(1-(kpWinProb[j]))-(100*(kpWinProb[j]))))
                if (awayAlphaOdds>10):
                    teamsToBetCBB.append({AlphaAPI[i]: awayAlphaOdds})
                    potential_winnings.append(int(((OddsA[i])-1)*100))
                    winning_odds.append(1-kpWinProb[j])
        except KeyError:
            continue


        try:
            if (BetaAPI[i]).lower() == (kpWinnersProj[j].lower()):
                homeBetaOdds = int(((((OddsB[i])-1)*100)*((kpWinProb[j])))-(100*(1-(kpWinProb[j]))))
                if (homeBetaOdds>10):
                    teamsToBetCBB.append({BetaAPI[i]: homeBetaOdds})
                    potential_winnings.append(int(((OddsB[i])-1)*100))
                    winning_odds.append(kpWinProb[j])
        except KeyError:
            continue


 #Comment the below in if just want results for this one model   

print(teamsToBetCBB)
