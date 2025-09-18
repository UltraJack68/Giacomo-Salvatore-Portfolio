"""Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negative_nums = [-x for x in nums]
        heapify(negative_nums)
        
        for _ in range(k):
            curr = heappop(negative_nums)
            
        return -curr