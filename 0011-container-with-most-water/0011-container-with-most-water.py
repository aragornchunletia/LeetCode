class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0
        start = 0
        end = len(height)-1
        while start <= end:

            area = min(height[start] , height[end]) * (end - start)
            maxA = max(maxA , area)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return maxA