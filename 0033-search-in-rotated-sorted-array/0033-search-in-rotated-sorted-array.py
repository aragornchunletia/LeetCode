class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bsearch(array):
            start = 0
            end = len(array) - 1
            while start <= end:
                mid = (start + end) // 2
                if array[mid] == target:
                    return mid
                elif array[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
            return -1

        prev = 0
        curr = 1
        while curr < len(nums) and nums[prev] < nums[curr]:
            curr += 1
            prev += 1

        pivot = prev

        if target == nums[pivot]:
            return pivot

        elif nums[0] <= target <= nums[pivot]:
            return bsearch(nums[:pivot+1])
        
        res = bsearch(nums[pivot+1:])
        return res if res == -1 else res + pivot +1
            
        

        



