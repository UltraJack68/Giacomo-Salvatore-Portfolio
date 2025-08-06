"""Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1."""
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        numbers = dict(nums)

