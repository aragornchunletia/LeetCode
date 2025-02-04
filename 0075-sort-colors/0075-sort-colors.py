class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Dutuch flag algorithm
        if mid == 0 swap at the front move front++ and move along
        if mid == 1 move along
        if mid == 2 swap at the back and move back--
        """
        low , mid, high = 0 , 0 , len(nums)-1
        while mid <= high:
            if nums[mid] == 0:
                nums[mid] , nums[low] = nums[low] , nums[mid]
                mid += 1
                low += 1
            
            elif nums[mid] == 1:
                mid += 1

            else:
                nums[mid] , nums[high] = nums[high] , nums[mid]
                high -= 1
        