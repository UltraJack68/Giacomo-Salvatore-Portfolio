"""Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between)."""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root])
        ans = []
        even_layer = True
        
        if not root:
            return []
        
        while len(queue) > 0:
            left = 0
            right = 0
            dummy = []
            curr = []
            for _ in range(len(queue)):
                node = queue.popleft()
                curr.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if even_layer:
                ans.append(curr)
                even_layer = False
            else:                       #reversing arr with two pointer O(n)
                right = len(curr) - 1 
                while right > left:
                    curr[left], curr[right] = curr[right], curr[left]
                    left += 1
                    right -= 1
                ans.append(curr)
                even_layer = True
        return ans
                