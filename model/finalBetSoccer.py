from modelSoccer import teams, teamsToBet1, team_num_t, FiveThirtyEightGamesYesterday, potential_winnings
from transfermarkt import injuredTeams
import csv
import pandas as pd
from moneyline.moneylineSoccer import gameDate, futureGame, yesterdayGame, sport

# Removed teams due to injuries
goneTeams= []
goneValues = []

print(teamsToBet1)

def removeInjuredTeams(team_num_t):
    i=0
    while i < len(team_num_t):
        if any(item == team_num_t[i] for item in injuredTeams):
            goneTeams.append(teamsToBet1[i])
            goneValues.append(potential_winnings[i])

        i+=1

    
    # Remove injured teams that match up with teams to bet on

    for j in teamsToBet1[:]:
      if j in goneTeams:
          teamsToBet1.remove(j)

    for j in potential_winnings[:]:
      if j in goneValues:
          potential_winnings.remove(j)
    


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

f = open("bets.csv", "w")
writer = csv.DictWriter(
    f, fieldnames=['Date', 'Sport', 'Team', 'Bet Amount', 'Expected Value', "Winner", "Bet Winnings"] )
writer.writeheader()
f.close()


leagueGames = []

for i in range(len(FiveThirtyEightGamesYesterday)):
    if FiveThirtyEightGamesYesterday[i][1] == sport:
        leagueGames.append(FiveThirtyEightGamesYesterday[i])




with open('bets.csv', 'a', newline='') as file:
    i=0
    while i < len(finalTeams):
        winnersTable ='No Win'
        betWinnings = -100
        for j in range(len(leagueGames)):
            if finalTeams[i] == leagueGames[j][9]:
                winnersTable = finalTeams[i]
                betWinnings = potential_winnings[i]

        # if winnersTable == finalTeams[i]:
        #     betWinnings = 

        writer = csv.writer(file)
        writer.writerow([futureGame, sport, finalTeams[i], 100, finalValues[i], winnersTable, betWinnings])
        i+=1


print(potential_winnings)

# print(leagueGames)

# winnersTable=[]

# for i in range(len(finalTeams)):
#     for j in range(len(leagueGames)):
#         if finalTeams[i] == leagueGames[j][9]:
#             winnersTable.append(finalTeams[i])

# print(winnersTable)



# finalTeamNames=[]
# for i in range(len(finalTeams)):
#     finalTeamNames.append(finalTeams[i][-4:])

# print(finalTeamNames)


# for i in range(len(finalTeams)):
#     if finalTeamNames[i] == 'away':
#         for j in range(len(leagueGames)):
#             if leagueGames[j][2] == finalTeams[i][:-5]:
#                 print(leagueGames[j][7])
#     if finalTeamNames[i][-4:] == 'home':
#         for j in range(len(leagueGames)):
#             if leagueGames[j][3] == finalTeams[i][:-5]:
#                 print(leagueGames[j][8])
            





# i=0
# while i < len(team_num_t):
#     if any(item == team_num_t[i] for item in injuredTeams):
#         goneTeams.append(teamsToBet1[i])

#     i+=1





    # g = open('bets.csv', 'r')
    # reader = csv.reader(g)
    # for row in reader:
    #     if reader[row][0] == yesterdayGame:




    # mylist = list(reader)
    # g.close()
    # if myList
    # mylist[1][3] = 'X'
    # my_new_list = open('mylist.csv', 'w', newline = '')
    # csv_writer = csv.writer(my_new_list)
    # csv_writer.writerows(mylist)
    # my_new_list.close()
