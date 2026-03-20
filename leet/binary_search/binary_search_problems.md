Pattern 5 : Binary Search.

  Binary Search — le concept

  Intuition : sur des données triées, au lieu de chercher en O(n), on coupe l'espace de recherche en deux à chaque étape → O(log n). On
  maintient left et right, on calcule mid, et on décide dans quelle moitié continuer.

  Quand l'utiliser :
  - Tableau trié — chercher un élément ou une position
  - "Trouver le minimum/maximum qui satisfait une condition" (binary search on answer)
  - Tout problème où on peut réduire l'espace de recherche de moitié

  Template classique :
  left, right = 0, len(nums) - 1
  while left <= right:
      mid = (left + right) // 2
      if nums[mid] == target:
          return mid
      elif nums[mid] < target:
          left = mid + 1
      else:
          right = mid - 1
  return -1  # pas trouvé

  Pièges classiques :
  - left <= right (pas <) sinon on rate le cas où l'élément est seul
  - mid = (left + right) // 2 — en Python pas de risque d'overflow, mais en Java/C++ on fait left + (right - left) // 2
  - Off-by-one sur mid + 1 / mid - 1 — ne jamais réinclure mid dans la recherche après l'avoir testé