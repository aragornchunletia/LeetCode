# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
        greatest path sum at a certain node is leftPath + rightPath + node.val
        and to get maxLeft Sum and maxRight sum
        recurse to find the the max 
    """
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        maxPath = float('-inf')

        def dfs(root):
            nonlocal maxPath
            if not root:
                return 0
            
            leftSum =  max(dfs(root.left),0)
            rightSum = max(dfs(root.right),0)

            maxPath = max(maxPath , leftSum + rightSum + root.val)

            return root.val + max(leftSum , rightSum)

        dfs(root)
        return maxPath
        