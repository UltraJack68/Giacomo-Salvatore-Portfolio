"""Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array."""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numbers = set(nums)

        for value in range(len(nums) + 1):
            if value in numbers:
                continue
            else:
                return value