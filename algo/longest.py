



def longest_substring_with_unique_chars(s: str) -> int:
    max_len = 0
    prev_indexes = {}
    left = right = 0
    while right < len(s):
        if (s[right] in prev_indexes and prev_indexes[s[right]] >= left):
            left = prev_indexes[s[right]] + 1
        max_len = max(max_len , right - left + 1)
        prev_indexes[s[right]] = right
        right += 1
    return max_len


def longest_substring_without_repeating(s: str) -> int:
    max_len = 0
    last_seen = {}
    left = 0
    
    for right, char in enumerate(s):
        #print(f"{right}->{char}")
        if char in last_seen and last_seen[char] >= left:
            #print(s[left:right])
            left = last_seen[char] + 1
        max_len = max(max_len, right - left + 1)
        last_seen[char] = right
        #print(f"{s[left:right]} {last_seen}")
    
    return max_len




#print(longest_substring_without_repeating("abcabcbb"))
#print(longest_substring_without_repeating("bbbbb"))
print(longest_substring_without_repeating("pwwkew"))

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: TreeNode):
    if not root:
        return []
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    
    return result