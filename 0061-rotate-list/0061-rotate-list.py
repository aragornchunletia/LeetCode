
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 0:
            return head

        q = deque([])
        while head:
            q.append(head)
            head = head.next

        N = len(q)
        r = k % N
        for _ in range(r):
            node = q.pop()
            q.appendleft(node)

        dummy = ListNode()
        temp = dummy
        while q:
            node = q.popleft()
            temp.next = node
            temp = temp.next

        temp.next = None

        return dummy.next