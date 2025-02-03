# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        dummy = ListNode()
        prev = dummy
        dummy.next = head

        while head and head.next:

            first = head
            second = head.next
            temp = second.next
            prev.next = second
            second.next = first
            first.next = temp
            prev = first

            head = temp

        return dummy.next

