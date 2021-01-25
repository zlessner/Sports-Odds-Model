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
bookAway =[]
totalHomeAvg = []
totalAwayAvg = []
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

                #putting home team Home, away team Away
                if theOddsAPIGames[i]['sites'][j]['site_key'] != 'betfair':
                    if eventsAPI[i][2][0][1] == eventsAPI[i][5][0]:
                        totalHome = totalHome + [theOddsAPIGames[i]['sites'][j]['odds']['h2h'][1]][0]
                        totalAway = totalAway + [theOddsAPIGames[i]['sites'][j]['odds']['h2h'][0]][0]

                    else:
                        totalHome = totalHome + [theOddsAPIGames[i]['sites'][j]['odds']['h2h'][0]][0]
                        totalAway = totalAway + [theOddsAPIGames[i]['sites'][j]['odds']['h2h'][1]][0]


                    if eventsAPI[i][2][0][1] == eventsAPI[i][5][0]:
                        if [theOddsAPIGames[i]['sites'][j]['odds']['h2h'][0]][0] > bestHome:
                            bestHome = [theOddsAPIGames[i]['sites'][j]['odds']['h2h'][0]][0]
                            bestBookHome = theOddsAPIGames[i]['sites'][j]['site_key']


                    else:
                        if [theOddsAPIGames[i]['sites'][j]['odds']['h2h'][1]][0] > bestHome:
                            bestHome = [theOddsAPIGames[i]['sites'][j]['odds']['h2h'][1]][0]
                            bestBookHome = theOddsAPIGames[i]['sites'][j]['site_key']


                    if eventsAPI[i][2][0][1] == eventsAPI[i][5][0]:
                        if [theOddsAPIGames[i]['sites'][j]['odds']['h2h'][1]][0] > bestAway:
                            bestAway = [theOddsAPIGames[i]['sites'][j]['odds']['h2h'][1]][0]
                            bestBookAway = theOddsAPIGames[i]['sites'][j]['site_key']

                    else:
                        if [theOddsAPIGames[i]['sites'][j]['odds']['h2h'][0]][0] > bestAway:
                            bestAway = [theOddsAPIGames[i]['sites'][j]['odds']['h2h'][0]][0]
                            bestBookAway = theOddsAPIGames[i]['sites'][j]['site_key']


            Home.append(bestHome)
            Away.append(bestAway)
            bookHome.append(bestBookHome)
            bookAway.append(bestBookAway)
            totalHomeAvg.append((totalHome-siteCount)/siteCount)
            totalAwayAvg.append((totalAway-siteCount)/siteCount)
            bestHome = 0
            bestAway = 0
            totalHome = 0
            totalAway = 0



for i in range(len(totalHomeAvg)):
    if totalHomeAvg[i] > 0:
        totalHomeAvg[i] = (100/(100+(totalHomeAvg[i]*100)))
        totalAwayAvg[i] = (100/(100+(totalAwayAvg[i]*100)))


homeNoVig = []
awayNoVig = []


# real odds of winning according to book without the vig
for i in range(len(totalHomeAvg)):
    if totalHomeAvg[i] != -1:
        homeNoVig.append(totalHomeAvg[i]/(totalHomeAvg[i]+ totalAwayAvg[i]))
        awayNoVig.append(totalAwayAvg[i]/(totalHomeAvg[i]+ totalAwayAvg[i]))

# for i in range(len(homeNoVig)):
#     if homeNoVig[i] == 0:
#         homeNoVig[i] = 0.001


AlphaAPIx=[]
BetaAPIx=[]
AlphaAPI=[]
BetaAPI=[]

FiveThirtyEightGamesYesterday = fmPast.fm_df['Winner']

loserTeams = fmPast.fm_df['Loser']

playedTeams = FiveThirtyEightGamesYesterday.append(loserTeams, ignore_index=True)

# print(playedTeams)

