# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(node, high):
            nonlocal res
            if not node:
                return 
            if node.val >= high:
                res += 1
                high = node.val
            
            dfs(node.left, high)
            dfs(node.right, high)

        dfs(root, root.val)
        return res