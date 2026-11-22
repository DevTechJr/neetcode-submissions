class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        cache = {}
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows = len(matrix)
        cols = len(matrix[0])

        def dfs(r, c):
            if(r,c) in cache:
                return cache[(r, c)]
            
            temp = 1
            for dr, dc in directions:
                nr = dr + r
                nc = dc + c
                if 0<=nr<rows and 0<=nc<cols and matrix[nr][nc] > matrix[r][c]:
                    temp = max(temp, 1+ dfs(nr, nc)) 
            
            cache[(r, c)] = temp
            return cache[(r, c)]

        best = 0
        for row_ind in range(len(matrix)):
            for col_ind in range(len(matrix[0])):
                best = max(best, dfs(row_ind, col_ind))
        
        return best