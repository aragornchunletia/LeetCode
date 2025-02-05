from heapq import heappop, heapify
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: 
            return head

        temp = head
        heap = []
        idx = 0
        
        # Push all nodes into the heap
        while temp:
            heap.append((temp.val,idx,temp))
            temp = temp.next
            idx+=1

        heapify(heap)  # Heapify in O(n)

        dummy = ListNode(0)
        temp = dummy

        # Extract elements from the heap and rebuild the sorted list
        while heap:
            _,_, node = heappop(heap)
            node.next = None  # Detach old references
            temp.next = node
            temp = node

        return dummy.next
