# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        As root node is common,
        check if leftSubtree == rightSubtree
        left.left == right.right and left.right == right.left
        
        """

        def check_reflection(leftNode , rightNode):
            
            if not leftNode and not rightNode:
                return True

            if not leftNode or not rightNode or leftNode.val != rightNode.val:
                return False 

            out_nodes = check_reflection(leftNode.left , rightNode.right)
            in_nodes = check_reflection(leftNode.right , rightNode.left)

            return out_nodes and in_nodes

        if not root:
            return True

        return check_reflection(root.left , root.right)
