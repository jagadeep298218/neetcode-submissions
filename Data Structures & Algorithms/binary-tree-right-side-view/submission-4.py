from collections import deque 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)

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
            


            
