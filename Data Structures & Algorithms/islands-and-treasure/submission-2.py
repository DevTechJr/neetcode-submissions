from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        steps = 0
        dirs = [(1,0), (-1,0),(0,1),(0,-1)]
        visited = {}

        # track all locations of existing treasures
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    visited[(row, col)] = True
                    q.append((row, col, steps))
        
        while q and len(q):
            row, col, steps = q.popleft()
            for dir in dirs:
                new_row = row + dir[0]
                new_col = col + dir[1]
                if 0<=new_row<rows and 0<=new_col<cols and grid[new_row][new_col] != -1 and grid[new_row][new_col] > steps and visited.get((new_row, new_col)) == None:
                    visited[(new_row, new_col)] = True
                    grid[new_row][new_col] = steps+1
                    q.append((new_row, new_col, steps+1))
        return

        