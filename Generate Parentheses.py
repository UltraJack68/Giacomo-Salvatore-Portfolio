"""Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses."""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(path, openable, closable):
            if openable == 0 and closable == 0:
                ans.append("".join(path))
            if openable > 0:
                path.append("(")
                backtrack(path, openable - 1, closable + 1)
                path.pop()
            if closable > 0:
                path.append(")")
                backtrack(path, openable, closable - 1)
                path.pop()
                
        ans = []
        backtrack([], n, 0)
    
        return ans