class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        N = len(candidates)
        res = []

        def solve(i , total , curr):
            if total > target:
                return

            if total == target:
                res.append(curr[:])
                return

            for j in range(i ,N):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                curr.append(candidates[j])
                solve(j+1 , total + candidates[j] , curr)
                curr.pop()

        solve(0 , 0 , [])
        return res


