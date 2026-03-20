Pattern 4 : Stack / Queue.

Stack — le concept

Intuition : une pile (LIFO — Last In, First Out). On empile (append) et on dépile pop) par le sommet. Très utile quand on doit matcher
des éléments par paires (parenthèses, balises), ou quand on a besoin de "revenir en rrière" au dernier élément non traité.

Quand l'utiliser :
- Parenthèses/brackets à valider ou matcher
- "Prochain élément plus grand/petit" (monotonic stack)
- Évaluation d'expressions (postfix, calculatrice)
- Historique / undo (revenir au dernier état)

Template basique :
stack = []
for element in data:
    # Condition pour dépiler (traiter les éléments en attente)
    while stack and condition(stack[-1], element):
        stack.pop()
    stack.append(element)

En Python, une list fait office de stack : append() pour push, pop() pour pop, stack-1] pour peek.