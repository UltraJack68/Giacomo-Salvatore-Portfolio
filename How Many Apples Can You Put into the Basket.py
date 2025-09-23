"""You have some apples and a basket that can carry up to 5000 units of weight.

Given an integer array weight where weight[i] is the weight of the ith apple, return the maximum number of apples you can put in the basket."""

class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        heapify(weight)
        basket_max = 5000
        ans = 0
        
        while basket_max >= 0 and weight:
            basket_max -= heappop(weight)
            ans += 1
            
        if basket_max < 0:
            ans -= 1
            
        return ans