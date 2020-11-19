from urllib.request import urlretrieve as retrieve
from moneyline.moneylineSoccer import gameDate, gameWeek
import csv


stringGameDate = str(gameDate)
stringGameWeek= str(gameWeek)


url2 = 'https://thepredictiontracker.com/nflpredictions.csv'


retrieve(url2,'nfl2.csv')

f2 = open('nfl2.csv', 'r')

reader2 = csv.reader(f2)
next(reader2)

fullList2=[]


#Parse CSV file for sport, teams, and odds for thepredictiontracker

for row2 in reader2:
    fullList2.append([row2[3], row2[2], float(row2[72]), 1-float(row2[72])])



predictionTracker = []

for i in range(len(fullList2)):
    if fullList2[i][0] != fullList2[i-1][0]:
        predictionTracker.append(fullList2[i])



for i in range(len(predictionTracker)):
        if (predictionTracker[i][0] == 'Arizona'):
            predictionTracker[i][0] = 'ARI'

        if (predictionTracker[i][0] == 'Atlanta'):
            predictionTracker[i][0] = 'ATL'

        if (predictionTracker[i][0] == 'Baltimore'):
            predictionTracker[i][0] = 'BAL'

        if (predictionTracker[i][0] == 'Buffalo'):
            predictionTracker[i][0] = 'BUF'

        if (predictionTracker[i][0] == 'Carolina'):
            predictionTracker[i][0] = 'CAR'

        if (predictionTracker[i][0] == 'Chicago'):
            predictionTracker[i][0] = 'CHI'

        if (predictionTracker[i][0] == 'Cincinnati'):
            predictionTracker[i][0] = 'CIN'

        if (predictionTracker[i][0] == 'Cleveland'):
            predictionTracker[i][0] = 'CLE'

        if (predictionTracker[i][0] == 'Dallas'):
            predictionTracker[i][0] = 'DAL'

        if (predictionTracker[i][0] == 'Denver'):
            predictionTracker[i][0] = 'DEN'

        if (predictionTracker[i][0] == 'Detroit'):
            predictionTracker[i][0] = 'DET'

        if (predictionTracker[i][0] == 'Green Bay'):
            predictionTracker[i][0] = 'GB'

        if (predictionTracker[i][0] == 'Houston'):
            predictionTracker[i][0] = 'HOU'

        if (predictionTracker[i][0] == 'Indianapolis'):
            predictionTracker[i][0] = 'IND'

        if (predictionTracker[i][0] == 'Jacksonville'):
            predictionTracker[i][0] = 'JAX'

        if (predictionTracker[i][0] == 'Kansas City'):
            predictionTracker[i][0] = 'KC'

        if (predictionTracker[i][0] == 'LA Chargers'):
            predictionTracker[i][0] = 'LAC'

        if (predictionTracker[i][0] == 'LA Rams'):
            predictionTracker[i][0] = 'LAR'

        if (predictionTracker[i][0] == 'Miami'):
            predictionTracker[i][0] = 'MIA'

        if (predictionTracker[i][0] == 'Minnesota'):
            predictionTracker[i][0] = 'MIN'

        if (predictionTracker[i][0] == 'New England'):
            predictionTracker[i][0] = 'NE'

        if (predictionTracker[i][0] == 'New Orleans'):
            predictionTracker[i][0] = 'NO'

        if (predictionTracker[i][0] == 'N.Y. Giants'):
            predictionTracker[i][0] = 'NYG'

        if (predictionTracker[i][0] == 'N.Y. Jets'):
            predictionTracker[i][0] = 'NYJ'

        if (predictionTracker[i][0] == 'Las Vegas'):
            predictionTracker[i][0] = 'OAK'

        if (predictionTracker[i][0] == 'Philadelphia'):
            predictionTracker[i][0] = 'PHI'

        if (predictionTracker[i][0] == 'Pittsburgh'):
            predictionTracker[i][0] = 'PIT'

        if (predictionTracker[i][0] == 'San Francisco'):
            predictionTracker[i][0] = 'SF'

        if (predictionTracker[i][0] == 'Seattle'):
            predictionTracker[i][0] = 'SEA'

        if (predictionTracker[i][0] == 'Tampa Bay'):
            predictionTracker[i][0] = 'TB'

        if (predictionTracker[i][0] == 'Tennessee'):
            predictionTracker[i][0] = 'TEN'

        if (predictionTracker[i][0] == 'Washington'):
            predictionTracker[i][0] = 'WSH'

        if (predictionTracker[i][1] == 'Arizona'):
            predictionTracker[i][1] = 'ARI'

        if (predictionTracker[i][1] == 'Atlanta'):
            predictionTracker[i][1] = 'ATL'

        if (predictionTracker[i][1] == 'Baltimore'):
            predictionTracker[i][1] = 'BAL'

        if (predictionTracker[i][1] == 'Buffalo'):
            predictionTracker[i][1] = 'BUF'

        if (predictionTracker[i][1] == 'Carolina'):
            predictionTracker[i][1] = 'CAR'

        if (predictionTracker[i][1] == 'Chicago'):
            predictionTracker[i][1] = 'CHI'

        if (predictionTracker[i][1] == 'Cincinnati'):
            predictionTracker[i][1] = 'CIN'

        if (predictionTracker[i][1] == 'Cleveland'):
            predictionTracker[i][1] = 'CLE'

        if (predictionTracker[i][1] == 'Dallas'):
            predictionTracker[i][1] = 'DAL'

        if (predictionTracker[i][1] == 'Denver'):
            predictionTracker[i][1] = 'DEN'

        if (predictionTracker[i][1] == 'Detroit'):
            predictionTracker[i][1] = 'DET'

        if (predictionTracker[i][1] == 'Green Bay'):
            predictionTracker[i][1] = 'GB'

        if (predictionTracker[i][1] == 'Houston'):
            predictionTracker[i][1] = 'HOU'

        if (predictionTracker[i][1] == 'Indianapolis'):
            predictionTracker[i][1] = 'IND'

        if (predictionTracker[i][1] == 'Jacksonville'):
            predictionTracker[i][1] = 'JAX'

        if (predictionTracker[i][1] == 'Kansas City'):
            predictionTracker[i][1] = 'KC'

        if (predictionTracker[i][1] == 'LA Chargers'):
            predictionTracker[i][1] = 'LAC'

        if (predictionTracker[i][1] == 'LA Rams'):
            predictionTracker[i][1] = 'LAR'

        if (predictionTracker[i][1] == 'Miami'):
            predictionTracker[i][1] = 'MIA'

        if (predictionTracker[i][1] == 'Minnesota'):
            predictionTracker[i][1] = 'MIN'

        if (predictionTracker[i][1] == 'New England'):
            predictionTracker[i][1] = 'NE'

        if (predictionTracker[i][1] == 'New Orleans'):
            predictionTracker[i][1] = 'NO'

        if (predictionTracker[i][1] == 'N.Y. Giants'):
            predictionTracker[i][1] = 'NYG'

        if (predictionTracker[i][1] == 'N.Y. Jets'):
            predictionTracker[i][1] = 'NYJ'

        if (predictionTracker[i][1] == 'Las Vegas'):
            predictionTracker[i][1] = 'OAK'

        if (predictionTracker[i][1] == 'Philadelphia'):
            predictionTracker[i][1] = 'PHI'

        if (predictionTracker[i][1] == 'Pittsburgh'):
            predictionTracker[i][1] = 'PIT'

        if (predictionTracker[i][1] == 'San Francisco'):
            predictionTracker[i][1] = 'SF'

        if (predictionTracker[i][1] == 'Seattle'):
            predictionTracker[i][1] = 'SEA'

        if (predictionTracker[i][1] == 'Tampa Bay'):
            predictionTracker[i][1] = 'TB'

        if (predictionTracker[i][1] == 'Tennessee'):
            predictionTracker[i][1] = 'TEN'

        if (predictionTracker[i][1] == 'Washington'):
            predictionTracker[i][1] = 'WSH'
