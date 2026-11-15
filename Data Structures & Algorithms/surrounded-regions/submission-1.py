from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        safe = {}
        q = deque()
        rows = len(board)
        cols = len(board[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O" and (row == 0 or row == rows-1 or col == 0 or col == cols-1):
                    safe[(row, col)] = True
                    q.append((row, col))

        while q and len(q) > 0:
            row, col = q.popleft()
            for dir in dirs:
                new_row = row + dir[0]
                new_col = col + dir[1]
                if 0<=new_row<rows and 0<=new_col<cols and board[new_row][new_col] == "O" and safe.get((new_row, new_col)) == None:
                    safe[(new_row, new_col)] = True
                    q.append((new_row, new_col))
                
        # final sweep
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O" and safe.get((row,col)) == None:
                    board[row][col] = "X"
        return

        

