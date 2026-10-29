# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        red = l1
        blue = l2

        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0

        while red is not None or blue is not None or carry != 0:
            red_box = red.val if red is not None else 0
            blue_box = blue.val if blue is not None else 0
            result = red_box + blue_box + carry

            digit = result % 10
            carry = result // 10
            
            temp = ListNode(digit)
            curr.next = temp
            curr = temp

            if red is not None:
                red = red.next
            if blue is not None:
                blue = blue.next

        return dummyHead.next
        
