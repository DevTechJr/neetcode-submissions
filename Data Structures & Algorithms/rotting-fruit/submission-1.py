from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        counter = 0
        directions = [(1,0), (-1, 0), (0, 1), (0,-1)]

        def bfs(row, col):
            pass
        
        rows = len(grid)
        cols = len(grid[0])

        q = deque()
        fresh_fruit = 0
        minutes = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
                elif grid[row][col] == 1:
                    fresh_fruit += 1

        if fresh_fruit == 0:
            return 0

        while q and len(q) > 0:
            for _ in range(len(q)):
                sr, sc = q.popleft()
                for dir in directions:
                    nr, nc = sr + dir[0], sc + dir[1]
                    if 0<= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        fresh_fruit -= 1
                        
                        q.append((nr, nc))
                        grid[nr][nc] = 2
            minutes += 1
            if fresh_fruit == 0:
                break
                
        
        return minutes if fresh_fruit == 0 else -1



