class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        def search(val):
            start , end = 0 , len(numbers)-1
            while start <= end:
                mid = (start+end)//2
                if numbers[mid] == val:
                    return mid
                elif numbers[mid] < val:
                    start = mid+1
                else:
                    end = mid -1
            return -1
        
        targetList = [target - num for num in numbers]

        for i , num in enumerate(targetList):
            res = search(num)
            if res > -1 and res != i:
                return sorted([i+1,res+1])


