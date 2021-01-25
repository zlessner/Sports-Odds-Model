from resultsWriter import teamOdds, today_csv, finalTeams, finalValues, yesterdayCSV
import csv
import pandas as pd
from moneyline.moneylineSoccer import sport, stringGameDate


if sport == 'NFL':
    from modelNFL import teamstobetNFL, potential_winnings, winning_odds, FiveThirtyEightGames, FiveThirtyEightGamesYesterday, playedTeams, winning_book, break_point
    teamOdds(teamstobetNFL)
    

elif sport == 'CFB':
    from modelNCAAF import teamsToBetCFB, potential_winnings, winning_odds, CFB_weekly_games, winning_book
    teamOdds(teamsToBetCFB)

elif sport == 'NBA':
    from modelNBA import teamsToBetNBA, potential_winnings, winning_odds, FiveThirtyEightGamesYesterday, playedTeams, winning_book, break_point
    teamOdds(teamsToBetNBA)

elif sport == 'CBB':
    from modelCBB import teamsToBetCBB, potential_winnings, winning_odds, FiveThirtyEightGamesYesterday, playedTeams, winning_book, break_point
    teamOdds(teamsToBetCBB)

elif sport == 'BEL':
    from modelEuroLeague import teamsToBetBEL, potential_winnings, winning_odds, winning_book, break_point
    teamOdds(teamsToBetBEL)

elif sport == 'NHL':
    from modelNHL import teamsToBetNHL, potential_winnings, winning_odds, winning_book, break_point
    teamOdds(teamsToBetNHL)
    

else:
    from resultsWriter import potential_winnings, winning_odds, dfToday, teamsToBet1, winning_book, break_point
    from modelSoccer import FiveThirtyEightGamesYesterday, playedTeams, winnerTeams
    teamOdds(teamsToBet1)



today_csv(sport, winning_odds, potential_winnings, finalValues, winning_book, break_point)

yesterdayCSV(FiveThirtyEightGamesYesterday, sport, playedTeams)

# run just soccer for sport on days where not many games - only gives back 7 results but coudl be quicker than going through every individual league

# append results tables to each other so only have to run teh results table once across all sports

# Add column to both tables with break point where bet would be over min expected value (right now it is EV of 7) and that's what you'd tell client ot bet if they can get moneyline over that value

# print(winnerTeams)