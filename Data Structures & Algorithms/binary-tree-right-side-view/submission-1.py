# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
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

            while level_size > 1:
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level_size -= 1

            node = queue.popleft()
            res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return res
            


            
