from utility import utils
# Problème Easy - Valid Palindrome
# Etant donné une string s, déterminer si c'est un palindrome en ne considérant que les caractères alphanumériques et en ignorant la casse.
# Example : "A man, a plan, a canal: Panama" -> True
# Example : "race a car" -> False

@utils.print_result
def valid_palindromes(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

valid_palindromes("A man, a plan, a canal: Panama")
valid_palindromes("race a car")

# Problème Medium - Container With Most Water
# Etant donné un tableau height de n entiers, chaque élément représente une barre verticale à la position i. Trouver deux barres qui, avec l'axe x, forment un conteneur contenant le plus d'eau. Retourner la quantité maximale d'eau.
# Example : height = [1, 8, 6, 2, 5, 4, 8, 3, 7] -> 49

@utils.print_result
def container_with_most_water(height: list[int]) -> int:
    volume = 0
    left, right = 0, len(height) - 1
    while left < right:
        volume = max(volume, min(height[left], height[right]) * (right - left))
        if height[left] < height[right]:
            left += 1
        elif height[right] < height[left]:
            right -= 1
        else:
            left += 1
    return volume

container_with_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7])

# Débrief Two Pointers :
# Palindromes : pointeurs opposés qui sautent les non-alnum, O(1) espace (pas de copie)
# Containers : on déplace le pointeur de la hauteur la plus petite car c'est le facteur limitant
# Piège classique : confondre indices et valeurs
