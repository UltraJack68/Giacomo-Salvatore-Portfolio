"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""




"""class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        switches = 0
        currmax = 0
        j = k
        
        for lowerbound in range(len(nums)):
            upperbound = lowerbound + 1
            j = k
            switches = 0

            if nums[lowerbound] == 0:
                continue
            
            while j > 0 and upperbound < (len(nums) - 1):
                upperbound += 1
                if nums[upperbound] == 0:
                    j -= 1
                    switches += 1
            while j > 0 and lowerbound > 0:
                    lowerbound -= 1
                    j -= 1
                    switches +=1    
          
            if currmax < len(nums[lowerbound:upperbound]):
                currmax = len(nums[lowerbound:upperbound])

        return currmax"""
    
""" while j > 0 and lowerbound > 0:
lowerbound -= 1
j -= 1
switches +=1"""

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1

            while k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len