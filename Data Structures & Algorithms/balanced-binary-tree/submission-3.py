# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(node):
            check = True

            if not node: 
                return 0, True

            left, left_check = height(node.left) 
            right, right_check = height(node.right) 
            
            if abs(left - right) > 1 or not left_check or not right_check:
                check = False
            return max(left, right) + 1, check
        
        h, c = height(root)
        return c
        
        
        
        
        


