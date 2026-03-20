*Pattern 2: Two Pointers*

*Intuition* : on place deux pointeurs (indices) sur une structure triée ou linéaire, et on les déplace selon une condition. Ca remplace une double boucle O(n^2) par un seul passage O(n).

*Deux variantes principales* :

1. Pointeurs opposés (début + fin) - sur un tableau trié, on resserre vers le centre
left = 0, right = len - 1
tant que left < right :
    si condition remplie -> trouvé
    si trop petit -> left += 1
    si trop grand -> right -= 1
2. Pointeurs dans la même direction (slow + fast) - pour filtrer, dédupliquer, ou detecter des cycles
slow = 0
pour fast in range(n) :
    si condition -> copier et avancer slow

*Quand l'utiliser* :
- Tableau trié + chercher paire/triplet
- Supprimer des doublons in-place
- Inverser une chaîne/tableau
- Conteneur avec le plus d'eau, piéger l'eau de pluie
