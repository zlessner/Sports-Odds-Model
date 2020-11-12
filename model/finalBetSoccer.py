from modelSoccer import teams, teamsToBet1, team_num_t
from transfermarkt import injuredTeams

# Removed teams due to injuries
goneTeams= []

def removeInjuredTeams(team_num_t):
    i=0
    while i < len(team_num_t):
        if any(item == team_num_t[i] for item in injuredTeams):
            goneTeams.append(teamsToBet1[i])

        i+=1

    
    # Remove injured teams that match up with teams to bet on

    for j in teamsToBet1[:]:
      if j in goneTeams:
          teamsToBet1.remove(j)
    


removeInjuredTeams(team_num_t)


print(teamsToBet1)
