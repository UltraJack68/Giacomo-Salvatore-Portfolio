"""You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A"."""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_dict = {}
        count = 0
        
        for char in stones:
            stones_dict[char] = stones_dict.get(char, 0) + 1
        
        for char in jewels:
            count += stones_dict.get(char, 0)
            
        return count 