# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverseLL(start, end):
            curr = start
            prev, nex = None, None
            while curr != end:
                nex = curr.next
                curr.next = prev
                prev = curr
                curr = nex
            return prev
        
        dummy = ListNode()
        dummy.next = head
        temp = dummy
        
        while True:
            # Check if there are at least k nodes to reverse
            curr = temp
            for _ in range(k):
                curr = curr.next
                if not curr:
                    return dummy.next
            
            start = temp.next  # Start of the group
            end = curr.next    # Node after the group
            
            # Reverse the current k-group
            temp.next = reverseLL(start, end)
            
            # Connect the reversed group to the rest of the list
            start.next = end
            
            # Move temp to the end of the reversed group
            temp = start
