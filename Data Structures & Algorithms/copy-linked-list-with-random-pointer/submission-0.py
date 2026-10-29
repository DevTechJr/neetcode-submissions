"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        freqMap = {}
        dummyHead = Node(0)

        current = head
        dummyCurrent = dummyHead
        while current is not None:
            tempNode = Node(current.val) # add index
            # update dummy list
            dummyCurrent.next = tempNode
            dummyCurrent = tempNode
            # move current
            freqMap[current] = tempNode
            current = current.next
        
        slow = head
        while slow is not None:
            temp_node = freqMap[slow]
            if slow.next is not None:
                temp_node.next = freqMap[slow.next]
            if slow.random is not None:
                temp_node.random = freqMap[slow.random]
            slow = slow.next        
            
        
        return dummyHead.next

