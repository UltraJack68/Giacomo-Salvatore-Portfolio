"""Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr. If there are duplicates in arr, count them separately."""

class Solution:
    def countElements(self, arr: List[int]) -> int:
        nums = set(arr)
        count = 0

        for value in arr:
            if (value + 1) in nums:
                count += 1
            else:
                continue
        
        return count