import requests
from bs4 import BeautifulSoup
import pandas as pd

#url de la page Worldmoters pour les statistiques Covid-19
url_base="https://www.worldometers.info/coronavirus/"

#user agent pour eviter les prb d'acces
headers = {
    "User-Agent" : "Mozilla/5.0"
}
#envoyer un requte HTTP GET a la page
resultats = requests.get(url_base, headers=headers)
#verifie si la requete a reussi
resultats.raise_for_status()

#Analyse le contenu HTML de la page avec BeautifulSoup
soup = BeautifulSoup(resultats.text, "html.parser")

#trouver le tableau principale des pays
table = soup.find("table", id="main_table_countries_today")

#Extraire les noms des colonnes depuis l'entete du tableau
headers_clm = table.find("thead").find_all("th")
columns = [header.text.strip() for header in headers_clm]  #Supp les espaces

#les enregistrement
data = []

#trouver le corps du tab (<tbody>) qui contient les donnees
body = table.find("tbody")
rows = body.find_all("tr")  #recuperer toutes les lignes du tableau

#Parcourir chaque ligne et extraire les cellules (<td>)
for row in rows:
    cols = row.find_all("td")
    if cols:  #ingnorer les lignes vides
        row_data = [col.text.strip() for col in cols] #clean le texte
        data.append(row_data) #Ajouter la ligne a la liste des donnees

#creation du data farme
data_farme = pd.DataFrame(data,columns=columns)
print("💖 Fatima, making Python dance to your curiosity beats! 🐍🎶")
data_farme.to_csv("covid_19_web_scraping.csv",index=False)