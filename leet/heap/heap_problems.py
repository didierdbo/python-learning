from utility import utils
import heapq
# Problème 1 (easy) : Kth Largest Element in an Array

#   Trouver le k-ième plus grand élément d'une liste.

#   Exemples :
#   nums = [3, 2, 1, 5, 6, 4], k = 2 → 5
#   nums = [1], k = 1 → 1

#   Contraintes : 1 ≤ k ≤ n ≤ 10⁵

#   À toi de jouer — pas de code, juste ta solution (logique + complexité).
@utils.print_result
def findKthLargest(nums, k):
    heap = [-x for x in nums]
    heapq.heapify(heap)

    for _ in range(k - 1):
        heapq.heappop(heap)

    return -heapq.heappop(heap)

findKthLargest([3, 2, 1, 5, 6, 4], 2) # findKthLargest : 5
findKthLargest([1],1) # findKthLargest : 1



@utils.print_result
def findKthLargestOptimized(nums, k):
    heap = nums[:k+1]
    heapq.heapify(heap)
    min = heapq.heappop(heap)
    
    if len(nums) == k:
         return min
     
    for i in range(k, len(nums)):
        if nums[i] > min:
                min = heapq.heappushpop(heap, nums[i])        
    return heapq.heappop(heap)


findKthLargestOptimized([3, 2, 1, 5, 6, 4], 2) # findKthLargestOptimized : 5
findKthLargestOptimized([1],1) # findKthLargestOptimized : 1
findKthLargestOptimized([1,3],1) # findKthLargestOptimized : 3
findKthLargestOptimized([1,3],2) # findKthLargestOptimized : 1




            


