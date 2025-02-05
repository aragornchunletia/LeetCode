# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        #build from the middle
        def balanced_btree(arr):
            if not arr:
                return None

            n = len(arr)
            mid = n//2
            new_node = TreeNode(arr[mid])
            lTree = balanced_btree(arr[0:mid])
            rTree = balanced_btree(arr[mid+1:])
            new_node.left = lTree
            new_node.right = rTree

            return new_node

        return balanced_btree(nums)
            
        