"""You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists."""

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and maze[row][col] == "." and (row, col) not in seen

        m, n = len(maze), len(maze[0])
        seen = {(entrance[0], entrance[1])}
        queue = deque([(entrance[0], entrance[1])])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        ans = 0

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if (r in (0, m-1) or c in (0, n-1)) and (r, c) != (entrance[0], entrance[1]):
                    return ans
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if valid(nr, nc):
                        seen.add((nr, nc))
                        queue.append((nr, nc))
            ans += 1
        
        return -1
                       