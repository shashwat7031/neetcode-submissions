# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        def D(node):
            if node is None:
                return 0
            l = D(node.left)
            r = D(node.right)
            return 1 + max(l,r)
        return D(root)