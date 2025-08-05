"""A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise."""

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        used_letters = set(sentence)
        for letter in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]:
            if letter not in used_letters:
                return False
            
        return True