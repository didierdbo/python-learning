from utility import utils
# Problème 1 — Easy : Binary Search (LeetCode 704)

#   ▎ Tableau nums trié en ordre croissant, et un target. Retourner l'index de target, ou -1 s'il n'existe pas.

#   ▎ Exemples :
#   ▎ - nums = [-1,0,3,5,9,12], target = 9 → 4
#   ▎ - nums = [-1,0,3,5,9,12], target = 2 → -1

#   Consignes :
#   1. Applique le template ci-dessus directement
#   2. Complexité cible : O(log n) temps, O(1) espace

@utils.print_result
def binary_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1

assert binary_search([-1,0,3,5,9,12], 9) == 4
assert binary_search([-1,0,3,5,9,12], 2) == -1


# Problème 2 — Medium : Search in Rotated Sorted Array (LeetCode 33)

#   ▎ Tableau nums trié en ordre croissant, puis roté à un pivot inconnu. Par exemple [0,1,2,4,5,6,7] roté à pivot 4 donne [4,5,6,7,0,1,2].
#   Pas de doublons.

#   ▎ Trouver l'index de target, ou -1. Doit tourner en O(log n).

#   ▎ Exemples :
#   ▎ - nums = [4,5,6,7,0,1,2], target = 0 → 4
#   ▎ - nums = [4,5,6,7,0,1,2], target = 3 → -1
#   ▎ - nums = [1], target = 0 → -1

#   Consignes :
#   1. Même base : left, right, mid
#   2. L'astuce : à chaque étape, une des deux moitiés est forcément triée. Détermine laquelle en comparant nums[left] et nums[mid]
#   3. Si la moitié gauche est triée (nums[left] <= nums[mid]) : vérifie si target est dans [nums[left], nums[mid]] → si oui, right = mid - 1,
#    sinon left = mid + 1
#   4. Sinon la moitié droite est triée : vérifie si target est dans [nums[mid], nums[right]] → si oui, left = mid + 1, sinon right = mid - 1
# #   5. Complexité cible : O(log n) temps, O(1) espace

@utils.print_result
def search_rotated_array(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        # si la moitié gauche est triée
        elif nums[left] <= nums[mid]:
            if target >= nums[left] and target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else: # sinon c'est la moitié droite qui est triée
            if target >= nums[mid] and target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

assert search_rotated_array([4,5,6,7,0,1,2], target = 0) == 4
assert search_rotated_array([4,5,6,7,0,1,2], target = 3) == -1
assert search_rotated_array([1], target = 0) == -1