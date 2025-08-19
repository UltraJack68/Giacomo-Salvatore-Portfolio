"""Given a string s, find the length of the longest substring without duplicate characters."""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:       
        seen = {} 
        maxLen = 0
        l = 0      
        
        for r in range(len(s)):
            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]] + 1
            seen[s[r]] = r
            maxLen = max(maxLen, r - l + 1)
        
        return maxLen
        