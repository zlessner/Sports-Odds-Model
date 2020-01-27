from urllib.request import urlretrieve as retrieve
from moneyline import workingGames
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

todayGames=[]

for game in fullList:
    if game[0] == stringToday:
        todayGames.append(game)

# print(todayGames, "\n")

# for odds in todayGames:
#     if (odds[4]>.5):
#         print(odds[2])

events = {}
# team=[]
# odds=[]

for i in range(len(workingGames)):
    for j in range(len(workingGames[i]['sites'])):
        events[i] = [workingGames[i]['sport_nice']], [workingGames[i]['teams']], [workingGames[i]['sites'][j]['odds']]
        break


# print(events[1][1][0][1])

team1=[]
team2=[]

for i in events:
        team1.append(events[i][1][0][1])
        team2.append(events[i][1][0][0])

print(team1)
print(team2)

for i in range(len(team1)):
    for j in range(len(todayGames)):
        # print (todayGames[j])
        if team1[i] == todayGames[j][2]:
            print (team1[i])
        if team2[i] == todayGames[j][2]:
            print (team2[i])
    