#Adding Home team to AlphaAPI, Away team to BetaAPI, Home teams odds to OddsA, and Away team odds to OddsB

for i in eventsAPI:
    # if (datetime.utcfromtimestamp((eventsAPI[i][1][0])-30000).strftime('%Y-%m-%d') == stringGameDate):
    if eventsAPI[i][2][0][1] == eventsAPI[i][5][0]:
        AlphaAPIx.append(eventsAPI[i][2][0][1].replace('St ', 'St. ').replace('Miami Hurricanes', 'Miami Hurricanes Hurricanes').rsplit(' ', 1)[0])
        BetaAPIx.append(eventsAPI[i][2][0][0].replace('St ', 'St. ').replace('Miami Hurricanes', 'Miami Hurricanes Hurricanes').rsplit(' ', 1)[0])
    else:
        AlphaAPIx.append(eventsAPI[i][2][0][0].replace('St ', 'St. ').replace('Miami Hurricanes', 'Miami Hurricanes Hurricanes').rsplit(' ', 1)[0])
        BetaAPIx.append(eventsAPI[i][2][0][1].replace('St ', 'St. ').replace('Miami Hurricanes', 'Miami Hurricanes Hurricanes').rsplit(' ', 1)[0])


# print(Home)
# print(Away)
# print(OddsB)
# print(OddsA)
# print(bookHome)
# print(bookAway)


#Cleaning up API names strings so that they match KenPom names strings
        
