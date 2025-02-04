class Solution:
    #dfs based approch
    # Space O(len(word))[Callstack] , Time -> O(M*N*4^K) as 4 directions for each cell
    def exist(self, board: List[List[str]], word: str) -> bool:
        m , n = len(board) , len(board[0])

        def helper(i,j,idx):

            if idx == len(word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[idx]:
                return False
            
            temp = board[i][j]
            board[i][j] = "*"
            found = False
            for x , y in [[0,1], [0,-1], [1,0],[-1,0]]:
                found |= helper(i+x , j+y, idx+1)
            board[i][j] = temp

            return found

        

        for i in range(m):
            for j in range(n):
                if helper(i,j,0):
                    return True

        return False

