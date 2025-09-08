"""There is an undirected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree. You are also given an integer array restricted which represents restricted nodes.

Return the maximum number of nodes you can reach from node 0 without visiting a restricted node.

Note that node 0 will not be a restricted node."""

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:

        def dfs(Input):
            nonlocal ans
            if Input in seen:
                return
            ans += 1
            seen.add(Input)
            for value in connections[Input]:
                dfs(value)
            return ans
    
        ans = 0    
        seen = set()
        restricted_set = set(restricted)
        connections = defaultdict(list)
        
        for x, y in edges:
            if x in restricted_set or y in restricted_set:
                continue
            connections[x].append(y)
            connections[y].append(x)
            
        return dfs(0)