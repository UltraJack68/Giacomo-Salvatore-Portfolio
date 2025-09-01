"""Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node."""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def minDepth(self, root: Optional[TreeNode]) -> int:    
        ans_set = set()

        def dfs(node, layer):
            if not node:
                return
            
            # leaf node
            if not node.left and not node.right:
                ans_set.add(layer)
                return

            if node.left:
                dfs(node.left, layer + 1)
            if node.right:
                dfs(node.right, layer + 1)

        dfs(root, 1)

        return min(ans_set) if ans_set else 0