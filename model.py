from urllib.request import urlretrieve as retrieve
from moneyline import theOddsAPIGames
import csv
import datetime


today = datetime.date.today()
tomorrow = today + datetime.timedelta(1)
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
    if game[0] == stringToday:
        FiveThirtyEightGames.append(game)

# print(FiveThirtyEightGames, "\n")

# for odds in FiveThirtyEightGames:
#     if (odds[4]>.5):
#         print(odds[2])

eventsAPI = {}

for i in range(len(theOddsAPIGames)):
    for j in range(len(theOddsAPIGames[i]['sites'])):
        eventsAPI[i] = [theOddsAPIGames[i]['sport_key']], [theOddsAPIGames[i]['teams']], [theOddsAPIGames[i]['sites'][j]['odds']]
        break

# print(eventsAPI[1][1][0][1])

HomeAPI=[]
AwayAPI=[]

for i in eventsAPI:
        HomeAPI.append(eventsAPI[i][1][0][1])
        AwayAPI.append(eventsAPI[i][1][0][0])

print(HomeAPI)
print(AwayAPI)
# print (range(len(HomeAPI)))
# print(FiveThirtyEightGames[0][2])
# print(FiveThirtyEightGames[0][3])

# for i in range(len(HomeAPI)):
#     for j in range(len(FiveThirtyEightGames)):
#         # print (FiveThirtyEightGames[j][2])
#         # if HomeAPI[i] == FiveThirtyEightGames[j][2]:
#         #     print (HomeAPI[i])
#         #     break
#         if AwayAPI[i] == FiveThirtyEightGames[j][3]:
#             print (AwayAPI[i])
#             break
    
#alphabeitical ordering per group and odds
#use soccer sport codes epl etc. to combine all the ganes