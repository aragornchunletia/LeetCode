class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        #backtrack
        def dfs(node, current_sum, path):
            if not node:
                return
            
            path.append(node.val)
            
            if not node.left and not node.right and current_sum == node.val:
                res.append(path[:])
            
            dfs(node.left, current_sum - node.val, path)
            dfs(node.right, current_sum - node.val, path)
    
            path.pop()
        
        dfs(root, targetSum, [])
        return res
