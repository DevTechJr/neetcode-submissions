class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        num_islands = 0
        visited = {}
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(row, col):
            visited[(row, col)] = True
            for dir in dirs:
                nr = row + dir[0]
                nc = col+ dir[1]
                if 0<=nr<rows and 0<=nc<cols and visited.get((nr,nc)) == None and grid[nr][nc] == "1":
                    dfs(nr, nc)


        for row in range(rows):
            for col in range(cols):
                # check if it exists in dict
                if visited.get((row,col)) == None and grid[row][col] == "1":
                    dfs(row, col)
                    num_islands+=1

        return num_islands