class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        best_area = 0
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(row_ind, col_ind):
            area = 1
            grid[row_ind][col_ind] = "#"
            for dir in dirs:
                new_row = row_ind + dir[0]
                new_col = col_ind + dir[1]

                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                    area += dfs(new_row, new_col)
                    
            return area
            
        
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    size = dfs(row, col)
                    best_area = max(best_area, size)
        
        return best_area