from utility import utils
# Problème Easy — Two Sum
# Etant donné un tableau de nums et un entier target, retourner les indices des deux éléments dont la somme vaut target.
# Chaque input a exactement une solution. Tu ne peux pas utiliser le même élément deux fois.
# Exemple: nums = [2, 7, 11, 15], target = 9 -> [0, 1]
@utils.print_result
def two_sum(nums, target):
    seen = {}
    for i,num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None
two_sum([2, 7, 11, 15], 9)

# Debrief :
# - Un seul passage -> O(n) temps, O(n) espace
# - seen stocke valeur -> index, lookup du complément en O(1)
# - enumerate bien utilisé pour avoir l'index
# - Le return None à la fin est un bon reflexe défensif
# Rien à redire, c'est exactement le pattern canonique

# Problème Medium - Group Anagrams
# Etant donné un tableau de strings strs, regrouper les anagrammes ensemble.
# Tu peux retourner les groupes dans n'importe quel ordre.
# Exemple: strs = ["eat", "tea", "tan", "ate", "nat", "bat"] -> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

from collections import Counter, defaultdict
@utils.print_result
def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    for word in strs:
        key:str = str(sorted(word))
        groups[key].append(word)
    return list(groups.values())
group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

# Debrief :
# Complexité : O(n * k log k) où k = longueur max d'un mot (à cause du sorted).
# L'approche O(n * k) utiliserait un comptage de lettres (tuple(Counter(word))) comme clé au lieu de trier, mais en entretien les deux passent
from collections import Counter, defaultdict
@utils.print_result
def group_anagrams_optimized(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    for word in strs:
        # key = tuple(sorted(Counter(word).items()))
        counts = [0] * 26
        for c in word:
            counts[ord(c) - ord('a')] += 1
        key = tuple(counts)
        groups[key].append(word)
    return list(groups.values())
group_anagrams_optimized(["eat", "tea", "tan", "ate", "nat", "bat"])

print(tuple(sorted(Counter("tee").items())))
print(tuple(sorted(Counter("ete").items())))