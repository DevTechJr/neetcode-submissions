
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return
            
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        
        # 1. Add all treasure chests (0s) to the queue as our starting points
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        # 2. Perform Multi-Source BFS outward from all treasures simultaneously
        while q:
            r, c = q.popleft()
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                
                # Check boundaries and ensure the cell is an empty room 
                # (unvisited empty rooms are typically initialized to a large value like 2^31 - 1 or positive numbers)
                # We update it only if the new path is shorter than its current value.
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > grid[r][c] + 1:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc))

