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
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        res = ListNode()
        final = res
        while heap:
            val, i, node = heapq.heappop(heap)
            res.next = ListNode(val)
            res = res.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return final.next