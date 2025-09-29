"""Given an integer array nums, return the largest integer that only occurs once. If no integer occurs once, return -1."""

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        numbers = dict()
        answer = -1
        
        for index in range(len(nums)):
            if nums[index] not in numbers:
                numbers[nums[index]] = 1
            else:
                numbers[nums[index]] += 1
        
        for key in numbers:
            if numbers[key] > 1:
                continue
            if key > answer:
                answer = key
        
        return answer           