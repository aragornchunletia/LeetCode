class Solution:
    # all possible sets
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        path = []
        res = []

        def backtracking(i):
            if i == n:
                res.append(list(path))
                return

            path.append(nums[i])
            backtracking(i+1)
            path.pop()
            backtracking(i+1)

        backtracking(0)
        return res
        