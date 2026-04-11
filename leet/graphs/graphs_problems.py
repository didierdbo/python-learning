from utility import utils

# Problème 1 (easy) — Number of Islands (LeetCode 200)

#   Donnée : une grille m x n de '1' (terre) et '0' (eau). Compter le nombre d'îles (groupes de '1' connectés horizontalement/verticalement).

#   Input:
#   [["1","1","0","0","0"],
#    ["1","1","0","0","0"],
#    ["0","0","1","0","0"],
#    ["0","0","0","1","1"]]
#   Output: 3

#   Indices :
#   - Parcourir chaque cellule de la grille
#   - Quand tu trouves un '1' non visité → c'est une nouvelle île, lance un DFS/BFS pour marquer toute l'île comme visitée
#   - Incrémenter le compteur à chaque nouvelle île trouvée
#   - Pour le visited : tu peux modifier la grille en place ('1' → '0') ou utiliser un set

#   Essaie d'implémenter numIslands(grid: list[list[str]]) -> int. A toi.
from collections import deque

def dfs(node: tuple[int, int], grid: list[list[str]], visited: set, rows, cols) -> None:
    r, c = node
    if c < 0 or c >= cols or r < 0 or r >= rows:
        return    
    if (r, c) in visited or grid[r][c] == "0":
        return   
    visited.add((r, c)) 
    dfs((r-1, c), grid, visited, rows, cols)
    dfs((r+1, c), grid, visited, rows, cols)
    dfs((r, c-1), grid, visited, rows, cols)
    dfs((r, c+1), grid, visited, rows, cols)

@utils.print_result    
def numIslands(grid: list[list[str]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    visited: set[tuple[int, int]] = set()
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):                  
            if (r, c) not in visited and grid[r][c] == "1":
                count += 1
                dfs((r, c), grid, visited, rows, cols)
    return count


grid = [["1","1","0","0","0"],
         ["1","1","0","0","0"],
         ["0","0","1","0","0"],
         ["0","0","0","1","1"]]

numIslands(grid)

# Clone Graph — Le problème

#   On te donne une référence à un noeud dans un graphe non-dirigé connexe. Chaque noeud a :
#   - val (int)
#   - neighbors (liste de noeuds)

#   Tu dois retourner un deep copy du graphe entier. Aucun noeud du clone ne doit pointer vers un noeud de l'original.

#   ---
#   Intuition

#   Le piège principal : les cycles. Si tu fais un DFS/BFS naïf sans tracker ce que tu as déjà copié, tu boucles infiniment.

#   L'idée clé : maintenir un dictionnaire old_node → new_node (mapping original vers copie). Ce dict sert à la fois de :
#   1. visited set — si le noeud est déjà dans le dict, on l'a déjà cloné
#   2. lookup — pour relier les voisins du clone aux bonnes copies

#   Template (consignes)

#   Approche DFS récursive :
#   1. Cas de base : si node is None, retourner None
#   2. Si node est déjà dans le mapping → retourner le clone existant
#   3. Sinon : créer un nouveau noeud avec node.val, l'ajouter au mapping
#   4. Pour chaque voisin de node : appeler récursivement et ajouter le résultat aux voisins du clone
#   5. Retourner le clone

#   Classe Node :
#   class Node:
#       def __init__(self, val=0, neighbors=None):
#           self.val = val
#           self.neighbors = neighbors if neighbors is not None else []

#   Signature :
#   def cloneGraph(self, node: 'Node') -> 'Node':

#   Complexité cible

#   - Temps : O(N + E) — chaque noeud et chaque arête visités une fois
#   - Espace : O(N) — le mapping

#   Pièges à surveiller

#   - Ne pas oublier le cas node is None (graphe vide)
#   - Le mapping doit être initialisé en dehors de la récursion (attribut ou variable dans la closure)
#   - Ne pas confondre "le noeud est dans le mapping" avec "ses voisins sont tous traités" — le mapping se remplit avant de traiter les voisins (sinon boucle infinie sur les cycles)


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    def __repr__(self) -> str:
        if self.neighbors:
            return f'{self.val} → ({", ".join(str(v) for v in self.neighbors)})'
        else:
            return f'{self.val} → ()'
    
class Solution:
    
    
    def cloneGraph(self, node: Node) -> Node:
        mapping = {}
        def clone(node: Node) -> Node:
            if not node:
                return None
            if node in mapping:
                return mapping[node]
            else:
                new_node = Node(node.val)
                mapping[node] = new_node
            for neighbor in node.neighbors:
                new_node.neighbors.append(clone(neighbor))
            return new_node
        return clone(node)
    
        

node = Node(0, [Node(1), Node(2, [Node(3)])])
s = Solution()
new_node = s.cloneGraph(node)
print(new_node is not node)
print(new_node.neighbors[1] is not node.neighbors[1])

