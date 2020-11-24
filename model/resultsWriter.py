from modelSoccer import teams, teamsToBet1, team_num_t, potential_winnings, winning_odds, stringGameDate, stringYesterdayDate
from transfermarkt import injuredTeams
import csv
import pandas as pd
from moneyline.moneylineSoccer import gameDate, sport, datetime, yesterdayGame

# Removed teams due to injuries

codeTime = datetime.datetime.now()

goneTeams= []
goneValues = []
goneOdds = []

print(teamsToBet1)

# also removes injured teams when betting on draws

def removeInjuredTeams(team_num_t):
    i=0
    while i < len(team_num_t):
        if any(item == team_num_t[i] for item in injuredTeams) or filter(lambda item: any(x in item for x in injuredTeams), teamsToBet1[:]):
            goneTeams.append(teamsToBet1[i])
            goneValues.append(potential_winnings[i])
            goneOdds.append(winning_odds[i])

        i+=1

# might be appending wrong teams into goneTeams - ones that come after the draw because teamsToBet1 and teamNumt are different lengths - check in morning
# or leipzig shouldn't be included in this group because they are the last element on list

    # Remove injured teams that match up with teams to bet on

    for j in teamsToBet1[:]:
      if j in goneTeams:
          teamsToBet1.remove(j)
          goneTeams.remove(j)

    for j in potential_winnings[:]:
      if j in goneValues:
          potential_winnings.remove(j)
          goneValues.remove(j)

    for j in winning_odds[:]:
      if j in goneOdds:
          winning_odds.remove(j)
          goneOdds.remove(j)
          

removeInjuredTeams(team_num_t)



print(teamsToBet1)

finalTeams = []
finalValues = []

def teamOdds(teamsToBet1):
    for i in range(len(teamsToBet1)):
        for key in teamsToBet1[i].keys():
            finalTeams.append(key)
        for value in teamsToBet1[i].values():
            finalValues.append(value)

# teamOdds(teamsToBet1)

# Create CSV file

# f = open("bets.csv", "w")
# writer = csv.DictWriter(
#     f, fieldnames=['Time Script Ran', 'Game Date', 'Sport', 'Team', 'Bet Amount', 'Odds of Winning', 'Potential Winnings', 'Expected Value'] )
# writer.writeheader()
# f.close()



def today_csv(sport, winning_odds, potential_winnings, finalValues):

    # today's upcoming bets
    with open('bets.csv', 'a', newline='') as file:
        i=0
        while i < len(finalTeams):
            writer = csv.writer(file)
            writer.writerow([codeTime, stringGameDate, sport, finalTeams[i], 100, winning_odds[i], potential_winnings[i], finalValues[i]])
            i+=1


# today_csv(sport)

dfToday = pd.read_csv('bets.csv')




# yesterday's results bets - getting some information for what is stored in above table

# Create CSV file

# f = open("betResults.csv", "w")
# writer = csv.DictWriter(
#     f, fieldnames=['Time Script Ran', 'Game Date', 'Sport', 'Team', 'Bet Amount', 'Odds of Winning', 'Potential Winnings', 'Expected Value', "Winner", "Bet Winnings"])
# writer.writeheader()
# f.close()



# yesterday's results

def yesterdayCSV(yesterdayTeam, sports):
    with open('betResults.csv', 'a', newline='') as file:

        for i in range(len(dfToday)):
            winnersTable ='No Win'
            betWinnings = -100
            for j in range(len(yesterdayTeam)):
                if dfToday['Team'][i] == yesterdayTeam[j][9]:
                    winnersTable = dfToday['Team'][i]
                    betWinnings = dfToday['Potential Winnings'][i]

                if dfToday['Team'][i][-4:] == 'Draw' and dfToday['Team'][i][-4:] == yesterdayTeam[j][9]:
                    winnersTable = dfToday['Team'][i][-4:]
                    betWinnings = dfToday['Potential Winnings'][i]
       
            if dfToday['Game Date'][i] == stringYesterdayDate and dfToday['Sport'][i][:3] == sports[:3]:
                writer = csv.writer(file)
                writer.writerow([dfToday['Time Script Ran'][i], stringYesterdayDate, dfToday['Sport'][i], dfToday['Team'][i], dfToday['Bet Amount'][i], dfToday['Odds of Winning'][i], dfToday['Potential Winnings'][i], dfToday['Expected Value'][i], winnersTable, betWinnings])
            







# print(leagueGames)



