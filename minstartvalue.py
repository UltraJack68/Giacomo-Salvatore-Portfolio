"""Given an array of integers nums, you start with an initial positive value startValue.

In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).

Return the minimum positive value of startValue such that the step by step sum is never less than 1."""

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        
        for index in range(1, len(nums)):
            prefix.append(nums[index] + prefix[len(prefix)-1])
            
        minPrefix = min(prefix)
        
        if minPrefix >= 1:
            return 1
        
        else:
            return 1 - minPrefix