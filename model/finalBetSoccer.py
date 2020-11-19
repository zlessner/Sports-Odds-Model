from modelSoccer import teams, teamsToBet1, team_num_t, FiveThirtyEightGamesYesterday, potential_winnings, winning_odds, stringGameDate, stringYesterdayDate, FiveThirtyEightGames
from transfermarkt import injuredTeams
import csv
import pandas as pd
from moneyline.moneylineSoccer import gameDate, sport

# Removed teams due to injuries
goneTeams= []
goneValues = []
goneOdds = []

print(teamsToBet1)



def removeInjuredTeams(team_num_t):
    i=0
    while i < len(team_num_t):
        if any(item == team_num_t[i] for item in injuredTeams):
            goneTeams.append(teamsToBet1[i])
            goneValues.append(potential_winnings[i])
            goneOdds.append(winning_odds[i])

        i+=1

    
    # Remove injured teams that match up with teams to bet on

    for j in teamsToBet1[:]:
      if j in goneTeams:
          teamsToBet1.remove(j)

    for j in potential_winnings[:]:
      if j in goneValues:
          potential_winnings.remove(j)

    for j in winning_odds[:]:
      if j in goneOdds:
          winning_odds.remove(j)
    


removeInjuredTeams(team_num_t)


print(teamsToBet1)


finalTeams = []
finalValues = []

for i in range(len(teamsToBet1)):
    for key in teamsToBet1[i].keys():
        finalTeams.append(key)
    for value in teamsToBet1[i].values():
        finalValues.append(value)


# Create CSV file

# f = open("bets.csv", "w")
# writer = csv.DictWriter(
#     f, fieldnames=['Date', 'Sport', 'Team', 'Bet Amount', 'Odds of Winning', 'Potential Winnings', 'Expected Value'] )
# writer.writeheader()
# f.close()


# leagueGamesToday = []

# for i in range(len(FiveThirtyEightGames)):
#     if FiveThirtyEightGames[i][1] == sport:
#         leagueGamesToday.append(FiveThirtyEightGames[i])



# # today's upcoming bets
# with open('bets.csv', 'a', newline='') as file:
#     i=0
#     while i < len(finalTeams):
#         oddsWinning = ''
#         for j in range(len(leagueGamesToday)):
#             if finalTeams[i] == leagueGamesToday[j][9]:
#                 oddsWinning = winning_odds[i]


#         writer = csv.writer(file)
#         writer.writerow([stringGameDate, sport, finalTeams[i], 100, winning_odds[i], potential_winnings[i], finalValues[i]])
#         i+=1


dfToday = pd.read_csv('bets.csv')


print(winning_odds)
# print(dfToday['Date'][0])




# yesterday's results bets - getting some information for what is stored in above table

# Create CSV file

# f = open("betResults.csv", "w")
# writer = csv.DictWriter(
#     f, fieldnames=['Date', 'Sport', 'Team', 'Bet Amount', 'Odds of Winning', 'Potential Winnings', 'Expected Value', "Winner", "Bet Winnings"])
# writer.writeheader()
# f.close()


leagueGames = []

for i in range(len(FiveThirtyEightGamesYesterday)):
    if FiveThirtyEightGamesYesterday[i][1] == sport:
        leagueGames.append(FiveThirtyEightGamesYesterday[i])



# yesterday's results
with open('betResults.csv', 'a', newline='') as file:

    for i in range(len(dfToday)):
        winnersTable ='No Win'
        betWinnings = -100
        for j in range(len(leagueGames)):
            if dfToday['Team'][i] == leagueGames[j][9]:
                winnersTable = dfToday['Team'][i]
                betWinnings = dfToday['Potential Winnings'][i]
        if dfToday['Date'][i] == stringYesterdayDate:
            writer = csv.writer(file)
            writer.writerow([stringYesterdayDate, dfToday['Sport'][i], dfToday['Team'][i], dfToday['Bet Amount'][i], dfToday['Odds of Winning'][i], dfToday['Potential Winnings'][i], dfToday['Expected Value'][i], winnersTable, betWinnings])
        







# print(leagueGames)



