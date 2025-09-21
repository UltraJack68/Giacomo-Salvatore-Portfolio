"""You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6)."""

class Solution:
    def maximum69Number (self, num: int) -> int:
        num_list = list(str(num))
        for i in range(len(num_list)):
            if num_list[i] == "6":
                num_list[i] = "9"
                ans = "".join(num_list)
                return int(ans)
        
        return num