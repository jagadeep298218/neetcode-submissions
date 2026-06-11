from collections import deque 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque()
        queue.append(root)
        if not root:
            return []

        while queue:
            level_size = len(queue)
            res.append(queue[-1].val)
            for i in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level_size -= 1
        
        return res
            


            
