"""You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph."""

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(value):
            seen.add(value)
            for num in connections[value]:
                if num in seen:
                    continue
                if not dfs(num):
                    return False
            return True

        ans = 0    
        seen = set()
        connections = defaultdict(list)
        
        for x, y in edges:
            connections[x].append(y)
            connections[y].append(x)
            
        for num in range(n):
            if num in seen:
                continue
            if dfs(num):
                ans += 1
                
        return ans