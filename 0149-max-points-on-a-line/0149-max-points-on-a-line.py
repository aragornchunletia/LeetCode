from math import gcd
from typing import List

class Solution:
    """
    Too check gradients and number of points that lie on a similiar gradient
    """
    def maxPoints(self, points: List[List[int]]) -> int:
        maxCount = 1  # At least one point
        N = len(points)
        
        for i in range(N):
            x1, y1 = points[i]
            currDict = {}
            duplicate = 0  # To track duplicate points
            vertical = 0   # To count vertical points
            
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                
                if dx == 0 and dy == 0:
                    # Duplicate point
                    duplicate += 1
                elif dx == 0:
                    # Vertical line (all points with the same x-coordinate)
                    vertical += 1
                else:
                    # Normalize the slope (dy/dx)
                    g = gcd(dy, dx)
                    dy //= g
                    dx //= g
                    
                    # Ensure slope is represented consistently
                    if dx < 0:
                        dx, dy = -dx, -dy
                    
                    slope = (dy, dx)
                    currDict[slope] = currDict.get(slope, 0) + 1
            
            # Max points on a single line through points[i]
            currMax = max(currDict.values(), default=0)
            maxCount = max(maxCount, currMax + duplicate + 1, vertical + duplicate + 1)
        
        return maxCount
