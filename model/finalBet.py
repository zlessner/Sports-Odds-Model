from resultsWriter import teamOdds, today_csv, finalTeams, finalValues, yesterdayCSV
import csv
import pandas as pd
from moneyline.moneylineSoccer import sport, stringGameDate


if sport == 'NFL':
    from modelNFL import teamstobetNFL, potential_winnings, winning_odds, FiveThirtyEightGames, FiveThirtyEightGamesYesterday, playedTeams
    teamOdds(teamstobetNFL)
    

elif sport == 'CFB':
    from modelNCAAF import teamsToBetCFB, potential_winnings, winning_odds, CFB_weekly_games
    teamOdds(teamsToBetCFB)

elif sport == 'NBA':
    from modelNBA import teamsToBetNBA, potential_winnings, winning_odds, FiveThirtyEightGamesYesterday, playedTeams
    teamOdds(teamsToBetNBA)

elif sport == 'CBB':
    from modelCBB import teamsToBetCBB, potential_winnings, winning_odds, FiveThirtyEightGamesYesterday, playedTeams
    teamOdds(teamsToBetCBB)
    

else:
    from resultsWriter import potential_winnings, winning_odds, dfToday, teamsToBet1
    from modelSoccer import FiveThirtyEightGamesYesterday, playedTeams, winnerTeams
    teamOdds(teamsToBet1)



today_csv(sport, winning_odds, potential_winnings, finalValues)

yesterdayCSV(FiveThirtyEightGamesYesterday, sport, playedTeams)

# run just soccer for sport on days where not many games - only gives back 7 results but coudl be quicker than going through every individual league

# append results tables to each other so only have to run teh results table once across all sports

# Add column to both tables with break point where bet would be over min expected value (right now it is EV of 7) and that's what you'd tell client ot bet if they can get moneyline over that value

# print(winnerTeams)