from resultsWriter import teamOdds, today_csv, finalTeams, finalValues, yesterdayCSV
import csv
import pandas as pd
from moneyline.moneylineSoccer import sport


if sport == 'NFL':
    from modelNFL import teamstobetNFL, potential_winnings, winning_odds, stringGameDate, FiveThirtyEightGames, FiveThirtyEightGamesYesterday
    winning_odds
    potential_winnings
    FiveThirtyEightGamesYesterday
    teamOdds(teamstobetNFL)
    

elif sport == 'CFB':
    from modelNCAAF import teamsToBetCFB, potential_winnings, winning_odds, stringGameDate, CFB_weekly_games
    winning_odds
    potential_winnings
    teamOdds(teamsToBetCFB)

elif sport == 'CBB':
    from modelCBB import teamsToBetCBB, potential_winnings, winning_odds, stringGameDate
    winning_odds
    potential_winnings
    teamOdds(teamsToBetCBB)
    

else:
    from resultsWriter import potential_winnings, winning_odds, dfToday, teamsToBet1
    from modelSoccer import FiveThirtyEightGamesYesterday
    winning_odds
    potential_winnings
    FiveThirtyEightGamesYesterday
    dfToday
    teamOdds(teamsToBet1)



today_csv(sport, winning_odds, potential_winnings, finalValues)

yesterdayCSV(FiveThirtyEightGamesYesterday, sport)


# why is benefica not getting caught for injuries