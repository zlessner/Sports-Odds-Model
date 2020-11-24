from urllib.request import urlretrieve as retrieve
from moneyline.moneylineSoccer import theOddsAPIGames, gameDate, futureGame, yesterdayGame
import csv
import time
from datetime import datetime


stringGameDate = str(futureGame)

stringYesterdayDate = str(yesterdayGame)



url = 'https://projects.fivethirtyeight.com/soccer-api/club/spi_matches.csv'

retrieve(url,'soccer.csv')

f = open('soccer.csv', 'r')

reader = csv.reader(f)
next(reader)

fullList=[]


#Parse CSV file for sport, teams, and odds

for row in reader:
        fullList.append([row[1], row[3], row[4], row[5], float(row[8]),float(row[9]),float(row[10]),row[15],row[16],row[17]])


FiveThirtyEightGames=[]


for game in fullList:
    if game[0] == stringGameDate:
        FiveThirtyEightGames.append(game)


FiveThirtyEightGamesYesterday=[]

def pastResults(fullList):

    # List of completed games to get results from

    for game in fullList:
        if game[0] == stringYesterdayDate:
            FiveThirtyEightGamesYesterday.append(game)



    for i in range(len(FiveThirtyEightGamesYesterday)):
        if len(FiveThirtyEightGamesYesterday[i][7])>0:
            FiveThirtyEightGamesYesterday[i][7] = float(FiveThirtyEightGamesYesterday[i][7])
        
        if len(FiveThirtyEightGamesYesterday[i][8])>0:
            FiveThirtyEightGamesYesterday[i][8] = float(FiveThirtyEightGamesYesterday[i][8])



    for i in range(len(FiveThirtyEightGamesYesterday)):

        if FiveThirtyEightGamesYesterday[i][7] > FiveThirtyEightGamesYesterday[i][8]:
            FiveThirtyEightGamesYesterday[i][9] = FiveThirtyEightGamesYesterday[i][2]

        elif FiveThirtyEightGamesYesterday[i][7] < FiveThirtyEightGamesYesterday[i][8]:
            FiveThirtyEightGamesYesterday[i][9] = FiveThirtyEightGamesYesterday[i][3]

        else:
            FiveThirtyEightGamesYesterday[i][9] = "Draw"


pastResults(fullList)


# Parse Sports Betting API for sport, game time, teams, and odds

eventsAPI = {}

for i in range(len(theOddsAPIGames)):
    for j in range(len(theOddsAPIGames[i]['sites'])):
        eventsAPI[i] = [theOddsAPIGames[i]['sport_key']], [theOddsAPIGames[i]['commence_time']], [theOddsAPIGames[i]['teams']], [theOddsAPIGames[i]['sites'][j]['odds']]
        break



AlphaAPIx=[]
BetaAPIx=[]
AlphaAPI=[]
BetaAPI=[]
OddsA=[]
OddsB=[]
OddsC=[]

#Adding first team to AlphaAPI, second team to BetaAPI, first teams odds to OddsA, second team odds to OddsB, and draw odds to OddsC

for i in eventsAPI:
    if (datetime.utcfromtimestamp(eventsAPI[i][1][0]).strftime('%Y-%m-%d') == stringGameDate):
        AlphaAPIx.append(eventsAPI[i][2][0][0])
        BetaAPIx.append(eventsAPI[i][2][0][1])
        OddsA.append(eventsAPI[i][3][0]['h2h'][0])
        OddsB.append(eventsAPI[i][3][0]['h2h'][1])
        OddsC.append(eventsAPI[i][3][0]['h2h'][2])


#Slightly altering names to match up to 538

