from __future__ import annotations
from utility import utils
#   Problème 1 — Easy : Reverse Linked List (LeetCode 206)
# 
#   ▎ Étant donné le head d'une singly linked list, reverse la liste et retourne le nouveau head.
# 
#   ▎ Exemple : 1 → 2 → 3 → 4 → 5 → 5 → 4 → 3 → 2 → 1
# 
#   Consignes :
#   - Utilise la technique prev/curr/nxt
#   - Itératif d'abord (O(n) temps, O(1) espace)
#   - Bonus : version récursive

class ListNode:
    def __init__(self, val=0, next:ListNode | None = None):
        self.val = val
        self.next = next
    def __repr__(self) -> str:
        return " → ".join(str(v) for v in self.to_list())
    
    def to_list(self) -> list[int]:
        curr = self
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res

@utils.print_result
def reverse(head:ListNode) -> ListNode | None:
    prev = None
    curr = head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev 

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
   
new_head = reverse(head)

# Problème 2 — Medium : Merge Two Sorted Lists (LeetCode 21)

#   ▎ Étant donné les head de deux linked lists triées, merge-les en une seule liste triée et retourne le head.

#   ▎ Exemple : 1 → 2 → 4 + 1 → 3 → 4 → 1 → 1 → 2 → 3 → 4 → 4

#   Consignes :
#   - Utilise la technique du dummy head — crée un noeud fictif, construis la liste mergée après lui, retourne dummy.next
#   - Compare les valeurs courantes des deux listes, avance le pointeur de celle qui a la plus petite
#   - Quand une des deux listes est épuisée, rattache le reste de l'autre
#   - O(n + m) temps, O(1) espace

@utils.print_result
def merge(head_a:ListNode | None, head_b:ListNode | None) -> ListNode | None:
    dummy = ListNode()
    
    head = dummy
    while head_a and head_b:
        
        if head_a.val < head_b.val:
           head.next = head_a
           head_a = head_a.next
        else:
           head.next = head_b
           head_b = head_b.next   
        
        head = head.next
    head.next = head_a or head_b
           
    return dummy.next

# Debrief Linked Lists

#   Deux problèmes, deux patterns essentiels maîtrisés :
#   - Reverse → prev/curr/nxt, retourner une flèche par tour
#   - Merge sorted → dummy head + comparaison courante

#   Problème bonus si tu veux aller plus loin

#   Linked List Cycle (LeetCode 141, easy) — technique slow/fast :
#   ▎ Étant donné un head, détermine si la liste contient un cycle. Retourne True/False.
#   ▎ - slow avance de 1, fast avance de 2
#   ▎ - S'ils se rencontrent → cycle. Si fast atteint None → pas de cycle.

@utils.print_result
def is_cyclic(head:ListNode) -> bool:

    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next # type: ignore
        fast = fast.next.next
        if slow == fast:
            return True
        
    return False

node_2 = ListNode(2)
head = ListNode(1, node_2)
node_2.next = ListNode(3, ListNode(4, ListNode(5, node_2)))

is_cyclic(head)
