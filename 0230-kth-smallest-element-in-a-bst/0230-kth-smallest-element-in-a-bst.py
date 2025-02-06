# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Using the property of the bst, i.e 
    inorder traversal yeilds a sorted traversal
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        res = None
        def inorder(root):
            nonlocal count,res
            if not root:
                return

            inorder(root.left)
            count -= 1
            if count == 0:
                res = root.val
                return
            inorder(root.right)

        inorder(root)
        return res

        