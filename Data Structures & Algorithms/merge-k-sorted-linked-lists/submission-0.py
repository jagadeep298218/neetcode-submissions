# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or (not lists[0] and len(lists) == 1):
            return ListNode(val="")
        heap = []
        for i in range(len(lists)):
            node = lists[i]
            while node:
                heapq.heappush(heap, node.val)
                node = node.next
        
        res = ListNode()
        final = res
        for i in range(len(heap)):
            res.val = heapq.heappop(heap)
            if len(heap) != 0:
                res.next = ListNode()
                res = res.next
        
        return final
