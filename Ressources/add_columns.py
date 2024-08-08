# Lecture du fichier CSV
file_path = 'Ressources/liste_148.csv'

with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Ajouter une virgule à la fin de chaque ligne
lines = [line.strip() + ',' + '\n' for line in lines]

# Écriture dans le nouveau fichier CSV
output_file_path = 'Ressources/liste_148_modified.csv'

with open(output_file_path, 'w', encoding='utf-8') as file:
    file.writelines(lines)

output_file_path