for i in range(len(AlphaAPIx)):
    AlphaAPI.append(AlphaAPIx[i].replace(' Tar', '').replace(' Bald', '').replace(' Bananna', '').replace(' Big', '').replace(' Black', '').replace(' Blue', '').replace(' Great', '').replace(' River', '').replace(' Green', '').replace(' Golden', '').replace(' Yellow', '').replace(' Fighting', '').replace(' Demon', '').replace(' Red', '').replace(" Runnin'", '').replace(' Nittany', '').replace(' Scarlet', '').replace(' Horned', '').replace(' Rainbow', '').replace(" Fightin'", '').replace(' Thundering', '').replace(' Mean', '').replace(' Purple', '').replace(' Wolf', '').replace(' Mountain', '').replace(' Crimson', '').replace(' Delta', '').replace(' Fighting', '').replace(" Ragin'", '').replace("-", '').replace("Miss ", 'Mississippi ').replace(' Demons', '').replace(' Anteaters', '').replace('Arkansas-Little', 'Little').replace('ArkansasLittle', 'Little').replace('GardnerWebb', 'Gardner Webb').replace('South Carolina Upstate', 'USC Upstate').replace('NC State', 'N.C. State').replace('UConn', 'Connecticut').replace('Boston Univ.', 'Boston University').replace('Bowling', 'Bowling Green').replace('Iowa State', 'Iowa St.').replace('Kent State', 'Kent St.').replace('Miami Hurricanes', 'Miami FL').replace('St. Francis BKN', 'St. Francis NY').replace('LIU Brooklyn', 'LIU').replace('N Colorado', 'Northern Colorado').replace('Arizona St. Sun', 'Arizona St.').replace("Mt. St. Mary's", "Mount St. Mary's").replace("Central Connecticut St.", "Central Connecticut").replace("SE Missouri St.", "Southeast Missouri St.").replace("St. Francis (PA)", "St. Francis PA").replace("Idaho State", "Idaho St.").replace("TennMartin", "Tennessee Martin").replace("UCside", "UC Riverside").replace("UL Monroe", "Louisiana Monroe").replace("Fort Wayne", "Purdue Fort Wayne").replace("CSU Fullerton", "Cal St. Fullerton").replace("CSU Bakersfield", "Cal St. Bakersfield").replace("Hawai'i", "Hawaii").replace("UTArlington", "UT Arlington").replace("UIC", "Illinois Chicago").replace("Florida Int'l", "FIU").replace("Omaha", "Nebraska Omaha").replace("San José St.", "San Jose St.").replace("Utah State", "Utah St.").replace("San Diego", "UC San Diego").replace("UC San Diego St.", "San Diego St.").replace("Boise State", "Boise St.").replace("Ole Miss", "Mississippi").replace("Loyola (Chi)", "Loyola Chicago").replace("Prairie View", "Prairie View A&M").replace("SIUEdwardsville", "SIU Edwardsville").replace("Miami (OH)", "Miami OH").replace("Ball State", "Ball St.").replace("Ohio State", "Ohio St.").replace("Detroit Mercy", "Detroit").replace("CSU Northridge", "Cal St. Northridge").replace("Texas State", "Texas St.").replace("UNCsboro", "UNC Greensboro").replace("SE Louisiana", "Southeastern Louisiana").replace("Loyola (MD)", "Loyola MD").replace("ArkansasPine Bluff", "Arkansas Pine Bluff").replace("Penn State", "Penn St.").replace("Texas A&MCC", "Texas A&M Corpus Chris").replace("Weber State", "Weber St.")) 
    BetaAPI.append(BetaAPIx[i].replace(' Tar', '').replace(' Bald', '').replace(' Bananna', '').replace(' Big', '').replace(' Black', '').replace(' Blue', '').replace(' Great', '').replace(' River', '').replace(' Green', '').replace(' Golden', '').replace(' Yellow', '').replace(' Fighting', '').replace(' Demon', '').replace(' Red', '').replace(" Runnin'", '').replace(' Nittany', '').replace(' Scarlet', '').replace(' Horned', '').replace(' Rainbow', '').replace(" Fightin'", '').replace(' Thundering', '').replace(' Mean', '').replace(' Purple', '').replace(' Wolf', '').replace(' Mountain', '').replace(' Crimson', '').replace(' Delta', '').replace(' Fighting', '').replace(" Ragin'", '').replace("-", '').replace("Miss ", 'Mississippi ').replace(' Demons', '').replace(' Anteaters', '').replace('Arkansas-Little', 'Little').replace('ArkansasLittle', 'Little').replace('GardnerWebb', 'Gardner Webb').replace('South Carolina Upstate', 'USC Upstate').replace('NC State', 'N.C. State').replace('UConn', 'Connecticut').replace('Boston Univ.', 'Boston University').replace('Bowling', 'Bowling Green').replace('Iowa State', 'Iowa St.').replace('Kent State', 'Kent St.').replace('Miami Hurricanes', 'Miami FL').replace('St. Francis BKN', 'St. Francis NY').replace('LIU Brooklyn', 'LIU').replace('N Colorado', 'Northern Colorado').replace('Arizona St. Sun', 'Arizona St.').replace("Mt. St. Mary's", "Mount St. Mary's").replace("Central Connecticut St.", "Central Connecticut").replace("SE Missouri St.", "Southeast Missouri St.").replace("St. Francis (PA)", "St. Francis PA").replace("Idaho State", "Idaho St.").replace("TennMartin", "Tennessee Martin").replace("UCside", "UC Riverside").replace("UL Monroe", "Louisiana Monroe").replace("Fort Wayne", "Purdue Fort Wayne").replace("CSU Fullerton", "Cal St. Fullerton").replace("CSU Bakersfield", "Cal St. Bakersfield").replace("Hawai'i", "Hawaii").replace("UTArlington", "UT Arlington").replace("UIC", "Illinois Chicago").replace("Florida Int'l", "FIU").replace("Omaha", "Nebraska Omaha").replace("San José St.", "San Jose St.").replace("Utah State", "Utah St.").replace("San Diego", "UC San Diego").replace("UC San Diego St.", "San Diego St.").replace("Boise State", "Boise St.").replace("Ole Miss", "Mississippi").replace("Loyola (Chi)", "Loyola Chicago").replace("Prairie View", "Prairie View A&M").replace("SIUEdwardsville", "SIU Edwardsville").replace("Miami (OH)", "Miami OH").replace("Ball State", "Ball St.").replace("Ohio State", "Ohio St.").replace("Detroit Mercy", "Detroit").replace("CSU Northridge", "Cal St. Northridge").replace("Texas State", "Texas St.").replace("UNCsboro", "UNC Greensboro").replace("SE Louisiana", "Southeastern Louisiana").replace("Loyola (MD)", "Loyola MD").replace("ArkansasPine Bluff", "Arkansas Pine Bluff").replace("Penn State", "Penn St.").replace("Texas A&MCC", "Texas A&M Corpus Chris").replace("Weber State", "Weber St."))               



