# Exercice 1 — Warm-up
# Given an integer array nums, return True if any value appears at least twice, false if every element is distinct.
# nums = [1, 2, 3, 1] -> True
# nums = [1, 2, 3, 4] -> False
def has_duplicates(nums: list) -> bool:
    set_of_uniques = {x for x in nums}
    return not len(nums) == len(set_of_uniques)

print(f"has_duplicates: { has_duplicates([1, 2, 3, 4])}")

# "Et si la liste fait 10 millions d'éléments, tu veux vraiment construire le set entier ?"
def has_duplicates_big_list(nums: list) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Exercice 2 - Un cran au dessus
# Given two strings s and t, determine if t is an anagram of s.
# (same letter, same frequencies, different order)
from collections import Counter, defaultdict
def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
#  "We could also sort both strings and compare — O(n log n) — but Counter gives us O(n)."
print(f"is_anagram- anagram, nagaram: {is_anagram("anagram", "nagaram")}")

# Exercise 3 - Le vrai challenge Hash Map
# Given an array of strings, group the anagrams together.
# Input:  ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

def group_anagrams(words: list[str]) -> list[list[str]]:
    anagram_map = defaultdict(list)
    for word in words:
        key = tuple(sorted(word))
        anagram_map[key].append(word)
    return list(anagram_map.values())
print(f"group_anagrams: {group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])}")
