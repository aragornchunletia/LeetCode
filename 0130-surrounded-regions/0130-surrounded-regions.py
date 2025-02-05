from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:  
            return  

        M, N = len(board), len(board[0])
        starts = []

        # Mark border 'O's and collect their positions
        for i in [0, M-1]:
            for j in range(N):
                if board[i][j] == "O":
                    board[i][j] = "#"
                    starts.append((i, j))

        for j in [0, N-1]:
            for i in range(M):
                if board[i][j] == "O":
                    board[i][j] = "#"
                    starts.append((i, j))

        # BFS to mark connected 'O's
        while starts:
            i, j = starts.pop()
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < M and 0 <= y < N and board[x][y] == "O":
                    board[x][y] = "#"
                    starts.append((x, y))

        # Convert all 'O's to 'X' and '#' back to 'O'
        for i in range(M):
            for j in range(N):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
