class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic = set()
        pacific = set()

        rows = len(heights)
        cols = len(heights[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(row, col, acc):
            acc.add((row, col))
            for dir in dirs:
                new_row = row + dir[0]
                new_col = col + dir[1]
                if 0<=new_row<rows and 0<=new_col<cols and heights[new_row][new_col] >= heights[row][col] and (new_row, new_col) not in acc:
                    dfs(new_row, new_col, acc)
        
        # pacific row
        for coord in range(cols):
            dfs(0, coord, pacific)
        
        # pacific col
        for coord in range(rows):
            dfs(coord, 0, pacific)
        
        # atlantic row
        for coord in range(cols):
            dfs(rows-1, coord, atlantic)
        
        # atlantic col
        for coord in range(rows):
            dfs(coord, cols-1, atlantic)
        
        # Find intersection and convert back to a list of lists if needed
        common_cells = pacific.intersection(atlantic)
        result = [[r, c] for r, c in common_cells]



        return result