for i in range(len(AlphaAPIx)):
    AlphaAPI.append(AlphaAPIx[i].replace("Ch\\u00e2teauroux", 'Chateauroux').replace("FC Chambly", 'Chambly Thelle FC').replace("Le Mans FC", 'Le Mans').replace("Rodez AF", 'Rodez').replace("Orl\\u00e9ans", 'Orléans').replace("SM Caen", 'Caen').replace("EA Guingamp", 'Guingamp').replace("AC Ajaccio", 'Ajaccio').replace("Dijon", 'Dijon FCO').replace("Nîmes Olympique", 'Nimes').replace("Stade de Reims", 'Reims').replace("Saint Etienne", 'St Etienne').replace("Wolverhampton Wanderers", 'Wolverhampton').replace("Newcastle United", 'Newcastle').replace("Bournemouth", 'AFC Bournemouth').replace("Blackburn Rovers", 'Blackburn').replace("Birmingham City", 'Birmingham').replace("Wigan Athletic", 'Wigan').replace("Bolton Wanderers", 'Bolton').replace("Barrow AFC", 'Barrow').replace("Olympiakos", 'Olympiacos').replace("RCD Espanyol", 'Espanyol').replace("Leganés", 'Leganes').replace("Zaragoza", 'Real Zaragoza').replace("Málaga", 'M√°laga').replace("Sporting Gijón", 'Sporting Gij√≥n').replace("Oviedo", 'Real Oviedo').replace("CF Fuenlabrada", 'Fuenlabrada').replace("CD Mirandés", 'Mirandes').replace("CD Castellón", 'Castellon').replace("UD Logroñés", 'Logrones').replace("Alcorcón", 'AD Alcorcon').replace("Sabadell FC", 'Sabadell').replace("İstanbul Başakşehir FK", 'Istanbul Basaksehir'))
    BetaAPI.append(BetaAPIx[i].replace("Ch\\u00e2teauroux", 'Chateauroux').replace("FC Chambly", 'Chambly Thelle FC').replace("Le Mans FC", 'Le Mans').replace("Rodez AF", 'Rodez').replace("Orl\\u00e9ans", 'Orléans').replace("SM Caen", 'Caen').replace("EA Guingamp", 'Guingamp').replace("AC Ajaccio", 'Ajaccio').replace("Dijon", 'Dijon FCO').replace("Nîmes Olympique", 'Nimes').replace("Stade de Reims", 'Reims').replace("Saint Etienne", 'St Etienne').replace("Wolverhampton Wanderers", 'Wolverhampton').replace("Newcastle United", 'Newcastle').replace("Bournmouth", 'AFC Bournmouth').replace("Blackburn Rovers", 'Blackburn').replace("Birmingham City", 'Birmingham').replace("Wigan Athletic", 'Wigan').replace("Bolton Wanderers", 'Bolton').replace("Barrow AFC", 'Barrow').replace("Olympiakos", 'Olympiacos').replace("RCD Espanyol", 'Espanyol').replace("Leganés", 'Leganes').replace("Zaragoza", 'Real Zaragoza').replace("Málaga", 'M√°laga').replace("Sporting Gijón", 'Sporting Gij√≥n').replace("Oviedo", 'Real Oviedo').replace("CF Fuenlabrada", 'Fuenlabrada').replace("CD Mirandés", 'Mirandes').replace("CD Castellón", 'Castellon').replace("UD Logroñés", 'Logrones').replace("Alcorcón", 'AD Alcorcon').replace("Sabadell FC", 'Sabadell').replace("İstanbul Başakşehir FK", 'Istanbul Basaksehir')) 



#Matching up 538 teams with sports betting API teams, whether to win, lose or draw
#Performing calculations to see if expected value of winnings on a $100 dollar bet is over $10 (10% return)

teamsToBet1=[]
potential_winnings=[]
winning_odds=[]

