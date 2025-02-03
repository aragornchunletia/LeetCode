from heapq import heappop, heappush
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        if len(nums) < 3:
            return -1
        
        nums.sort()
        minSum = float('inf')
        minDiff = float('inf')
        for a in range(len(nums)-2):
            b = a + 1
            c = len(nums)-1 
            while b < c:
                currSum = nums[a]+nums[b]+nums[c]
                currDiff = abs(currSum - target)
                if currDiff < minDiff:
                    minSum = currSum
                    minDiff = currDiff

                if currSum == target:
                    return currSum

                elif currSum > target:
                    c -= 1

                elif currSum < target:
                    b += 1

        return minSum



