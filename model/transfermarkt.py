import requests
from bs4 import BeautifulSoup
import pandas as pd

from modelSoccer import team_num_t




"""
To make the request to the page we have to inform the
website that we are a browser and that is why we
use the headers variable
"""
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

injuredTeams= []

for i in range(len(team_num_t)):
    team_num = team_num_t[i]


    # page_address stands for the data page address
    page_address = "https://www.transfermarkt.us/tottenham/sperrenundverletzungen/verein/{0}/plus/1".format(team_num)

    # In the object_response variable we will the download of the web page
    
    object_response = requests.get(page_address, headers=headers)

    # try:
    #  page1 = requests.get(ap)
        #except requests.exceptions.ConnectionError:
            #r.status_code = "Connection refused"

    """
    Now we will create a BeautifulSoup object from our object_response.
    The 'html.parser' parameter represents which parser we will use when creating our object,
    a parser is a software responsible for converting an entry to a data structure.
    """
    page_elements = BeautifulSoup(object_response.content, 'html.parser')


    # Total Value of team

    total_team_value = page_elements.find_all("div", {"class": "dataMarktwert"})

    for tag in total_team_value:
        team_value = tag.text
        team_value = team_value.replace("\n$", "").replace("m Total market value\n", "")
        if "bn" in team_value:
                team_value = team_value.split('bn')[0]
                team_value = team_value[0:]
                team_value = float(team_value)*1000

        elif "Th." in team_value:
                team_value = team_value.split('Th.')[0]
                team_value = team_value[0:]
                team_value = float(team_value)*.001

        else:
            team_value = float(team_value)






    # The find_all () method is able to return all tags that meet restrictions within parentheses

    injury_table = page_elements.find_all("div", {"id": "yw1"})



    player_names = [] # List that will receive all the players names




    for tag in injury_table:
        names = tag.find_all("a", {"class": "spielprofil_tooltip"})
        for tag in names:
            text_name = tag.text
            player_names.append(text_name)



    # In our case, we are finding all anchors with the class "spielprofil_tooltip"






    # Reason for injury

    reason = [] 


    injury_reason = page_elements.find_all("td", {"class": "links"})

    for tag_jogador in injury_reason:
        reason.append(tag_jogador.text)




    # Market Price

    player_price = []



    for tag in injury_table:
        tags_price = tag.find_all("td", {"class": "rechts"})
        for tag in tags_price:
            value_text = tag.text
            # The price text contains characters that we don’t need like £ (euros) and m (million) so we’ll remove them
            value_text = value_text.replace("£", "").replace("m","").replace("$", "").replace("-", "0")
            if "Th." in value_text:
                value_text = value_text.split('Th.')[0]
                value_text = value_text[0:]
                value_text = float(value_text)*.001
            # We will now convert the value to a numeric variable (float)
            value_number = float(value_text)
            player_price.append(value_number)







    #Player Age

    zentriert = [] 


    for tag in injury_table:
        tdTags = tag.find_all("td", {"class": "zentriert"})
        for tag in tdTags:
            zentriert.append(tag.text)


    # zentriert class brings back many things in table but age comes back every fifth element

    fifth = zentriert[0::5]

    age = [int(i) for i in fifth]





    # Creating a DataFrame with our data
    df = pd.DataFrame({
        "Player":player_names,
        "Age": age,
    "Reason": reason, 
    "Player Value":player_price
    })




    # Adding additional column to adjust current value for age

    df.loc[df['Age'] < 27, 'Adjusted Player Value'] = .9 * df['Player Value']
    df.loc[(df['Age'] < 33) & (df['Age'] >= 27), 'Adjusted Player Value'] = df['Player Value']
    df.loc[df['Age'] >= 33, 'Adjusted Player Value'] = 1.1* df['Player Value']




    team_value_injured = (df['Adjusted Player Value'].sum() / team_value)

    # print(team_value_injured)


    # Printing our gathered data

    # print(df)


    # Manually writing down #'s for all 538 teams - start off with PL to measure and test

    

    if team_value_injured > .09:
        injuredTeams.append(team_num)

# print(injuredTeams)
