from urllib.request import urlretrieve as retrieve
from moneyline import theOddsAPIGames, today, tomorrow
import csv
import time
# import datetime
from datetime import datetime


stringToday = str(today)
stringTomorrow = str(tomorrow)

url = 'https://projects.fivethirtyeight.com/soccer-api/club/spi_matches.csv'

retrieve(url,'soccer.csv')

f = open('soccer.csv', 'r')

reader = csv.reader(f)
next(reader)

fullList=[]

for row in reader:
        fullList.append([row[0], row[2], row[3], row[4], float(row[7]),float(row[8]),float(row[9])])

FiveThirtyEightGames=[]

for game in fullList:
    if game[0] == stringTomorrow:
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

AlphaAPI=[]
BetaAPI=[]
AllTeamsAPI=[]

for i in eventsAPI:
    if (datetime.utcfromtimestamp(eventsAPI[i][1][0]).strftime('%Y-%m-%d') == stringTomorrow):
        AlphaAPI.append(eventsAPI[i][2][0][0])
        BetaAPI.append(eventsAPI[i][2][0][1])
        AllTeamsAPI.append(eventsAPI[i][2][0])

# print(AlphaAPI)
# print(BetaAPI)

# print(AllTeamsAPI)

# # print (range(len(AlphaAPI)))
# print(FiveThirtyEightGames)
# print(FiveThirtyEightGames[0][3])

for i in range(len(AlphaAPI)):
    for j in range(len(FiveThirtyEightGames)):
        if AlphaAPI[i][:5] == FiveThirtyEightGames[j][2][:5]:
            print (AlphaAPI[i],
             int((((eventsAPI[i][3][0]['h2h'][0])-1)*100)*(float(FiveThirtyEightGames[j][4]))-(100*(1-(float(FiveThirtyEightGames[j][4]))))))
            
        if BetaAPI[i][:5] == FiveThirtyEightGames[j][3][:5]:
            print (BetaAPI[i], int((((eventsAPI[i][3][0]['h2h'][1])-1)*100)*(float(FiveThirtyEightGames[j][5]))-(100*(1-(float(FiveThirtyEightGames[j][5]))))))
            
        if AlphaAPI[i][:5] == FiveThirtyEightGames[j][3][:5]:
            print (AlphaAPI[i], int((((eventsAPI[i][3][0]['h2h'][0])-1)*100)*(float(FiveThirtyEightGames[j][5]))-(100*(1-(float(FiveThirtyEightGames[j][5]))))))
            
        if BetaAPI[i][:5] == FiveThirtyEightGames[j][2][:5]:
            print (BetaAPI[i], int((((eventsAPI[i][3][0]['h2h'][1])-1)*100)*(float(FiveThirtyEightGames[j][4]))-(100*(1-(float(FiveThirtyEightGames[j][4]))))))
            
    


#alphabeitical ordering per group and odds
#use soccer sport codes epl etc. to combine all the ganes
#home team option for sorting? Not sure if there's an away team field
#Because same name is used for multiple teams, teams may repeat twice - see what happens for Man City Man U
#add in draw option