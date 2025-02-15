class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        M,N = len(matrix) , len(matrix[0])
        heights = [0]*(N+1)
        max_area = 0

        for row in matrix:
            for col in range(N):
                heights[col] = heights[col] + 1 if row[col] == "1" else 0
            
            stack = []
            for i in range(N+1):
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area , h*w)
                stack.append(i)

        return max_area


        
