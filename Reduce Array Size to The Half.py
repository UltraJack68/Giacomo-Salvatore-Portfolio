"""You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed."""

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        goal = len(arr) / 2
        ans = 0
        freq_map = Counter(arr)

        freq_list = list(freq_map.values())
        freq_list.sort()
        
        removed = 0
        while removed < goal:
            removed += freq_list.pop()
            ans += 1

        return ans