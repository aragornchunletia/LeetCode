# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    preorder
    root._._._._._._ -> preOrder
    _._._root._._._ -> InOrder
    use map to store indices of values inOrder
    start traversing preorder
    find leftSubtree index from inorder i.e (0,rootIdx-1)
    find rightSubtree index from inorder i.e (rootIdx+1 , len(inorder))
    do this recursevly like a mergeSort
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        idx = {val : i for i , val in enumerate(inorder)}

        def helper(pre_start , pre_end , in_start , in_end):

            if pre_start > pre_end or in_start > in_end:
                return None

            root_val = preorder[pre_start]
            in_index = idx[root_val]

            left_size = in_index - in_start

            root = TreeNode(root_val)

            leftTree = helper(pre_start + 1 , pre_start + left_size , in_start , in_index)
            rightTree = helper(pre_start + left_size + 1 , pre_end , in_index + 1 , in_end)

            root.left = leftTree
            root.right = rightTree

            return root
            
        n = len(preorder)
        return helper(0 , n-1 , 0 ,n-1)