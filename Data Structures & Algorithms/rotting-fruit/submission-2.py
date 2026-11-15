from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        minutes = 0
        q = deque()
        rows = len(grid)
        cols = len(grid[0])
        fresh_fruit_count = 0
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        # find all rotten fruit and track it
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col, minutes))
                elif grid[row][col] == 1:
                    fresh_fruit_count += 1
        
        # branch from each rotten fruit and update stopwatch
        while q and len(q) > 0:
            row, col, mins = q.popleft()
            minutes = max(minutes, mins)
            for dir in dirs:
                new_row = row + dir[0]
                new_col = col + dir[1]
                if 0<=new_row<rows and 0<=new_col<cols and grid[new_row][new_col] == 1:
                    grid[new_row][new_col] = 2
                    fresh_fruit_count -= 1
                    q.append((new_row, new_col, minutes+1))
        
        return minutes if fresh_fruit_count == 0 else -1


        