class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        new_list = []
        
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = -nums[i]
                
        while left <= right:
            if nums[left] >= nums[right]:
                new_list.insert(0, nums[left]**2)
                left += 1
            else:
                new_list.insert(0, nums[right]**2)
                right -= 1

                
        return new_list