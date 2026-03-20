Pattern 6 — Linked Lists

Quand l'utiliser

- Manipulation de séquences ordonnées sans accès par index
- Insertion/suppression en O(1) quand on a le pointeur
- Problèmes de réorganisation en place (reverse, merge, detect cycle)

Intuition clé

Contrairement aux arrays, on ne peut pas sauter à un index — on parcourt noeud par noeud. La plupart des problèmes se résolvent avec des pointeurs : prev, curr, next pour reverse, slow/fast pour trouver le milieu ou détecter un cycle.

Template — structure de base

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

Techniques récurrentes

1. Dummy head — un noeud fictif avant le vrai head, simplifie les edge cases (suppression du premier élément, merge de deux listes)
2. Slow/Fast pointers — slow avance de 1, fast de 2. Quand fast atteint la fin, slow est au milieu. Si fast rattrape slow → cycle
3. Reverse in place — 3 pointeurs prev/curr/nxt, on retourne les flèches une par une

Pièges classiques

- Oublier de gérer head is None ou liste à un seul élément
- Perdre la référence au next avant de modifier le pointeur (toujours sauvegarder nxt = curr.next avant)
- Oublier de retourner dummy.next plutôt que head quand on utilise un dummy