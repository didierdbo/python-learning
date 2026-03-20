from utility import utils
# Problème 1 — Easy : Valid Parentheses (LeetCode 20)

#   ▎ String s contenant uniquement (, ), {, }, [, ]. Déterminer si la string est valide.

#   ▎ Règles : chaque parenthèse ouvrante doit être fermée par le même type, dans le bon ordre.

#   ▎ Exemples :
#   ▎ - "()" → True
#   ▎ - "()[]{}" → True
#   ▎ - "(]" → False
#   ▎ - "([)]" → False
#   ▎ - "{[]}" → True

#   Consignes :
#   1. Parcours chaque caractère
#   2. Si c'est une ouvrante → push sur la stack
#   3. Si c'est une fermante → pop de la stack et vérifie que ça matche (attention : stack vide = False)
#   4. À la fin, la stack doit être vide
#   5. Astuce : un dict qui mappe fermante → ouvrante simplifie le matching
#   6. Complexité cible : O(n) temps, O(n) espace

@utils.print_result
def valid_parentheses(s: str) -> bool:
    matches = {")": "(", "}": "{", "]": "["}
    stack = []
    for c in s:
        if not c in matches:
            stack.append(c)
        elif stack and stack[-1] == matches[c]:
            stack.pop()
        else:
            return False
    return len(stack) == 0
valid_parentheses("()")
valid_parentheses("()[]{}")
valid_parentheses("(]")
valid_parentheses("([)]")
valid_parentheses("{[]}")
valid_parentheses("()(")



# Problème 2 — Medium : Daily Temperatures (LeetCode 739)

#   ▎ Tableau temperatures de températures quotidiennes. Pour chaque jour, retourner le nombre de jours à attendre pour une température plus
#   chaude. Si aucun jour futur n'est plus chaud, mettre 0.

#   ▎ Exemple : [73,74,75,71,69,72,76,73] → [1,1,4,2,1,1,0,0]

#   C'est un cas classique de monotonic stack (stack décroissante).
@utils.print_result
def daily_temperatures(t: list[int]) -> list[int]:
    result = [0] * len(t)
    stack = []
    for i in range(len(t)):
        while stack and t[i] > t[stack[-1]]:
            j = stack.pop()
            result[j] = i - j
        stack.append(i)
    return result

daily_temperatures([73,74,75,71,69,72,76,73])