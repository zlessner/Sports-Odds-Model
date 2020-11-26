from resultsWriter import teamOdds, today_csv, finalTeams, finalValues, yesterdayCSV
import csv
import pandas as pd
from moneyline.moneylineSoccer import sport

# Comment sport out if soccer
# sport


# sport = 'CBB'

if sport == 'NFL':
    from modelNFL import teamstobetNFL, potential_winnings, winning_odds, stringGameDate, FiveThirtyEightGames, FiveThirtyEightGamesYesterday
    soccer = False
    winning_odds
    potential_winnings
    FiveThirtyEightGamesYesterday
    teamOdds(teamstobetNFL)
    

elif sport == 'CFB':
    from modelNCAAF import teamsToBetCFB, potential_winnings, winning_odds, stringGameDate, CFB_weekly_games
    soccer = False
    winning_odds
    potential_winnings
    teamOdds(teamsToBetCFB)

elif sport == 'CBB':
    from modelCBB import teamsToBetCBB, potential_winnings, winning_odds, stringGameDate
    soccer = False
    winning_odds
    potential_winnings
    teamOdds(teamsToBetCBB)
    

else:
    from resultsWriter import potential_winnings, winning_odds, dfToday, teamsToBet1
    from modelSoccer import FiveThirtyEightGamesYesterday
    soccer = True
    winning_odds
    potential_winnings
    FiveThirtyEightGamesYesterday
    dfToday
    teamOdds(teamsToBet1)



today_csv(sport, winning_odds, potential_winnings, finalValues)

# yesterdayCSV(FiveThirtyEightGamesYesterday, sport)

# isolate running transfermarkt to just soccer python runs - and then solve the bad handshake problem

# why is benefica not getting caught for injuries