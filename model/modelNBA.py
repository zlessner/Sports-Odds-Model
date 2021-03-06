from urllib.request import urlretrieve as retrieve
from moneyline.moneylineNBA import theOddsAPIGames
from moneyline.moneylineSoccer import stringGameDate, stringYesterdayDate 
import csv
import time
from datetime import datetime


url = 'https://projects.fivethirtyeight.com/nba-model/nba_elo_latest.csv'

retrieve(url,'nba.csv')

f = open('nba.csv', 'r')

reader = csv.reader(f)
next(reader)

fullList=[]

#Parse CSV file for sport, teams, and odds

# Eventually bring in thepredictiontracker once season starts

for row in reader:
        fullList.append([row[0], row[4], row[5], float(row[20]),float(row[21]), row[6], row[7], row[22], row[23], row[8]])

FiveThirtyEightGames=[]

for game in fullList:
    if game[0] == stringGameDate:
        FiveThirtyEightGames.append(game)


FiveThirtyEightGamesYesterday=[]
playedTeams = []

for game in fullList:
    if game[0] == stringYesterdayDate:
        FiveThirtyEightGamesYesterday.append(game)





for i in range(len(FiveThirtyEightGamesYesterday)):
    if len(FiveThirtyEightGamesYesterday[i][7])>0:
        FiveThirtyEightGamesYesterday[i][7] = float(FiveThirtyEightGamesYesterday[i][7])
        playedTeams.append(FiveThirtyEightGamesYesterday[i][1])
        playedTeams.append(FiveThirtyEightGamesYesterday[i][2])

    if len(FiveThirtyEightGamesYesterday[i][8])>0:
        FiveThirtyEightGamesYesterday[i][8] = float(FiveThirtyEightGamesYesterday[i][8])


for i in range(len(FiveThirtyEightGamesYesterday)):

    if FiveThirtyEightGamesYesterday[i][7] > FiveThirtyEightGamesYesterday[i][8]:
        FiveThirtyEightGamesYesterday[i][9] = FiveThirtyEightGamesYesterday[i][1]

    elif FiveThirtyEightGamesYesterday[i][7] < FiveThirtyEightGamesYesterday[i][8]:
        FiveThirtyEightGamesYesterday[i][9] = FiveThirtyEightGamesYesterday[i][2]



# Parse Sports Betting API for sport, game time, teams, and odds

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
        
            for j in range(len(theOddsAPIGames[i]['sites'])):

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


AlphaAPI=[]
BetaAPI=[]

#Adding Home team to AlphaAPI, Away team to BetaAPI, Home teams odds to OddsA, and Away team odds to OddsB

for i in eventsAPI:
    # if (datetime.utcfromtimestamp((eventsAPI[i][1][0])-30000).strftime('%Y-%m-%d') == stringGameDate):
    if eventsAPI[i][2][0][1] == eventsAPI[i][5][0]:
        AlphaAPI.append(eventsAPI[i][2][0][1])
        BetaAPI.append(eventsAPI[i][2][0][0])
    else:
        BetaAPI.append(eventsAPI[i][2][0][1])
        AlphaAPI.append(eventsAPI[i][2][0][0])


#Matching up 538 teams with sports betting API teams
#Performing calculations to see if expected value of winnings on a $100 dollar bet is over $10 (10% return)

discrepancy = []

for i in range(len(FiveThirtyEightGames)):
        for k in range(len(AlphaAPI)):
            if FiveThirtyEightGames[i][1].lower() == AlphaAPI[k].lower():
                if abs((FiveThirtyEightGames[i][3]-homeNoVig[k])/homeNoVig[k]) > .25 or abs((FiveThirtyEightGames[i][3]-homeNoVig[k])/FiveThirtyEightGames[i][3]) > .25:
                    # print(FiveThirtyEightGames[i][3])
                    # print(homeNoVig[k])
                    discrepancy.append(FiveThirtyEightGames[i][1] + " discrepancy")
                FiveThirtyEightGames[i][3] = float(FiveThirtyEightGames[i][3]*.75+homeNoVig[k]*.25)
            if FiveThirtyEightGames[i][2].lower() == BetaAPI[k].lower():
                if abs((FiveThirtyEightGames[i][4]-awayNoVig[k])/awayNoVig[k]) > .25 or abs((FiveThirtyEightGames[i][4]-awayNoVig[k])/FiveThirtyEightGames[i][4]) > .25:
                    # print(FiveThirtyEightGames[i][4])
                    # print(awayNoVig[k])
                    discrepancy.append(FiveThirtyEightGames[i][2] + " discrepancy")
                FiveThirtyEightGames[i][4] = float(FiveThirtyEightGames[i][4]*.75+awayNoVig[k]*.25)


teamsToBetNBA=[]
potential_winnings=[]
winning_odds=[]
winning_book=[]
break_point = []

# setting rules for reccomended bet if not best book

for i in range(len(AlphaAPI)):
    for j in range(len(FiveThirtyEightGames)):
        try:
            if (AlphaAPI[i]).lower() == (FiveThirtyEightGames[j][1].lower()):
                HomeAlphaOdds = int((((Away[i])-1)*100)*(float(FiveThirtyEightGames[j][3]))-(100*(1-(float(FiveThirtyEightGames[j][3])))))
                if (HomeAlphaOdds>7):
                    for n in range(len(discrepancy)):
                        if discrepancy[n].rsplit(' ', 1)[0] == AlphaAPI[i]:
                            print(discrepancy[n])
                    if round((107/float(FiveThirtyEightGames[j][3]))-100) >= .95*int(((Away[i])-1)*100):
                        break_point.append(round((107/float(FiveThirtyEightGames[j][3]))-100))
                    else:
                        break_point.append(round(.95*int(((Away[i])-1)*100)))
                    # break_point.append(round((107/float(FiveThirtyEightGames[j][3]))-100))
                    teamsToBetNBA.append({AlphaAPI[i]: HomeAlphaOdds})
                    potential_winnings.append(int(((Away[i])-1)*100))
                    winning_odds.append(float(FiveThirtyEightGames[j][3]))
                    winning_book.append(bookAway[i])
        except KeyError:
            continue

        try:    
            if (BetaAPI[i]).lower() == (FiveThirtyEightGames[j][2].lower()):
                AwayBetaOdds = int((((Home[i])-1)*100)*(float(FiveThirtyEightGames[j][4]))-(100*(1-(float(FiveThirtyEightGames[j][4])))))
                if (AwayBetaOdds>7):
                    for n in range(len(discrepancy)):
                        if discrepancy[n].rsplit(' ', 1)[0] == BetaAPI[i]:
                            print(discrepancy[n])
                    # break_point.append(round((107/float(FiveThirtyEightGames[j][4]))-100))
                    if round((107/float(FiveThirtyEightGames[j][4]))-100) >= .95*int(((Home[i])-1)*100):
                        break_point.append(round((107/float(FiveThirtyEightGames[j][4]))-100))
                    else:
                        break_point.append(round(.95*int(((Home[i])-1)*100)))
                    teamsToBetNBA.append({BetaAPI[i]: AwayBetaOdds})
                    potential_winnings.append(int(((Home[i])-1)*100))
                    winning_odds.append(float(FiveThirtyEightGames[j][4]))
                    winning_book.append(bookHome[i])
        except KeyError:
            continue


 #Comment the below in if just want results for this one model   

print(teamsToBetNBA)

print(potential_winnings)
print(winning_book)
print(winning_odds)
print(len(AlphaAPI))
print(len(bookHome))
