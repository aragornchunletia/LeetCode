class Solution:
    """
    Just follow the spiral
    -> go left to right , top++
    -> go top to bottom , right --
    -> go right to left , bottom --
    -> go bottom to top , left ++
    space -> O(1) excluding result
    time -> O(len(matrix[0]) * len(matrix))
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        left , top , right , bottom =  0 , 0 , len(matrix[0]) -1  , len(matrix)-1
        res = []

        while top <= bottom and left <= right:

            for j in range(left , right+1):
                res.append(matrix[top][j])
            top += 1
            
            for i in range(top , bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for j in  range(right , left-1 , -1):
                    res.append(matrix[bottom][j])
                bottom -= 1

            if left <= right:
                for i in range(bottom , top -1 , -1):
                    res.append(matrix[i][left])
                left += 1 

        return res