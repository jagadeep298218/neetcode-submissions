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
        nodes = {None : None}
        i = head
        while i:
            copy = Node(i.val)
            nodes[i] = copy
            i = i.next
        
        i = head

        while i:
            copy = nodes[i]
            copy.next = nodes[i.next]
            copy.random = nodes[i.random]
            i = i.next

        
        return nodes[head]
