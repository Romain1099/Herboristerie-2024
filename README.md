# Herboristerie 2024

Compiler le fichier main avec LuaLaTeX en compilation simple. 

Pour la compilation incluant les index, table des matières et références, utiliser l'option "LuaLaTeX + MakeIndex + BibTeX" ( plus long ) 


# principales commandes à utiliser

Elles se trouvent définies dans le fichier Notes de stages

\voc{texte}  -> met en valeur ( gras + couleur ) un texte et le place dans l'index.
\vocref{url}{texte} -> idem mais ajoute un lien vers l'url visé. 

\label{keyword}
\lien{keyword}{expression}  -> lien interne au document redirigeant vers le label keyword. Génère une erreur si pas de label correspondant.

\ficheidentiteplante[]{}{}{}{}{}{}{}{} -> génère une fiche de présentation de plantes. voir modules de botanique.
\ficherecette[]{}{}{}{}{}{}{}{} -> génère une fiche de présentation de recettes. voir modules de recettes.
