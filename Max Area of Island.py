"""You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0."""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == 1
        
        def dfs(row, col):
            nonlocal curr
            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    curr += 1
                    seen.add((next_row, next_col))
                    dfs(next_row, next_col)
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        seen = set()
        ans = 0
        curr = 0
        m = len(grid)
        n = len(grid[0])
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                curr = 0
                if (row, col) in seen:
                    continue
                if grid[row][col] == 1:
                    seen.add((row, col))
                    curr += 1
                    dfs(row, col)
                ans = max(ans, curr)
                
        return ans