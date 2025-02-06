from bisect import bisect_left
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        count = 0          
        for num in nums:
            pos = bisect_left(sub, num)
            
            if pos == len(sub):
                sub.append(num)
                count += 1
            else:
                sub[pos] = num
        
        return count
