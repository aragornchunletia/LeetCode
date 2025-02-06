# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    if p is found reutrn p
    if q is found return q
    if found in leftree return leftTree
    if found in rightTree return rightTree
    if leftTree and rightTree return node
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            if not node:
                return None

            if node == p or node == q:
                return node

            leftTree = dfs(node.left)
            rightTree = dfs(node.right)

            if leftTree and rightTree:
                return node

            return leftTree if leftTree else rightTree

        res = dfs(root)

        return res

            
