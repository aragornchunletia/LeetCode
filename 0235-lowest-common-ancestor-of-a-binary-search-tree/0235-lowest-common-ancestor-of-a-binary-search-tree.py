# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        The way i thought this problem is if p and q both in different subtrees
        then the root is the LCA
        recursively search for that node where both the nodes are in different subtrees
        """
        def helper(root , p , q): 

            if (p.val < root.val) and (q.val < root.val):
                return helper(root.left , p , q)
            
            if (p.val > root.val) and (q.val > root.val):
                return helper(root.right , p , q)

            else:
                return root


        return helper(root , p, q)