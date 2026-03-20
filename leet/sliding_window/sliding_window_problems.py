from utility import utils
# Problème 1 — Easy : Best Time to Buy and Sell Stock (LeetCode 121)
#
# ▎ Tableau prices où prices[i] = prix du jour i. Tu peux acheter un jour et vendre un jour ultérieur. Retourner le profit max. Si aucun
# profit possible, retourner 0.
#
# ▎ Exemple : prices = [7,1,5,3,6,4] → output 5 (acheter à 1, vendre à 6)
#
# Consignes :
# 1. Maintiens un pointeur left (jour d'achat) et parcours avec right (jour de vente)
# 2. Si prices[right] < prices[left] → ce nouveau prix est un meilleur achat, déplace left à right
# 3. Sinon, calcule le profit et mets à jour le max
# 4. Complexité cible : O(n) temps, O(1) espace


@utils.print_result
def best_buy_sell_days(prices: list[int]) -> int:
    best_buy_day = 0
    best_profit = 0
    for i, right in enumerate(prices):
        if right < prices[best_buy_day]:
            best_buy_day = i
        else:
            best_profit = max(best_profit, right - prices[best_buy_day])
    return best_profit

prices = [7,1,5,3,6,4]
best_buy_sell_days(prices)

# Problème 2 — Medium : Longest Substring Without Repeating Characters (LeetCode 3)

# ▎ String s. Retourner la longueur de la plus longue substring sans caractère répété.

# ▎ Exemples :
# ▎ - "abcabcbb" → 3 ("abc")
# ▎ - "bbbbb" → 1 ("b")
# ▎ - "pwwkew" → 3 ("wke")

# Consignes :
# 1. Fenêtre variable : left et right
# 2. Utilise un set (ou un dict) pour tracker les caractères présents dans la fenêtre
# 3. Quand s[right] est déjà dans le set → shrink depuis left (retirer s[left] du set, left += 1) jusqu'à ce que le doublon disparaisse
# 4. À chaque pas, mettre à jour max_len = max(max_len, right - left + 1)
# 5. Complexité cible : O(n) temps, O(min(n, alphabet)) espace

@utils.print_result
def longest_substring_no_repeat(s: str) -> int:
    longest = 0
    left = 0
    state = set()
    for right in range(len(s)):
        while s[right] in state:
            state.discard(s[left])                       
            left += 1
        state.add(s[right])
        longest = max(longest, right - left + 1)
    return longest

longest_substring_no_repeat("abcabcbb")
longest_substring_no_repeat("bbbbb")
longest_substring_no_repeat("pwwkew")


class Solution:
    @utils.print_result
    def spiral_order(self, matrix):
        result = []
        while matrix:
            result += matrix.pop(0)
            if matrix and matrix[0]:  
                for row in matrix:
                    result.append(row.pop())                    
            if matrix:
                result += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))
        return result

matrix = [
    [0,1,2],
    [3,4,5],
    [6,7,8]
]
print(matrix.pop(0))
for row in matrix:        
    print(row.pop())
print(matrix.pop()[::-1])
print(matrix[::-1])
for row in matrix[::-1]:
    print(row.pop(0))
print(matrix)

s = Solution()
#s.spiral_order(matrix=matrix)
        


