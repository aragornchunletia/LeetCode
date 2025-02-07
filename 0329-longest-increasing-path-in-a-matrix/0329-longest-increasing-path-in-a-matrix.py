class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M,N = len(matrix) , len(matrix[0])
        MEMO = [[-1]*(N+1) for _ in range(M+1)]




        def dfs(i , j):
            if i < 0 or j < 0 or i >= M or j >= N:
                return 0
            if MEMO[i][j] != -1:
                return MEMO[i][j]
            path = 1
            for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0 <= x < M and 0<=y<N and matrix[i][j] < matrix[x][y] :
                    path = max(1+dfs(x,y) , path)
            MEMO[i][j] = path
            return MEMO[i][j]


        res = 1

        for i in range(M):
            for j in range(N):
                res = max(res , dfs(i,j))
        
        return res
