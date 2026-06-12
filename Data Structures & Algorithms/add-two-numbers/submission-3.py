# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = False
        prev = ListNode(0)
        res = prev
        while l1 and l2:
            if (not l1.next) ^ (not l2.next):
                if not l1.next: l1.next = ListNode(0)
                if not l2.next: l2.next = ListNode(0)

            sum = l1.val + l2.val
            if carry:
                sum += 1
                carry = False
            if sum > 9:
                carry = True
                sum -= 10
            prev.next = ListNode(sum)
            prev, l1, l2 = prev.next, l1.next, l2.next

        if carry:
            prev.next = ListNode(1)
        return res.next



