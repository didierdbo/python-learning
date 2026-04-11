from utility import utils
# Easy — Maximum Depth of Binary Tree (LeetCode 104)

#   ▎ Étant donné la racine d'un arbre binaire, retourner sa profondeur maximale.
#   ▎ La profondeur max = nombre de noeuds sur le plus long chemin racine → feuille.

#   Consignes :
#   1. C'est un problème DFS classique, récursif
#   2. Cas de base : noeud None → profondeur 0
#   3. La profondeur d'un noeud = 1 + max(profondeur gauche, profondeur droite)
#   4. Une seule ligne de return suffit

#   Implémente maxDepth(self, root: TreeNode) -> int puis dis-moi quand tu as fini, je te donnerai le medium.
class TreeNode:
      def __init__(self, val=0, left=None, right=None):
          self.val = val
          self.left = left
          self.right = right
        
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
             return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5))
s = Solution()
print(s.maxDepth(root=root))


# Medium — Binary Tree Level Order Traversal (LeetCode 102)

#   ▎ Étant donné la racine d'un arbre binaire, retourner le parcours par niveau (level order) sous forme de liste de listes.
#   ▎ Exemple : [3, 9, 20, None, None, 15, 7] → [[3], [9, 20], [15, 7]]

#   Consignes :
#   1. C'est un problème BFS classique — utilise collections.deque
#   2. Initialise la queue avec root, puis boucle tant que la queue n'est pas vide
#   3. À chaque itération : capture len(queue) = nombre de noeuds du niveau courant
#   4. Boucle interne sur ce nombre : popleft(), ajoute la valeur à une liste temporaire du niveau, et enqueue les enfants non-None
#   5. Ajoute la liste du niveau au résultat final
#   6. Attention au cas root is None → retourner []

#   Implémente levelOrder(self, root: TreeNode) -> list[list[int]].
from collections import deque

class SolutionLevelOrder:
     def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
          if not root:
               return []
          queue = deque([root])          
          tree_path = []
          while queue:               
                nb_nodes = len(queue)
                level_path = []
                for _ in range(nb_nodes):
                    node = queue.popleft()
                    level_path.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                tree_path.append(level_path)
          return tree_path
     
s = SolutionLevelOrder()
print(s.levelOrder(root=root))