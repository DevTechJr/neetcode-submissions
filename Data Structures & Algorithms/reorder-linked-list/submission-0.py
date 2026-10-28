# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split into halves
        # reverse second half
        # new dummy head and iterate through and add to it from second half

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow is now at the middle
        before = None
        current = slow.next
        slow.next = None

        while current is not None:
            after = current.next
            current.next = before
            before = current
            current = after
        # merge lists
        first = head
        second = before
        while second is not None:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
        
        
