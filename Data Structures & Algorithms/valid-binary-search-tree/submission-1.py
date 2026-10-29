# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def check(node, left_bound, right_bound):
            if not node:
                return True
            
            if not((node.val < right_bound) and (node.val > left_bound)):
                return False
            
            return check(node.left, left_bound, min(right_bound, node.val)) and check(node.right, max(left_bound, node.val), right_bound)

        return check(root, float("-inf"), float("inf"))
