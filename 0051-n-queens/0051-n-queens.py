from typing import List
"""
This was the simplest hard problem,
we need to fill the board row by row,
hence no need to check for rows as we are filling the board row by row
only upper Left and upper Right diagonals with columns to be considered for checking
valid cell.
and then recurse the hell out of it with backtracking.
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        colSet = [False for _ in range(n)]
        
        board = [["." for _ in range(n)] for _ in range(n)]
        res = []

        def checkDiag(row , col):

            for i in range(row):
                if col - row + i >= 0 and board[i][col - row + i] == "Q":
                    return False
                if col + row - i < n and board[i][col + row - i] == "Q":
                    return False

            return True


        def solve(row,remainingQueens):
     
            if remainingQueens == 0 :
                res.append(["".join(row) for row in board])
                return

            if row >= n:
                return

            for col in range(n):
                if not colSet[col] and checkDiag(row,col):
                    board[row][col] = "Q"
                    colSet[col] = True
                    solve(row + 1 , remainingQueens - 1)
                    board[row][col] = "."
                    colSet[col] = False
                    
        
        solve(0 , n)
        return res
