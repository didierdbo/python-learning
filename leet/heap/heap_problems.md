Pattern 9 : Heap / Priority Queue

  Intuition : Accès rapide au minimum (ou maximum) — structure arborescente où le parent ≤ ses enfants. En Python : heapq implémente un
  min-heap (le plus petit au sommet).

  Quand l'utiliser :
  - Trouver le k-ième plus petit/grand élément
  - Fusionner k listes triées
  - Ordonnancer les tâches par priorité
  - Algorithmes greedy (Dijkstra, Prim, etc.)

  Template Python :
  import heapq

  # Min-heap par défaut
  heap = []
  heapq.heappush(heap, 5)
  heapq.heappush(heap, 3)
  min_val = heapq.heappop(heap)  # 3

  # Construire d'un coup
  arr = [3, 7, 1, 5]
  heapq.heapify(arr)  # O(n) vs O(n log n) si push un à un

  # Max-heap (inverser les signes)
  heapq.heappush(max_heap, -val)
  max_val = -heapq.heappop(max_heap)

  # Heap avec tuple (priorité, ordre, valeur)
  heap = []
  heapq.heappush(heap, (priority, counter, value))