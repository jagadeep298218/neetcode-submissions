# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = end = head
        counter = 0
        while end:
            if counter > (n):
                curr = curr.next
            end = end.next
            counter += 1
        if counter == n:
            return head.next
        if curr.next:
            temp = curr.next.next
        else:
            temp = curr.next
        curr.next = temp
        return head

