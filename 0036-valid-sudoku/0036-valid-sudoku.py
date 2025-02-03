class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = len(board)
        rowSet = [set() for _ in range(N)]
        colSet = [set() for _ in range(N)]
        subSquare = [set() for _ in range(N)]


        for i in range(N):
            for j in range(N):
                val = board[i][j]
                subSq = 3 * (i//3) + j//3
                if val == ".":
                    continue
                if val in rowSet[i] or val in colSet[j] or val in subSquare[subSq]:
                    return False
                rowSet[i].add(val)
                colSet[j].add(val)
                subSquare[subSq].add(val)

        return True

        