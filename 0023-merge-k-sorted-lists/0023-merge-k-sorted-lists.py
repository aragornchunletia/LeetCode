# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush , heappop , heapify
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy = ListNode()
        temp = dummy

        heap = [(node.val,i,node) for i , node in enumerate(lists) if node]
        heapify(heap)

        while heap:
            _,i,node = heappop(heap)
            if node.next:
                heappush(heap , (node.next.val , i , node.next))

            temp.next = node
            temp = temp.next

        return dummy.next




                

        