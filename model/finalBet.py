from resultsWriter import teamOdds, today_csv, teamsToBet1, finalTeams, finalValues, potential_winnings, winning_odds
import csv
import pandas as pd
from moneyline.moneylineSoccer import sport

# Comment this out if soccer

# sport = 'NFL'

# if sport == 'NFL':
#     from modelNFL import teamstobetNFL, potential_winnings, winning_odds, stringGameDate, FiveThirtyEightGames
#     winning_odds
#     potential_winnings



# Comment this out if NFL

winning_odds
potential_winnings


# change this to particular sport to use

teamOdds(teamsToBet1)


today_csv(sport, winning_odds, potential_winnings, finalValues)


