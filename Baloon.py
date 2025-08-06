"""Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed."""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        listed = list(text)
        counted = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}
        answer = 0
        
        for index in range(len(listed)):
            if listed[index] not in counted:
                counted[listed[index]] = 1
            else:
                counted[listed[index]] += 1
        
        while counted["b"] > 0 and counted["a"] > 0 and counted["l"] > 1 and counted["o"] > 1 and counted["n"] > 0:
            answer += 1
            for x in ["b", "a", "l", "l", "o", "o", "n"]:
                counted[x] -= 1

        return answer        


        
