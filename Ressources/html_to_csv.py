import pandas as pd
from bs4 import BeautifulSoup

# Lire le contenu du fichier HTML
with open('Ressources/liste_148.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse le HTML avec BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Trouver toutes les lignes du tableau
rows = soup.find_all('tr')

# Extraire les données du tableau
data = []
for row in rows:
    cells = row.find_all('td')
    row_data = [cell.get_text(separator=' ', strip=True) for cell in cells]
    data.append(row_data)

# Convertir les données en DataFrame pandas
df = pd.DataFrame(data, columns=["Nom commun", "Nom scientifique", "Famille", "Partie utilisée", "Usage"])

# Sauvegarder en fichier CSV
df.to_csv('Ressources/liste_148.csv', index=False, encoding='utf-8')

print("Conversion terminée. Le fichier CSV a été sauvegardé sous le nom 'tableau.csv'.")
