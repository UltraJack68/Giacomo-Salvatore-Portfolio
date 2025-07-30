class Solution:
    def reverseString(self, s: List[str]):
        
        left = 0
        right = len(s) - 1
        letter = 'x'
        
        while left < right:
            letter = s[left]
            s[left] = s[right]
            s[right] = letter
            left = left + 1
            right = right - 1
            
        
        
        
        """
        Do not return anything, modify s in-place instead.