# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def LongestBranchOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        arr = [root.val]
        ans = 1
        def dfs(root):
            nonlocal ans
            if root == None:
                return
            
            if root.left:
                arr.append(root.left.val)
                if ans < len(arr) - 1:
                    ans = len(arr) - 1
                return dfs(root.left)
                arr.pop()
            
            if root.right:
                arr.append(root.right.val)
                if ans < len(arr) - 1:
                    ans = len(arr) - 1
                return dfs(root.right)
                arr.pop
            
            return 
        dfs(root)
        return ans