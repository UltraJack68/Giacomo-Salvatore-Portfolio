"""You are given an integer array nums of length n, and an integer array queries of length m.

Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements."""

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        #subsequence (gives choice for any subset of elements) != subarray (doesn't)
        
        nums.sort()
        ans = []

        for query in queries:
            count = 0
            
            for num in nums:
                if query >= num:
                    query -= num
                    count += 1
                else:
                    break
            ans.append(count)
        
        return ans