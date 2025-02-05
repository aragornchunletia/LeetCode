"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    """
    Solution
    old1 -> new1 -> old2 -> new2 -> old3 -> new3 
    new1.random = old1.random.next
    and seperate new from old using a dummy node
    """
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head
        dummy = Node(0)
        newtemp = dummy
        while temp:
            newNode = Node(temp.val)
            nextNode = temp.next
            temp.next = newNode
            newNode.next = nextNode
            temp = nextNode

        temp = head
        while temp:
            randptr = temp.random
            newNode = temp.next
            if randptr:
                newNode.random = randptr.next
            newtemp.next = newNode
            newtemp = newNode
            temp = newNode.next

        return dummy.next




            