import requests
from bs4 import BeautifulSoup
import pandas as pd




"""
To make the request to the page we have to inform the
website that we are a browser and that is why we
use the headers variable
"""
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}

# page_address stands for the data page address
page_address = "https://www.transfermarkt.us/liverpool-fc/sperrenundverletzungen/verein/121/plus/1"

# In the object_response variable we will the download of the web page
object_response = requests.get(page_address, headers=headers)

"""
Now we will create a BeautifulSoup object from our object_response.
The 'html.parser' parameter represents which parser we will use when creating our object,
a parser is a software responsible for converting an entry to a data structure.
"""
page_elements = BeautifulSoup(object_response.content, 'html.parser')



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
        value_text = value_text.replace("£", "").replace("m","").replace("$", "")
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



age = []

# zentriert class brigns back many things in table but age comes back every fifth element

for i in range(len(zentriert)):
    if zentriert.index(zentriert[i]) % 5 == 0:
        zentriert[i] = int(zentriert[i])
        age.append(zentriert[i])




# Creating a DataFrame with our data
df = pd.DataFrame({
    "Player":player_names,
    "Age": age,
"Reason": reason, 
"Player Value":player_price})

# Printing our gathered data
print(df)