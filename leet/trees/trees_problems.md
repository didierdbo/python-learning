Pattern 7 — Trees (BFS/DFS)

  Intuition

  Un arbre binaire, c'est une structure récursive : chaque noeud a une valeur, un enfant gauche, un enfant droit (ou None). Presque tous les   problèmes d'arbres se ramènent à deux approches :

  DFS (Depth-First Search) — on descend en profondeur d'abord.
  - 3 ordres de parcours :
    - Preorder : noeud → gauche → droite
    - Inorder : gauche → noeud → droite (donne l'ordre trié pour un BST)
    - Postorder : gauche → droite → noeud
  - Implémentation : récursion (la pile d'appels fait le travail) ou pile explicite
  - Quand l'utiliser : trouver un chemin, calculer hauteur/profondeur, vérifier une propriété récursive

  BFS (Breadth-First Search) — on explore niveau par niveau.
  - Implémentation : file (queue) — collections.deque
  - Quand l'utiliser : parcours par niveau, plus court chemin dans un arbre, trouver le noeud le plus proche

  Template DFS récursif

  def dfs(node):
      if not node:
          return  # cas de base
      # traitement preorder ici
      dfs(node.left)
      # traitement inorder ici
      dfs(node.right)
      # traitement postorder ici

  Template BFS

  from collections import deque

  def bfs(root):
      if not root:
          return
      queue = deque([root])
      while queue:
          level_size = len(queue)  # pour traiter niveau par niveau
          for _ in range(level_size):
              node = queue.popleft()
              # traitement du noeud
              if node.left:
                  queue.append(node.left)
              if node.right:
                  queue.append(node.right)

  Classe TreeNode (standard LeetCode)

  class TreeNode:
      def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right

  Pièges classiques

  - Oublier le cas de base if not node → crash sur None.val
  - Confondre hauteur (bottom-up) et profondeur (top-down)
  - BFS : oublier de boucler sur level_size si on veut distinguer les niveaux

  Quand utiliser quoi :

  ┌────────────────────────────────────────────┬─────────────────────┐
  │                 Situation                  │      Approche       │
  ├────────────────────────────────────────────┼─────────────────────┤
  │ Hauteur, chemin, propriété récursive       │ DFS                 │
  ├────────────────────────────────────────────┼─────────────────────┤
  │ Parcours par niveau, plus court chemin     │ BFS                 │
  ├────────────────────────────────────────────┼─────────────────────┤
  │ Arbre très profond (risque stack overflow) │ BFS ou DFS itératif │
  └────────────────────────────────────────────┴─────────────────────┘

  Variantes classiques à connaître :
  - Invert Binary Tree (easy) — DFS, swap left/right récursivement
  - Validate BST (medium) — DFS inorder, vérifier que les valeurs sont croissantes
  - Lowest Common Ancestor (medium) — DFS, remonter quand on trouve p ou q