def Prediction():

    for i in range(len(AlphaAPI)):
        for j in range(len(FiveThirtyEightGames)):
            if AlphaAPI[i] == FiveThirtyEightGames[j][2]:
                homeAlphaOdds = int((((OddsA[i])-1)*100)*(float(FiveThirtyEightGames[j][4]))-(100*(1-(float(FiveThirtyEightGames[j][4])))))
                homeAlphaDrawOdds = int((((OddsC[i])-1)*100)*(float(FiveThirtyEightGames[j][6]))-(100*(1-(float(FiveThirtyEightGames[j][6])))))
                if (homeAlphaOdds>10):
                    teamsToBet1.append({AlphaAPI[i]: homeAlphaOdds})
                    potential_winnings.append(int(((OddsA[i])-1)*100))
                    winning_odds.append(float(FiveThirtyEightGames[j][4]))
                if (homeAlphaDrawOdds>10):
                    teamsToBet1.append({AlphaAPI[i] + " Draw": homeAlphaDrawOdds})
                    winning_odds.append(float(FiveThirtyEightGames[j][6]))
                    potential_winnings.append(int(((OddsC[i])-1)*100))
                
            if BetaAPI[i] == FiveThirtyEightGames[j][3]:
                awayBetaOdds = int((((OddsB[i])-1)*100)*(float(FiveThirtyEightGames[j][5]))-(100*(1-(float(FiveThirtyEightGames[j][5])))))
                if (awayBetaOdds>10):
                    teamsToBet1.append({BetaAPI[i]: awayBetaOdds})
                    potential_winnings.append(int(((OddsB[i])-1)*100))
                    winning_odds.append(float(FiveThirtyEightGames[j][5]))

            if AlphaAPI[i] == FiveThirtyEightGames[j][3]:
                awayAlphaOdds = int((((OddsA[i])-1)*100)*(float(FiveThirtyEightGames[j][5]))-(100*(1-(float(FiveThirtyEightGames[j][5])))))
                awayAlphaDrawOdds = int((((OddsC[i])-1)*100)*(float(FiveThirtyEightGames[j][6]))-(100*(1-(float(FiveThirtyEightGames[j][6])))))
                if (awayAlphaOdds>10):
                    teamsToBet1.append({AlphaAPI[i]: awayAlphaOdds})
                    potential_winnings.append(int(((OddsA[i])-1)*100))
                    winning_odds.append(float(FiveThirtyEightGames[j][5]))
                if (awayAlphaDrawOdds>10):
                    teamsToBet1.append({AlphaAPI[i] + " Draw": awayAlphaDrawOdds})
                    winning_odds.append(float(FiveThirtyEightGames[j][6]))
                    potential_winnings.append(int(((OddsC[i])-1)*100))
                
            if BetaAPI[i] == FiveThirtyEightGames[j][2]:
                homeBetaOdds = int((((OddsB[i])-1)*100)*(float(FiveThirtyEightGames[j][4]))-(100*(1-(float(FiveThirtyEightGames[j][4])))))
                if (homeBetaOdds>10):
                    teamsToBet1.append({BetaAPI[i]: homeBetaOdds})
                    potential_winnings.append(int(((OddsB[i])-1)*100))
                    winning_odds.append(float(FiveThirtyEightGames[j][4]))


Prediction()

 #Comment the below in if just want results for this one model          
    
# print(teamsToBet1)


teams = []


for i in range(len(teamsToBet1)):
    for key in teamsToBet1[i].keys():
        if key[-5:] == ' Draw':
            teams.append(key[:-5])
        else:
            teams.append(key)




# print(teams)

team_num_t =[]

for i in range(len(teams)):
# Premier League
    if teams[i] == "Liverpool":
        team_num_t.append(31)
    if teams[i] == "Manchester City":
        team_num_t.append(281)
    if teams[i] == "Chelsea":
        team_num_t.append(631)
    if teams[i] == "Manchester United":
        team_num_t.append(985)
    if teams[i] == "Tottenham":
        team_num_t.append(148)
    if teams[i] == "Arsenal":
        team_num_t.append(11)
    if teams[i] == "Everton":
        team_num_t.append(29)
    if teams[i] == "Leicester City":
        team_num_t.append(1003)
    if teams[i] == "Wolverhampton":
        team_num_t.append(543)
    if teams[i] == "Aston Villa":
        team_num_t.append(405)
    if teams[i] == "West Ham":
        team_num_t.append(379)
    if teams[i] == "Newcastle United":
        team_num_t.append(762)
    if teams[i] == "Brighton and Hove Albion":
        team_num_t.append(1237)
    if teams[i] == "Crystal Palace":
        team_num_t.append(873)
    if teams[i] == "Southhampton":
        team_num_t.append(180)
    if teams[i] == "Fulham":
        team_num_t.append(931)
    if teams[i] == "Leeds United":
        team_num_t.append(399)
    if teams[i] == "Sheffield United":
        team_num_t.append(350)
    if teams[i] == "Burnley":
        team_num_t.append(1132)
    if teams[i] == "West Brom Albion":
        team_num_t.append(984)


