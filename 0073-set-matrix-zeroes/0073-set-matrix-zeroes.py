class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        colSet = set()
        rowSet = set()
        M,N = len(matrix) , len(matrix[0])

        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    colSet.add(j)
                    rowSet.add(i)

        for i in range(M):
            for j in range(N):
                if i in rowSet or j in colSet:
                    matrix[i][j] = 0
        