class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(row_ind, col_ind):
            grid[row_ind][col_ind] = '#'
            for direction in directions:
                temp_row = direction[0] + row_ind
                temp_col = direction[1] + col_ind

                if (0<=temp_row < rows) and (0<=temp_col < cols) and grid[temp_row][temp_col] == "1":
                    dfs(temp_row, temp_col)

            
        
        counter = 0
        
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == "1":
                    counter += 1
                    dfs(row, col)
        return counter