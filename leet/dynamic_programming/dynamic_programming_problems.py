# Problème 1 (easy) : Climbing Stairs

# Tu es au bas d'un escalier avec n marches. À chaque étape, tu peux monter 1 ou 2 marches. Combien de façons différentes pour atteindre
# le sommet ?

# Exemples :
# n = 2 → 2  (1+1, 2)
# n = 3 → 3  (1+1+1, 1+2, 2+1)
# n = 4 → 5

# Contraintes : 1 ≤ n ≤ 45
from utility import utils
@utils.print_result
def count_climbing_paths(steps):
    memo = {}
    def dp(n):
        if n in memo:
            return memo[n]
        if n <= 1:
            return 1
        memo[n] = dp(n-1) + dp(n-2)           
        return memo[n]
    return dp(steps)

count_climbing_paths(1)
count_climbing_paths(2)
count_climbing_paths(3)
count_climbing_paths(4)
count_climbing_paths(5)

@utils.print_result
def count_climbing_paths_bottom_up(steps):
    def dp(n):
        if n <= 1:
            return n
        dp_array = [0] * (n + 1)
        dp_array[0] = 1
        dp_array[1] = 1

        for i in range(2, n + 1):
            dp_array[i] = dp_array[i-1] + dp_array[i-2]
        return dp_array[n]
    return dp(steps)

count_climbing_paths_bottom_up(1)
count_climbing_paths_bottom_up(2)
count_climbing_paths_bottom_up(3)
count_climbing_paths_bottom_up(4)
count_climbing_paths_bottom_up(5)
