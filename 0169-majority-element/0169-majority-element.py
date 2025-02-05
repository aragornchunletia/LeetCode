class Solution:
    """
    voting algorithm
    maintain a rolling count of curr element
    if different element encountered
    count --
    if count becomes zero switch the element
    """
    def majorityElement(self, nums: List[int]) -> int:
        ele = nums[0]
        count = 1

        for num in nums[1:]:
            if num == ele:
                count += 1  
            else:
                count -= 1

            if count < 0:
                ele = num
                count = 0

        return ele

        