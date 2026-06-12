class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
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
            
                



