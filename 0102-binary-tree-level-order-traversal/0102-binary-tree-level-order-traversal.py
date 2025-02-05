# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    """
    Queue based BFS
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:    return []

        res = []
        q = deque([root])
        while q:
            currlevel = []
            #len(q) gives a snapshot of number of elemets at a certain level
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                currlevel.append(node.val)

            res.append(currlevel)

        return res


