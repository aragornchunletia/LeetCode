# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    recursively check if every subtree follows
    if root.left in lowerBounds and root.right in upper bounds
    at each level whilst updating bounds
    i.e 
    leftSubtree -> upperBound(root) , lowerBound(-inf)
    rightSubtree -> upperBound(inf) , lowerBound(root)
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root , lower , upper):

            if not root:
                return True

            if root.val >= upper or root.val <= lower:
                return False
         

            leftTree = helper(root.left , lower , root.val)
            rightTree = helper(root.right , root.val , upper)

            return leftTree and rightTree

        return helper(root , float('-inf') , float('inf'))
