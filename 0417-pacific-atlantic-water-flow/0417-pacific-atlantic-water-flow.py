class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        def dfs(i,j,ocean):
            ocean.add((i,j))
            for x,y in [(i+1,j) , (i-1,j) , (i,j+1) , (i,j-1)]:
                if 0<=x<M and 0<=y<N and (x,y) not in ocean and heights[x][y] >= heights[i][j]:
                    dfs(x,y,ocean)

        M,N = len(heights) , len(heights[0])
        pacific , atlantic = set() , set()

        for i in range(M):
            dfs(i,0,pacific)
            dfs(i,N-1,atlantic)

        for j in range(N):
            dfs(0,j,pacific)
            dfs(M-1,j , atlantic)

        return  list(pacific & atlantic)
