"""
IDEA of sliding window:

function fn(arr):
    left = 0
    for (int right = 0; right < arr.length; right++):
        Do some logic to "add" element at arr[right] to window

        while WINDOW_IS_INVALID:
            Do some logic to "remove" element at arr[left] from window
            left++

        Do some logic to update the answer"""


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        
        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, curr_sum)
        
        return max_sum / k
        
