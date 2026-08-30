# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        res = root

        while root.left or root.right:
            if not root:
                continue
            if not root.left and val < root.val:
                root.left = TreeNode(val)
                return res
            if not root.right and val > root.val:
                root.right = TreeNode(val)
                return res
            if val < root.val:
                root = root.left
            else:
                root = root.right
        if val < root.val:
            root.left = TreeNode(val)
        else:
            root.right = TreeNode(val)
        return res

        