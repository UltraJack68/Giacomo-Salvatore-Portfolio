"""Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1."""

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum = 0
        first_occurrence = {0: -1}
        max_len = 0

        for i, num in enumerate(nums):
            
            prefix_sum += 1 if num == 1 else -1

            if prefix_sum in first_occurrence:
                max_len = max(max_len, i - first_occurrence[prefix_sum])
            else:
                first_occurrence[prefix_sum] = i

        return max_len