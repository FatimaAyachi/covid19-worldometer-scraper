# covid19-worldometer-scraper
Un script Python léger de web scraping utilisant BeautifulSoup et Pandas pour extraire les statistiques COVID-19 en temps réel depuis Worldometer et les exporter au format CSV.
# COVID-19 Worldometer Web Scraper 🦠📊

Ce projet est un script automatisé en Python conçu pour extraire les données statistiques globales sur le COVID-19 directement depuis le site [Worldometer](https://www.worldometers.info/coronavirus/)[cite: 1].

## 🚀 Fonctionnalités
- **Requêtes HTTP sécurisées :** Utilisation de `requests` avec un en-tête `User-Agent` personnalisé pour éviter les erreurs d'accès (blocages 403).
- **Analyse HTML précise :** Utilisation de `BeautifulSoup` pour cibler et extraire le tableau principal des pays (`main_table_countries_today`)[cite: 1].
- **Nettoyage des données :** Traitement automatique des espaces superflus et structuration des données via `pandas`[cite: 1].
- **Exportation automatique :** Sauvegarde des données propres sous forme de fichier structuré `covid_19_web_scraping.csv`[cite: 1].

## 🛠️ Technologies Utilisées
- **Python 3.x**[cite: 1]
- **Requests** (Requêtes HTTP)[cite: 1]
- **BeautifulSoup4** (Parsing HTML)[cite: 1]
- **Pandas** (Manipulation et export des données)[cite: 1]