midDayWinTeam = []
midDayLoseTeam = []
midDayWinProb = []
midDayLoseProb = []
discrepancy = []


for i in range(len(kpWinnersProj)):
        for k in range(len(AlphaAPI)):
            if kpWinnersProj[i].lower() == AlphaAPI[k].lower():
                if abs((kpWinProb[i]-homeNoVig[k])/homeNoVig[k]) > .25 or abs((kpWinProb[i]-homeNoVig[k])/kpWinProb[i]) > .25:
                    # print(FiveThirtyEightGames[i][3])
                    # print(homeNoVig[k])
                    discrepancy.append(kpWinnersProj[i] + " discrepancy")
                midDayWinProb.append(float(kpWinProb[i]+homeNoVig[k])/2)
                midDayWinTeam.append(kpWinnersProj[i])
            if kpWinnersProj[i].lower() == BetaAPI[k].lower():
                if abs((kpWinProb[i]-awayNoVig[k])/awayNoVig[k]) > .25 or abs((kpWinProb[i]-awayNoVig[k])/kpWinProb[i]) > .25:
                    # print(FiveThirtyEightGames[i][3])
                    # print(homeNoVig[k])
                    discrepancy.append(kpWinnersProj[i] + " discrepancy")
                midDayWinProb.append(float(kpWinProb[i]+awayNoVig[k])/2)
                midDayWinTeam.append(kpWinnersProj[i])
            if kpLosersProj[i].lower() == AlphaAPI[k].lower():
                if abs((kpLoseProb[i]-homeNoVig[k])/homeNoVig[k]) > .25 or abs((kpLoseProb[i]-homeNoVig[k])/kpLoseProb[i]) > .25:
                    # print(FiveThirtyEightGames[i][3])
                    # print(homeNoVig[k])
                    discrepancy.append(kpLosersProj[i] + " discrepancy")
                midDayLoseProb.append(float(kpLoseProb[i]+homeNoVig[k])/2)
                midDayLoseTeam.append(kpLosersProj[i])
            if kpLosersProj[i].lower() == BetaAPI[k].lower():
                if abs((kpLoseProb[i]-awayNoVig[k])/awayNoVig[k]) > .25 or abs((kpLoseProb[i]-awayNoVig[k])/kpLoseProb[i]) > .25:
                    # print(FiveThirtyEightGames[i][3])
                    # print(homeNoVig[k])
                    discrepancy.append(kpLosersProj[i] + " discrepancy")
                midDayLoseProb.append(float(kpLoseProb[i]+awayNoVig[k])/2)
                midDayLoseTeam.append(kpLosersProj[i])




teamsToBetCBB=[]
potential_winnings=[]
winning_odds=[]
winning_book=[]
break_point=[]
print(AlphaAPI)
print(len(AlphaAPI))
print(BetaAPI)
print(len(BetaAPI))
print(midDayWinTeam)
print(len(midDayWinTeam))
print(midDayLoseTeam)
print(len(midDayLoseTeam))





# print(kpWinProb)
# print(kpLoseProb)



#Matching up KenPom teams with sports betting API teams - from best odds for sportsbooks available
#Performing calculations to see if expected value of winnings on a $100 dollar bet is over $7 (7% return)

