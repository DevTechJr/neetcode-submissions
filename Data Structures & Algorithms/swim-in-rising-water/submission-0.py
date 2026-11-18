class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()

        minHeap = [(grid[0][0], 0, 0)]
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        while minHeap:

            elevation, row, col = heapq.heappop(minHeap)
            if row == n-1 and col == n-1:
                return elevation
            
            if (row, col) in visited:
                continue
            
            visited.add((row, col))
            
            for dir in dirs:
                new_row = row + dir[0]
                new_col = col + dir[1]
                if 0<=new_row<n and 0<=new_col<n and (new_row, new_col) not in visited:
                    
                    new_max = max(elevation, grid[new_row][new_col])
                    heapq.heappush(minHeap, (new_max, new_row, new_col))
        return elevation
            