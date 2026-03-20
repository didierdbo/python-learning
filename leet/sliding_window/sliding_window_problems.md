Pattern 3 : Sliding Window
*Quand l'utiliser* : chaque fois qu'on cherche un sous-tableau contigu (ou sous-chaîne) qui satisfait une condition - longueur max/min, somme cible, caractère distincts, etc.

*Deux variantes* :
1. Fenêtre de taille fixe (k)
- Tu avances la fenêtre d'un cran à chaque itération : tu ajoutes l'élément de droite, tu retires celui de gauche.
- Example : "mas sum of subarray of size k"

2. Fenêtre de taille variable
- Deux pointeurs left et right. Tu étends right pour explorer, tu contractes left quand la contrainte est violée.
- C'est la variante la plus fréquente en entretien.

Template (taille variable) :

left = 0
state = ... # compteur, set, dict, somme...

for right in range(len(arr)):
    # 1. Ajouter arr[right] dans state
    # 2. Tant que la contrainte est violée :
    #       retirer arr[left] du state
    #       left += 1
    # 3. Mettre à jour le résultat (max/min window size, etc.)
Complexité : O(n) - chaque élément est ajouté et retiré au plus une fois/
Piège classique : oublier de mettre à jour le state quand on déplace left.