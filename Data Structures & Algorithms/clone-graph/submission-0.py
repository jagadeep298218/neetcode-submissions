"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        if not node.neighbors:
            return Node(1)
        
        root = Node(node.val)
        compare = {node:root}

        stack = []
        stack.append(node)
        while stack:
            val = stack.pop()
            for neighbor in val.neighbors:
                if neighbor not in compare:
                    compare[neighbor] = Node(neighbor.val)
                    stack.append(neighbor)
                compare[val].neighbors.append(compare[neighbor])
        
        return root
            
                



