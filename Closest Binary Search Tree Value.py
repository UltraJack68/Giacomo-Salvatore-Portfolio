"""Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. If there are multiple answers, print the smallest."""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if root is None:
            return
        
        best = root.val
        best_diff = abs(root.val - target)
        node = root
        eps = 1e-12
        
        while node:
            val = node.val
            diff = abs(val - target)
            
            if diff + eps < best_diff or (abs(diff - best_diff) <= eps and val < best):
                best = val
                best_diff = diff
            
            if diff <= eps:
                return val

            if target < val:
                node = node.left
            else:
                node = node.right
        
        return best
        