for i in range(len(AlphaAPI)):
    for j in range(len(midDayWinTeam)):
        try:
            if (AlphaAPI[i]).lower() == (midDayWinTeam[j].lower()):
                HomeAlphaOdds = int(((((Away[i])-1)*100)*(midDayWinProb[j])-(100*((1-midDayWinProb[j])))))
                if (HomeAlphaOdds>7):
                    for n in range(len(discrepancy)):
                        if discrepancy[n].rsplit(' ', 1)[0] == AlphaAPI[i]:
                            print(discrepancy[n])
                    break_point.append(round((107/midDayWinProb[j])-100))
                    teamsToBetCBB.append({AlphaAPI[i]: round(HomeAlphaOdds)})
                    potential_winnings.append(int(((Away[i])-1)*100))
                    winning_odds.append(midDayWinProb[j])
                    winning_book.append(bookAway[i])
        except KeyError:
            continue

        try:    
            if (BetaAPI[i]).lower() == (midDayLoseTeam[j].lower()):
                AwayBetaOdds = int(((((Home[i])-1)*100)*(midDayLoseProb[j])))-(100*((1-midDayLoseProb[j])))
                if (AwayBetaOdds>7):
                    for n in range(len(discrepancy)):
                        if discrepancy[n].rsplit(' ', 1)[0] == BetaAPI[i]:
                            print(discrepancy[n])
                    break_point.append(round((107/midDayLoseProb[j])-100))
                    teamsToBetCBB.append({BetaAPI[i]: round(AwayBetaOdds)})
                    potential_winnings.append(int(((Home[i])-1)*100))
                    winning_odds.append(midDayLoseProb[j])
                    winning_book.append(bookHome[i])
        except KeyError:
            continue

        try:    
            if (AlphaAPI[i]).lower() == (midDayLoseTeam[j].lower()):
                AwayAlphaOdds = int(((((Away[i])-1)*100)*(midDayLoseProb[j]))-(100*((1-midDayLoseProb[j]))))
                if (AwayAlphaOdds>7):
                    for n in range(len(discrepancy)):
                        if discrepancy[n].rsplit(' ', 1)[0] == AlphaAPI[i]:
                            print(discrepancy[n])
                    break_point.append(round((107/midDayLoseProb[j])-100))
                    teamsToBetCBB.append({AlphaAPI[i]: round(AwayAlphaOdds)})
                    potential_winnings.append(int(((Away[i])-1)*100))
                    winning_odds.append(midDayLoseProb[j])
                    winning_book.append(bookAway[i])
        except KeyError:
            continue


        try:
            if (BetaAPI[i]).lower() == (midDayWinTeam[j].lower()):
                HomeBetaOdds = int(((((Home[i])-1)*100)*((midDayWinProb[j])))-(100*((1-midDayWinProb[j]))))
                if (HomeBetaOdds>7):
                    for n in range(len(discrepancy)):
                        if discrepancy[n].rsplit(' ', 1)[0] == BetaAPI[i]:
                            print(discrepancy[n])
                    break_point.append(round((107/midDayWinProb[j])-100))
                    teamsToBetCBB.append({BetaAPI[i]: round(HomeBetaOdds)})
                    potential_winnings.append(int(((Home[i])-1)*100))
                    winning_odds.append(midDayWinProb[j])
                    winning_book.append(bookHome[i])
        except KeyError:
            continue


 #Comment the below in if just want results for this one model   

print(teamsToBetCBB)

print(potential_winnings)
print(winning_book)
print(winning_odds)
print(len(AlphaAPI))
print(len(bookHome))
# print(len(AlphaAPI))
# print(BetaAPI)
# print(len(homeNoVig))
# print(noVigLeft)
# print(noVigRight)
# print(kpWinProb)
# print(kpLoseProb)

# print(noVigLeft)
# print(noVigRight)