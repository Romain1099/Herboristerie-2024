import re
from bs4 import BeautifulSoup

def html_to_latex_table(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    tables = soup.find_all('table')
    
    if not tables:
        return [], 0, ""
    
    # Extraire l'en-tête du premier tableau
    first_table = tables[0]
    first_header_row = first_table.find_all('tr')[0]
    header_cols = first_header_row.find_all(['td', 'th'])
    header_text = [col.get_text(strip=True) for col in header_cols]
    while len(header_text) < 5:
        header_text.append('')
    header_latex_row = ' & '.join(header_text[:5]) + ' \\\\ \\hline'
    
    latex_tables = []
    total_lines = 0
    
    for table in tables:
        rows = table.find_all('tr')[1:]  # Ignorer la première ligne d'en-tête
        latex_table = [header_latex_row]  # Utiliser l'en-tête extrait du premier tableau
        
        for i, row in enumerate(rows):
            cols = row.find_all(['td', 'th'])
            cols_text = [col.get_text(strip=True) for col in cols]
            # S'assurer que chaque ligne a exactement 5 colonnes
            while len(cols_text) < 5:
                cols_text.append('')
            # Ajouter \vocref pour le premier mot de la première colonne
            if cols_text:
                first_word = cols_text[0].split()[0].capitalize()
                url = f"https://fr.wikipedia.org/wiki/{first_word}"
                cols_text[0] = f"\\vocref{{{url}}}{{{cols_text[0]}}}"
            latex_row = ' & '.join(cols_text[:5]) + ' \\\\ \\hline'
            latex_table.append(latex_row)
            total_lines += 1
            
            if (i + 2) % 15 == 0:  # Compter l'en-tête aussi
                latex_tables.append(latex_table)
                latex_table = [header_latex_row]
        
        if latex_table:
            latex_tables.append(latex_table)
    
    return latex_tables, total_lines, header_latex_row

def generate_latex_document(latex_tables, header_latex_row):
    latex_document = [
        "\\documentclass{article}",
        "\\usepackage{geometry}",
        "\\geometry{a4paper, margin=1in}",
        "\\usepackage{tabularx}",
        "\\begin{document}"
    ]
    
    for table in latex_tables:
        if len(table) > 0:
            latex_document.append("\\noindent\\begin{tabularx}{\\textwidth}{|X|X|X|X|X|}")
            latex_document.append("\\hline")
            latex_document.extend(table)
            latex_document.append("\\end{tabularx}")
            latex_document.append("\\newpage")
    
    latex_document.append("\\end{document}")
    return "\n".join(latex_document)

def main():
    input_html_file = 'Ressources/liste_148_bis.html'
    output_latex_file = 'Ressources/liste_148_bis.tex'
    
    with open(input_html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    latex_tables, total_lines, header_latex_row = html_to_latex_table(html_content)
    latex_document = generate_latex_document(latex_tables, header_latex_row)
    
    with open(output_latex_file, 'w', encoding='utf-8') as file:
        file.write(latex_document)
    
    print(f"Le document LaTeX a été généré et enregistré sous {output_latex_file}")
    print(f"Nombre total de lignes dans tous les tableaux : {total_lines}")

if __name__ == "__main__":
    main()
