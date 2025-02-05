class Solution:
    """
    count distinct connected components
    ->
    """
    def numIslands(self, grid: List[List[str]]) -> int:

        m , n = len(grid) , len(grid[0])

        def dfs(x , y):
            if x < 0 or y < 0 or x >= m or y >= n:
                return
            
            if grid[x][y] == "0" :
                return
            # marking the cell visited
            grid[x][y] = "0"

            for i , j in [(1,0),(0,1),(0,-1),(-1,0)]:
                a , b = x+i , y+j
                dfs(a,b)

            return

        connected_components = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    connected_components += 1
                    dfs(i, j)

        return connected_components
                