# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return  # No reordering needed for empty, single-node, or two-node lists.

        # Step 1: Find the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secondH = slow.next
        slow.next = None

        #reverse Second half
        prev = None
        while secondH:
            nex = secondH.next
            secondH.next = prev
            prev = secondH
            secondH = nex
        secondH = prev

        #interleave both lists
        firstH = head
        while secondH:
            temp1 = firstH.next
            temp2 = secondH.next
            
            firstH.next = secondH
            secondH.next = temp1
            
            firstH = temp1
            secondH = temp2
