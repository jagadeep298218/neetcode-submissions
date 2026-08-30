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
        def recursion(node):
            if not node.left and (node.val > val):
                node.left = TreeNode(val)
            if not node.right and (node.val < val):
                node.right = TreeNode(val)
            if node.right and val > node.val:
                recursion(node.right)
            elif node.left and val < node.val:
                recursion(node.left)
        recursion(root)
        return res
            


        '''

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

        '''

        