# Two-Pointer Approach to Trapping Rain Water
# We maintain two pointers (left and right) starting from both ends of the array.
# lH and rH track the maximum heights encountered from the left and right respectively.
# If height[left] is smaller, it means the trapped water depends on lH, so we update lH 
# and compute trapped water at the current position.
# Similarly, if height[right] is smaller, we update rH and compute trapped water on the right side.
# This ensures that at any step, water trapped depends on the minimum boundary encountered so far.
# The total trapped water is accumulated in 'area' and returned.


class Solution:
    def trap(self, height: List[int]) -> int:
        left , right = 0 , len(height) -1
        lH , rH = 0,0
        area = 0
        
        while left < right:
            if height[left] < height[right]:
                lH = max(lH , height[left])
                area += lH - height[left]
                left += 1

            else:
                rH = max(rH , height[right])
                area += rH - height[right]
                right -= 1

        return area