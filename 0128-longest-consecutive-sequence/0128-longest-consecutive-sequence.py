class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        s = set(nums) 

        for num in s: 
            #checking if this is a starting number for consecutive sequence
            if num - 1 not in s:
                current_len = 1
                current_num = num

                while current_num + 1 in s:
                    current_num += 1
                    current_len += 1

                max_len = max(max_len, current_len)

        return max_len
