"""Given the root of a binary tree, return the sum of values of its deepest leaves."""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        
        while len(queue) > 0:
            curr_level = len(queue)
            
            curr = 0
            for index in queue:
                curr += index.val
                
            
            for _ in range(curr_level):
                node = queue.popleft()
            
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
        return curr