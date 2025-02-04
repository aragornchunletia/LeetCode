class Solution:
    # multilevel binary search
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        M , N = len(matrix) , len(matrix[0])

        iL, iU = 0 , M-1
        row = -1
        while iL <= iU:
            mid = (iU+iL) // 2
            if matrix[mid][0] <= target <= matrix[mid][N-1]:
                row = mid
                break

            elif target < matrix[mid][0]:
                iU = mid - 1
            else:
                iL = mid + 1

        if row != -1:
            
            jL , jU = 0 , N-1
            while jL <= jU:
                mid = (jL + jU)//2
                if matrix[row][mid] == target:
                    return True
                elif target < matrix[row][mid]:
                    jU = mid -1
                else:
                    jL = mid +1

        return False



        
