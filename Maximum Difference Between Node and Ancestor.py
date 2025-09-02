"""Given the root of a binary tree, find the maximum value v for which there exist different nodes a and b where v = |a.val - b.val| and a is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b or any child of a is an ancestor of b."""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        Max = [root.val]
        Min = [root.val]
        ans = set()
        
        def dfs(root):
            if root == None:
                return
            
            if root.left != None:
                if Min[-1] > root.left.val:
                    Min.append(root.left.val)
                if Max[-1] < root.left.val:
                    Max.append(root.left.val)
                ans.add(Max[-1] - Min[-1])
                
                dfs(root.left)
                if Max[-1] == root.left.val and Max[-1] != root.val:
                    Max.pop()
                if Min[-1] == root.left.val and Min[-1] != root.val:
                    Min.pop()
                
            
            if root.right != None:
                if Min[-1] > root.right.val:
                    Min.append(root.right.val)
                if Max[-1] < root.right.val:
                    Max.append(root.right.val)
                ans.add(Max[-1] - Min[-1])
                
                dfs(root.right)
                if Max[-1] == root.right.val and Max[-1] != root.val:
                    Max.pop()
                if Min[-1] == root.right.val and Min[-1] != root.val:
                    Min.pop()
                
                
                dfs(root.right)
               
            return
        
        dfs(root) 
        return max(ans)