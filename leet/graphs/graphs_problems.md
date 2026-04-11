Pattern 8 : Graphs — le pattern qu'on attaque aujourd'hui.

  Quand utiliser les graphes ?

  Dès que le problème parle de :
  - connexions entre éléments (amis, villes, cours pré-requis)
  - chemins, composantes connexes, cycles
  - grille 2D à explorer (chaque cellule = noeud, voisins = haut/bas/gauche/droite)

  Représentations

  Adjacency list (la plus courante en interview) :
  graph = {
      'A': ['B', 'C'],
      'B': ['A', 'D'],
      'C': ['A'],
      'D': ['B'],
  }
  # ou avec defaultdict(list) quand on construit depuis une edge list

  Matrice d'adjacence — rarement utilisée en interview (mémoire O(V²)), sauf si le problème la donne.

  Templates essentiels

  DFS (récursif) — explorer en profondeur, marquer les visités :
  def dfs(node, graph, visited):
      visited.add(node)
      for neighbor in graph[node]:
          if neighbor not in visited:
              dfs(neighbor, graph, visited)

  BFS (itératif avec deque) — explorer niveau par niveau, utile pour le plus court chemin :
  from collections import deque

  def bfs(start, graph):
      visited = {start}
      queue = deque([start])
      while queue:
          node = queue.popleft()
          for neighbor in graph[node]:
              if neighbor not in visited:
                  visited.add(neighbor)
                  queue.append(neighbor)

  Points clés

  - visited : toujours un set, jamais oublier de marquer les noeuds visités (sinon boucle infinie)
  - DFS : stack (ou récursion) → explore un chemin à fond avant de revenir
  - BFS : queue → explore tous les voisins d'abord, garantit le plus court chemin en nombre d'arêtes
  - Sur une grille : les voisins sont [(r-1,c), (r+1,c), (r,c-1), (r,c+1)], vérifier les bornes