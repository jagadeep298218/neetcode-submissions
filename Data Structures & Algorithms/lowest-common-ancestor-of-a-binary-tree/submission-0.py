# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path=[]
        q_path=[]
        res = 0
        def path(node):
            if not node:
                return None
            if node == p or node == q:
                return node
            
            left, right = path(node.left), path(node.right)
            if left and right:
                return node
            return left or right

        return path(root)

    
            
