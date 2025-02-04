class Solution:
    """
    Monotonic Stack approach to find the largest rectangle in a histogram.
    Uses a stack to maintain increasing height bars and calculate maximum area efficiently.
    """
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # Stores (index, height) pairs
        area = 0  # Variable to track the maximum area

        for i, h in enumerate(heights):
            start = i
            # Maintain an increasing stack (top element is always the greatest so far)
            while stack and h < stack[-1][1]:  # If the current height is smaller, process previous heights
                idx, height = stack.pop()
                area = max(area, height * (i - idx))  # Compute area with popped height as the smallest bar
                start = idx  # Update start to the earliest index of the popped bar
            stack.append((start, h))  # Push the current bar onto the stack

        # Process remaining elements in the stack
        for i, h in stack:
            area = max(area, h * (len(heights) - i))  # Compute area using the full width from stored index

        return area
