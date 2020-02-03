from moneylineCBB import theOddsAPIGames, today, tomorrow
import time
from datetime import datetime
from kenpompy.utils import login
from FanMatch import FanMatch


stringToday = str(today)
stringTomorrow = str(tomorrow)


browser = login('testudotimes@gmail.com', 'lenbi@s34')
fm = FanMatch(browser, date = stringToday)


# print (fm.fm_df['PredictedWinner'], fm.fm_df['PredictedLoser'], fm.fm_df['WinProbability'])

# print (float(fm.fm_df['WinProbability'][1][:2]))

# print (range(len(fm.fm_df['PredictedWinner'])))

# fullList = []

# for i in range(len(fm.fm_df['PredictedWinner'])):
#         fullList.append(fm.fm_df['PredictedWinner'], fm.fm_df['PredictedLoser'], fm.fm_df['WinProbability'])

# print (fullList)



eventsAPI = {}

for i in range(len(theOddsAPIGames)):
    for j in range(len(theOddsAPIGames[i]['sites'])):
        eventsAPI[i] = [theOddsAPIGames[i]['sport_key']], [theOddsAPIGames[i]['commence_time']], [theOddsAPIGames[i]['teams']], [theOddsAPIGames[i]['sites'][j]['odds']]
        break


AlphaAPIx=[]
BetaAPIx=[]
AlphaAPI=[]
BetaAPI=[]

#Can change date



for i in eventsAPI:
    if (datetime.utcfromtimestamp((eventsAPI[i][1][0]-30000)).strftime('%Y-%m-%d') == stringToday):
        AlphaAPIx.append(eventsAPI[i][2][0][0].rsplit(' ', 1)[0])
        BetaAPIx.append(eventsAPI[i][2][0][1].rsplit(' ', 1)[0])
        
for i in range(len(AlphaAPIx)):
    AlphaAPI.append(AlphaAPIx[i].replace(' Tar', '').replace(' Bald', '').replace(' Bananna', '').replace(' Big', '').replace(' Black', '').replace(' Blue', '').replace(' Great', '').replace(' River', '').replace(' Green', '').replace(' Golden', '').replace(' Yellow', '').replace(' Fighting', '').replace(' Demon', '').replace(' Red', '').replace(" Runnin'", '').replace(' Nittany', '').replace(' Scarlet', '').replace(' Horned', '').replace(' Rainbow', '').replace(" Fightin'", '').replace(' Thundering', '').replace(' Mean', '').replace(' Purple', '').replace(' Wolf', '').replace(' Mountain', '').replace(' Crimson', '').replace(' Delta', '').replace(' Fighting', '').replace(" Ragin'", '').replace("-", '').replace("Miss", 'Mississippi'))
    BetaAPI.append(BetaAPIx[i].replace(' Tar', '').replace(' Bald', '').replace(' Bananna', '').replace(' Big', '').replace(' Black', '').replace(' Blue', '').replace(' Great', '').replace(' River', '').replace(' Green', '').replace(' Golden', '').replace(' Yellow', '').replace(' Fighting', '').replace(' Demon', '').replace(' Red', '').replace(" Runnin'", '').replace(' Nittany', '').replace(' Scarlet', '').replace(' Horned', '').replace(' Rainbow', '').replace(" Fightin'", '').replace(' Thundering', '').replace(' Mean', '').replace(' Purple', '').replace(' Wolf', '').replace(' Mountain', '').replace(' Crimson', '').replace(' Delta', '').replace(' Fighting', '').replace(" Ragin'", '').replace("-", '').replace("Miss", 'Mississippi'))

# # print (range(len(AlphaAPI)))
# print(FiveThirtyEightGames)
# print(FiveThirtyEightGames[0][3])

#Adding teams to bet on
teamsToBetCBB=[]
# print ((AlphaAPI))
# print(eventsAPI)


kpWinnersProjx=[]
kpLosersProjx=[]
kpWinProb=[]

kpWinnersProj=[]
kpLosersProj=[]

for i in range(len(fm.fm_df['PredictedWinner'])):
    kpWinnersProjx.append(fm.fm_df['PredictedWinner'][i])
    kpLosersProjx.append(fm.fm_df['PredictedLoser'][i])
    kpWinProb.append(float(fm.fm_df['WinProbability'][i][:2])/100)


for i in range(len(kpWinnersProjx)):
    kpWinnersProj.append(kpWinnersProjx[i].replace('.', ''))
    kpLosersProj.append(kpLosersProjx[i].replace('.', ''))



# print(kpWinnersProj)
# print(kpLosersProj)
# print(kpWinProb)

# print(TeamsAPI)
# print("break")
# print(kpWinnersProj)
# print(kpLosersProj)


# print(int((((eventsAPI[4][3][0]['h2h'][0])-1)*100)))

for i in range(len(AlphaAPI)):
    for j in range(len(kpWinnersProj)):
    # print(fm.fm_df['PredictedWinner'][i].lower())
    # print("Break Break")
    # print((AlphaAPI[i]).lower())
        # print(int((((eventsAPI[j][3][0]['h2h'][0])-1)*100)))
        try:
            if (AlphaAPI[i]).lower() == (kpWinnersProj[j].lower()):
                homeAlphaOdds = int(((((eventsAPI[i][3][0]['h2h'][0])-1)*100)*(kpWinProb[j])-(100*(1-(kpWinProb[j])))))
                if (homeAlphaOdds>0):
                    teamsToBetCBB.append({AlphaAPI[i]: homeAlphaOdds})
        except KeyError:
            continue

        try:    
            if (BetaAPI[i]).lower() == (kpLosersProj[j].lower()):
                awayBetaOdds = int(((((eventsAPI[i][3][0]['h2h'][1])-1)*100)*(1-(kpWinProb[j])))-(100*(kpWinProb[j])))
                if (awayBetaOdds>0):
                    teamsToBetCBB.append({BetaAPI[i]: awayBetaOdds})
        except KeyError:
            continue

        try:    
            if (AlphaAPI[i]).lower() == (kpLosersProj[j].lower()):
                awayAlphaOdds = int(((((eventsAPI[i][3][0]['h2h'][0])-1)*100)*(1-(kpWinProb[j]))-(100*(kpWinProb[j]))))
                if (awayAlphaOdds>0):
                    teamsToBetCBB.append({AlphaAPI[i]: awayAlphaOdds})
        except KeyError:
            continue


        try:
            if (BetaAPI[i]).lower() == (kpWinnersProj[j].lower()):
                homeBetaOdds = int(((((eventsAPI[i][3][0]['h2h'][1])-1)*100)*((kpWinProb[j])))-(100*(1-(kpWinProb[j]))))
                if (homeBetaOdds>0):
                    teamsToBetCBB.append({BetaAPI[i]: homeBetaOdds})
        except KeyError:
            continue

print(teamsToBetCBB)