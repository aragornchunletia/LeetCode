class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        def helper(index , total , combination):
            if total < 0:
                return

            if total == 0:
                res.append(combination)
                return
            
            for i in range(index , len(candidates)):
                helper(i , total - candidates[i] , combination + [candidates[i]])

            return

        helper(0 , target , [])
        return res

                