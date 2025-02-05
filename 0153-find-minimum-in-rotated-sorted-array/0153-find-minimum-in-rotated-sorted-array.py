class Solution:
    """
    BINARY SEARCH 
    the point of inflection is the minValue
    """
    def findMin(self, nums: List[int]) -> int:
        
        start , end = 0 , len(nums)-1
        minVal = float('inf')

        while start <= end:
            mid = (end + start) // 2
            minVal = min(minVal , nums[mid])
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid - 1

        return minVal
