# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def helper(root):
            if not root:
                return 0
            
            depth_l = 1 + helper(root.left)
            depth_r = 1 + helper(root.right)

            return max(depth_l , depth_r)

        return helper(root)
        