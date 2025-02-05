# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        multiple ways to do this
        go DFS or go BFS
        DFS Solution
        start at bottom, if equal depth return True else False
        comapre values of each node
        if mismatch return False
        return True
        """
        def helper(root1 , root2):
            if not root1 and not root2:
                return True

            if root1 and not root2:
                return False

            if not root1 and root2:
                return False
            
            leftRes = helper(root1.left , root2.left)
            rightRes = helper(root1.right , root2.right)

            if leftRes and rightRes and root1.val == root2.val:
                return True

            return False

        return helper(p,q)

        