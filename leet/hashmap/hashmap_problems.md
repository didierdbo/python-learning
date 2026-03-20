*Hash Maps - Quand les utiliser*

*Intuition* : une hash map (dict en Python) te donne un accès O(1) en lecture/écriture. Dès qu'un problème te demande de compter, chercher un complément, ou détecter un doublon, pense hash map.

*Cas typiques* :
- "Trouver deux éléments dont la somme vaut "X" -> stocker ce qu'on a déjà vu
- "Compter les occurences" -> dict ou collections.Counter
- "Trouver le premier élément unique / dupliqué"
- "Grouper des éléments par propriété" (anagrammes, etc.)

*Template mental* :
créer un dict vide
pour chaque élément :
    calculer ce qu'on cherche (complément, clé de regroupement...)
    si c'est dans le dict -> on a trouvé
    sinon -> stocker l'élément dans le dict

*Complexité* : O(n) temps, O(n) espace - le trade-off classique espace contre temps.