# Championship
    if teams[i] == "AFC Bournemouth":
        team_num_t.append(989)
    if teams[i] == "Norwich City":
        team_num_t.append(1123)
    if teams[i] == "Watford":
        team_num_t.append(1010)
    if teams[i] == "Brentford":
        team_num_t.append(1148)
    if teams[i] == "Cardiff City":
        team_num_t.append(603)
    if teams[i] == "Bristol City":
        team_num_t.append(698)
    if teams[i] == "Nottingham Forest":
        team_num_t.append(703)
    if teams[i] == "Swansea City":
        team_num_t.append(2288)
    if teams[i] == "Stoke City":
        team_num_t.append(512)
    if teams[i] == "Reading":
        team_num_t.append(1032)
    if teams[i] == "Middlesbrough":
        team_num_t.append(641)
    if teams[i] == "Derby County":
        team_num_t.append(22)
    if teams[i] == "Blackburn":
        team_num_t.append(164)
    if teams[i] == "Birmingham":
        team_num_t.append(337)
    if teams[i] == "Huddersfield Town":
        team_num_t.append(1110)
    if teams[i] == "Millwall":
        team_num_t.append(1028)
    if teams[i] == "Sheffield Wednesday":
        team_num_t.append(1035)
    if teams[i] == "Preston North End":
        team_num_t.append(466)
    if teams[i] == "Queens Park Rangers":
        team_num_t.append(1039)
    if teams[i] == "Barnsley":
        team_num_t.append(349)
    if teams[i] == "Luton Town":
        team_num_t.append(1031)
    if teams[i] == "Coventry City":
        team_num_t.append(990)
    if teams[i] == "Rotherham United":
        team_num_t.append(1194)
    if teams[i] == "Wycombe Wanderers":
        team_num_t.append(2805)



    # League 1
    if teams[i] == "Hull City":
        team_num_t.append(3008)
    if teams[i] == "Ipswich Town":
        team_num_t.append(677)
    if teams[i] == "Blackpool":
        team_num_t.append(1181)
    if teams[i] == "Sunderland":
        team_num_t.append(289)
    if teams[i] == "Shrewsbury Town":
        team_num_t.append(3054)
    if teams[i] == "Charlton Athletic":
        team_num_t.append(358)
    if teams[i] == "Fleetwood Town":
        team_num_t.append(11177)
    if teams[i] == "Oxford United":
        team_num_t.append(988)
    if teams[i] == "Milton Keynes Dons":
        team_num_t.append(991)
    if teams[i] == "Wigan":
        team_num_t.append(1071)
    if teams[i] == "Swindon Town":
        team_num_t.append(352)
    if teams[i] == "Doncaster Rovers":
        team_num_t.append(2454)
    if teams[i] == "Burton Albion":
        team_num_t.append(2963)
    if teams[i] == "Portsmouth":
        team_num_t.append(1020)
    if teams[i] == "Gillingham":
        team_num_t.append(2814)
    if teams[i] == "Bristol Rovers":
        team_num_t.append(2455)
    if teams[i] == "Plymouth Argyle":
        team_num_t.append(2262)
    if teams[i] == "Northampton Town":
        team_num_t.append(1032)
    if teams[i] == "Lincoln City":
        team_num_t.append(1198)
    if teams[i] == "Peterborough United":
        team_num_t.append(1072)
    if teams[i] == "Rochdale":
        team_num_t.append(1088)
    if teams[i] == "Crewe Alexandra":
        team_num_t.append(1042)
    if teams[i] == "AFC Wimbledon":
        team_num_t.append(3884)
    if teams[i] == "Accrington Stanley":
        team_num_t.append(3688)


    # League 2
    if teams[i] == "Salford City":
        team_num_t.append(34888)
    if teams[i] == "Southend United":
        team_num_t.append(2793)
    if teams[i] == "Bolton":
        team_num_t.append(355)
    if teams[i] == "Oldham Athletic":
        team_num_t.append(1078)
    if teams[i] == "Tranmere Rovers":
        team_num_t.append(1074)
    if teams[i] == "Morecambe":
        team_num_t.append(3697)
    if teams[i] == "Colchester United":
        team_num_t.append(1060)
    if teams[i] == "Grimsby Town":
        team_num_t.append(1034)
    if teams[i] == "Leyton Orient":
        team_num_t.append(1150)
    if teams[i] == "Mansfield Town":
        team_num_t.append(3820)
    if teams[i] == "Bradford City":
        team_num_t.append(1027)
    if teams[i] == "Scunthorpe United":
        team_num_t.append(2964)
    if teams[i] == "Barrow":
        team_num_t.append(6168)
    if teams[i] == "Port Vale":
        team_num_t.append(1211)
    if teams[i] == "Cheltenham Town":
        team_num_t.append(3371)
    if teams[i] == "Exeter City":
        team_num_t.append(6699)
    if teams[i] == "Carlisle United":
        team_num_t.append(1220)
    if teams[i] == "Crawley Town":
        team_num_t.append(3537)
    if teams[i] == "Newport County":
        team_num_t.append(3716)
    if teams[i] == "Cambridge United":
        team_num_t.append(986)
    if teams[i] == "Walsall":
        team_num_t.append(899)
    if teams[i] == "Forest Green Rovers":
        team_num_t.append(3455)
    if teams[i] == "Stevenage":
        team_num_t.append(3684)
    if teams[i] == "Harrogate Town":
        team_num_t.append(12020)


    # MLS
    if teams[i] == "Los Angeles FC":
        team_num_t.append(51828)
    if teams[i] == "Inter Miami CF":
        team_num_t.append(69261)
    if teams[i] == "Atlanta United FC":
        team_num_t.append(51663)
    if teams[i] == "Toronto FC":
        team_num_t.append(11141)
    if teams[i] == "Los Angeles Galaxy":
        team_num_t.append(1061)
    if teams[i] == "Seattle Sounders FC":
        team_num_t.append(9636)
    if teams[i] == "Sporting Kansas City":
        team_num_t.append(4284)
    if teams[i] == "New York City FC":
        team_num_t.append(40058)
    if teams[i] == "Columbus Crew SC":
        team_num_t.append(813)
    if teams[i] == "Orlando City SC":
        team_num_t.append(45604)
    if teams[i] == "Portland Timbers":
        team_num_t.append(4291)
    if teams[i] == "Minnesota United FC":
        team_num_t.append(56089)
    if teams[i] == "Philadelphia Union":
        team_num_t.append(25467)
    if teams[i] == "DC United":
        team_num_t.append(2440)
    if teams[i] == "FC Dallas":
        team_num_t.append(8816)
    if teams[i] == "New England Revolution":
        team_num_t.append(626)
    if teams[i] == "Chicago Fire FC":
        team_num_t.append(432)
    if teams[i] == "Colorado Rapids":
        team_num_t.append(1247)
    if teams[i] == "New York Red Bulls":
        team_num_t.append(623)
    if teams[i] == "FC Cincinnati":
        team_num_t.append(51772)
    if teams[i] == "Vancouver Whitecaps FC":
        team_num_t.append(6321)
    if teams[i] == "Montreal Impact":
        team_num_t.append(4078)
    if teams[i] == "Nashville SC":
        team_num_t.append(63966)
    if teams[i] == "Houston Dynamo":
        team_num_t.append(9168)
    if teams[i] == "San Jose Earthquakes":
        team_num_t.append(218)
    if teams[i] == "Real Salt Lake City":
        team_num_t.append(6643)


    # Bundesliga
    if teams[i] == "Borussia Dortmund":
        team_num_t.append(16)
    if teams[i] == "RB Leipzig":
        team_num_t.append(23826)
        

    # Russian Premier League 
    if teams[i] == "FC Krasnodar":
        team_num_t.append(16704)
    if teams[i] == "Zenit St Petersburg":
        team_num_t.append(964)

    # Belgium First Division
    if teams[i] == "Club Brugge":
        team_num_t.append(2282)

    # Greek Super League
    if teams[i] == "Olympiacos":
        team_num_t.append(683)

    # Spanish Segunda Division
    if teams[i] == "Espanyol":
        team_num_t.append(714)
    if teams[i] == "Almeria":
        team_num_t.append(3302)
    if teams[i] == "Leganes":
        team_num_t.append(1244)
    if teams[i] == "Girona FC":
        team_num_t.append(12321)
    if teams[i] == "Mallorca":
        team_num_t.append(237)
    if teams[i] == "Rayo Vallecano":
        team_num_t.append(367)
    if teams[i] == "Las Palmas":
        team_num_t.append(472)
    if teams[i] == "Real Zaragoza":
        team_num_t.append(142)
    if teams[i] == "M√°laga":
        team_num_t.append(1084)
    if teams[i] == "Sporting Gij√≥n":
        team_num_t.append(2448)
    if teams[i] == "Tenerife":
        team_num_t.append(648)
    if teams[i] == "Real Oviedo":
        team_num_t.append(2497)
    if teams[i] == "Albacete":
        team_num_t.append(1532)
    if teams[i] == "Fuenlabrada":
        team_num_t.append(16486)
    if teams[i] == "FC Cartagena":
        team_num_t.append(7077)
    if teams[i] == "Mirandes":
        team_num_t.append(13222)
    if teams[i] == "SD Ponferradina":
        team_num_t.append(4032)
    if teams[i] == "Castellon":
        team_num_t.append(2502)
    if teams[i] == "Logrones":
        team_num_t.append(24420)
    if teams[i] == "Lugo":
        team_num_t.append(11000)
    if teams[i] == "Sabadell":
        team_num_t.append(11422)
    if teams[i] == "AD Alcorcon":
        team_num_t.append(11596)


    # Spanish Primera Division
    if teams[i] == "Real Madrid":
        team_num_t.append(418)

    # Turkey Super League
    if teams[i] == "Istanbul Basaksehir":
        team_num_t.append(6890)


    # Non-538
    if teams[i] == "Shakhtar Donetsk":
        team_num_t.append(660)
    




# print(team_num_t)
