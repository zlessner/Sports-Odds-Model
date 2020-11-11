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





player_names = [] # List that will receive all the players names

# The find_all () method is able to return all tags that meet restrictions within parentheses
tags_jogadores = page_elements.find_all("a", {"class": "spielprofil_tooltip"})
# In our case, we are finding all anchors with the class "spielprofil_tooltip"

# Now we will get only the names of all players
for tag_jogador in tags_jogadores:
    player_names.append(tag_jogador.text)






reason = [] # List that will receive all the names of the countries of the players’s previous leagues.

# The find_all () method is able to return all tags that meet restrictions within parentheses
tags_jogadores = page_elements.find_all("td", {"class": "links"})
# In our case, we are finding all anchors with the class "spielprofil_tooltip"

# Now we will get only the names of all players
for tag_jogador in tags_jogadores:
    reason.append(tag_jogador.text)




player_price = []

tags_custos = page_elements.find_all("td", {"class": "rechts"})

for tag_custo in tags_custos:
    texto_preco = tag_custo.text
    # The price text contains characters that we don’t need like £ (euros) and m (million) so we’ll remove them
    texto_preco = texto_preco.replace("£", "").replace("m","").replace("$", "")
    if "Th." in texto_preco:
        texto_preco = texto_preco.split('Th.')[0]
        texto_preco = texto_preco[0:]
        texto_preco = float(texto_preco)*.001
    # We will now convert the value to a numeric variable (float)
    preco_numerico = float(texto_preco)
    player_price.append(preco_numerico)


# print(player_price)


# Creating a DataFrame with our data
df = pd.DataFrame({
    "Player":player_names,
# "Reason": reason, 
"Player Value":player_price})

# Printing our gathered data
print(df)



#Try to use ID and not class so it excludes list of "Risk of Suspension"