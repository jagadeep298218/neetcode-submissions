# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(head, s):
            if not head:
                return False
            s+= head.val
            if not head.right and not head.left and s == targetSum:
                return True
            return dfs(head.left, s) or dfs(head.right, s)

        return dfs(root, 0)
