from modelSoccer import teams, teamsToBet1, team_num_t, potential_winnings, winning_odds, winning_book, break_point
import csv
import pandas as pd
from moneyline.moneylineSoccer import sport, datetime, nowTime, stringGameDate, stringGameDateMDY, stringYesterdayDateMDY

# Removed teams due to injuries

goneTeams= []
goneValues = []
goneOdds = []



# also removes injured teams when betting on draws
if sport[:6] == 'Soccer':
    from transfermarkt import injuredTeams

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
    print(potential_winnings)
    print(winning_book)
    print(winning_odds)


finalTeams = []
finalValues = []
rightNow = []
teamSport = []

def teamOdds(teamsToBet1):
    for i in range(len(teamsToBet1)):
        for key in teamsToBet1[i].keys():
            finalTeams.append(key)
        for value in teamsToBet1[i].values():
            finalValues.append(value)
        for key in teamsToBet1[i].keys():
            rightNow.append(stringGameDate) 
        for key in teamsToBet1[i].keys():
            teamSport.append(sport) 

# teamOdds(teamsToBet1)

# Create CSV file

# f = open("bets.csv", "w")
# writer = csv.DictWriter(
#     f, fieldnames=['Time Script Ran', 'Game Date', 'Sport', 'Team', 'Bet Amount', 'Odds of Winning', 'Potential Winnings with Best Book', 'Expected Value', 'Row_Key', 'Best Book', 'Minimum Odds to Bet'] )
# writer.writeheader()
# f.close()

dfToday = pd.read_csv('bets.csv')

def today_csv(sport, winning_odds, potential_winnings, finalValues, winning_book, break_point):

    # today's upcoming bets
    with open('bets.csv', 'a', newline='') as file:
        for i in range(len(finalTeams)):
            # in order for bet to be recorded, row_key must not already be in bets table
            if (not dfToday['Row_Key'].isin([(stringGameDateMDY + "_" + sport + "_" + finalTeams[i])]).any()):
                writer = csv.writer(file)
                writer.writerow([nowTime, stringGameDateMDY, sport, finalTeams[i], 100, winning_odds[i], winning_book[i], potential_winnings[i], finalValues[i], (stringGameDateMDY + "_" + sport + "_" + finalTeams[i]), break_point[i]])

#or not dfToday['Sport'].isin([teamSport[i]]).any()
# today_csv(sport)

dfToday = pd.read_csv('bets.csv')




# yesterday's results bets - getting some information for what is stored in above table

# Create CSV file

# f = open("betResults.csv", "w")
# writer = csv.DictWriter(
#     f, fieldnames=['Time Script Ran', 'Game Date', 'Sport', 'Team', 'Bet Amount', 'Odds of Winning', 'Potential Winnings with Best Book', 'Expected Value', "Winner", "Bet Winnings", "Row_Key", "Best Book", "Minimum Odds to Bet"])
# writer.writeheader()
# f.close()



# yesterday's results

def yesterdayCSV(yesterdayTeam, sports, playedTeams):
    with open('betResults.csv', 'a', newline='') as file:
        dfResults = pd.read_csv('betResults.csv')
        for i in range(len(dfToday)):
            winnersTable ='No Win'
            betWinnings = -1*(dfToday['Bet Amount'][i])
            for j in range(len(yesterdayTeam)):
                if sport != 'CBB':           
                    if dfToday['Team'][i] == yesterdayTeam[j][9]:
                        winnersTable = dfToday['Team'][i]
                        betWinnings = dfToday['Potential Winnings with Best Book'][i]
                        break

                    if dfToday['Team'][i][-4:] == 'Draw' and dfToday['Team'][i][-4:] == yesterdayTeam[j][9] and (yesterdayTeam[j][3] == dfToday['Team'][i][:-5] or yesterdayTeam[j][2] == dfToday['Team'][i][:-5]):
                        winnersTable = dfToday['Team'][i][-4:]
                        betWinnings = dfToday['Potential Winnings with Best Book'][i]
                        break


                else:
                    if dfToday['Team'][i] == yesterdayTeam[j]:
                        winnersTable = dfToday['Team'][i]
                        betWinnings = dfToday['Potential Winnings with Best Book'][i]
                        break

                    

            # In order for result to be recorded, date(day of game and day of day results are run for) and sport must match and row_key must not be already in results table
            # adds results of games but doesn't add anything if game wasn't played or was canceled 
            
            # print(playedTeams)

            if dfToday['Game Date'][i] == stringYesterdayDateMDY and dfToday['Sport'][i][:3] == sports[:3] and any(item == dfToday['Team'][i] for item in playedTeams) and (not dfResults['Row_Key'].isin([dfToday['Row_Key'][i]]).any()):
                writer = csv.writer(file)
                writer.writerow([dfToday['Time Script Ran'][i], dfToday['Game Date'][i], dfToday['Sport'][i], dfToday['Team'][i], dfToday['Bet Amount'][i], dfToday['Odds of Winning'][i], dfToday['Best Book'][i], dfToday['Potential Winnings with Best Book'][i], dfToday['Expected Value'][i], winnersTable, betWinnings, dfToday['Row_Key'][i], dfToday['Minimum Odds to Bet'][i]])


#dfToday['Sport'][i] == yesterdayTeam[j][1]