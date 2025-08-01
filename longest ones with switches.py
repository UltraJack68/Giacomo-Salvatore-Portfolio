"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""




class solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        cuurmax = 0
        
        for lowerbound in range(len(nums)):
            upperbound = lowerbound + 1
            
            if nums[lowerbound] == 0:
                break
            
            while k > 0 and upperbound <= (len(nums) - 1):
                upperbound += 1
                if nums[upperbound] == 0:
                    k -= 1

            while k > 0 and lowerbound > 0:
                lowerbound -= 1
                k -= 1
                    
            if currmax < len(nums[lowerbound:upperbound]):
                currmax = len(nums[lowerbound:upperbound])

        return currmax