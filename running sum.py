"""Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums."""


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        
        for index in range(1, len(nums)):
            prefix.append(nums[index] + prefix[len(prefix) - 1])
            
        return prefix
            