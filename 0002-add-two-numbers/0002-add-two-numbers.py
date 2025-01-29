# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        res = dummy
        temp1 , temp2 = l1 , l2

        carry = 0

        while temp1 and temp2:
            val = temp1.val + temp2.val + carry
            new = ListNode((val % 10))
            carry = val // 10
            res.next = new
            temp1 = temp1.next
            temp2 = temp2.next
            res = res.next

        while temp1:
            val = temp1.val + carry
            new = ListNode(val % 10)
            carry = val // 10
            res.next = new
            temp1 = temp1.next
            res = res.next

        while temp2:
            val = temp2.val + carry
            new = ListNode(val % 10)
            carry = val // 10
            res.next = new
            temp2 = temp2.next
            res = res.next

        if carry > 0:
            res.next = ListNode(carry)

        return dummy.next

            




        
