class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        best_area = 0
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = {}

    
        def dfs(row, col):
            visited[(row, col)] = True
            area = 1
            for dir in dirs:
                nr = row + dir[0]
                nc = col + dir[1]
                if 0<=nr<rows and 0<=nc<cols and grid[nr][nc] == 1 and visited.get((nr, nc)) == None:
                    area += dfs(nr, nc)

            return area


        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and visited.get((row, col)) == None:
                    size = dfs(row, col)
                    best_area = max(best_area, size)
        
        return best_area