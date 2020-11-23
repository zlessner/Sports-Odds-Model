from resultsWriter import teamOdds, today_csv, teamsToBet1, finalTeams, finalValues, yesterdayCSV
import csv
import pandas as pd
from moneyline.moneylineSoccer import sport

# Comment sport out if soccer

sport = 'NFL'

if sport == 'NFL':
    from modelNFL import teamstobetNFL, potential_winnings, winning_odds, stringGameDate, FiveThirtyEightGames, FiveThirtyEightGamesYesterday
    winning_odds
    potential_winnings
    FiveThirtyEightGamesYesterday

elif sport == 'CFB':
    from modelNCAAF import teamsToBetCFB, potential_winnings, winning_odds, stringGameDate, CFB_weekly_games
    winning_odds
    potential_winnings

else:
    from resultsWriter import potential_winnings, winning_odds, dfToday
    from modelSoccer import FiveThirtyEightGamesYesterday
    winning_odds
    potential_winnings
    FiveThirtyEightGamesYesterday
    dfToday





# change this to particular sport to use

teamOdds(teamstobetNFL)




today_csv(sport, winning_odds, potential_winnings, finalValues)

yesterdayCSV(FiveThirtyEightGamesYesterday, sport)


