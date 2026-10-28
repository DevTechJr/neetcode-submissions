# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head == None):
            return None
        before = None
        current = head
        while current is not None:
            after = current.next
            current.next = before
            before = current
            current = after
        return before