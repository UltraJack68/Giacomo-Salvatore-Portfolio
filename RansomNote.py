"""Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote."""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
            
        mag_dict = {}
        
        for char in magazine:
            mag_dict[char] = mag_dict.get(char, 0) + 1

        for char in ransomNote:
            if mag_dict.get(char, 0) == 0:
                return False
            
            mag_dict[char] -= 1
            
        return True