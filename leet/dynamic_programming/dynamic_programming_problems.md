Pattern 10 : Dynamic Programming

Intuition : Résoudre des sous-problèmes et stocker les résultats pour viter les recalculs. Deux approches : top-down (memoization) ou
bottom-up (tabulation).

Quand l'utiliser :
- Récurrence + chevauchement de sous-problèmes (fib, coins change)
- Optimisation de partition (knapsack, cut rod)
- Comptage de chemins / combinaisons
- Alignement de séquences (LCS, edit distance)

Template Python :
# Top-down (memoization) — récursif
memo = {}
def dp(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = dp(n-1) + dp(n-2)
    return memo[n]

# Bottom-up (tabulation) — itératif
def dp(n):
    if n <= 1:
        return n
    dp_array = [0] * (n + 1)
    dp_array[1] = 1
    for i in range(2, n + 1):
        dp_array[i] = dp_array[i-1] + dp_array[i-2]
    return dp_array[n]