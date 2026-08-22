# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def goodnodes(node,maxval):
            if node is None:
                return 0
            res = 1 if node.val >= maxval else 0
            maxval = max(maxval,node.val)
            res += goodnodes(node.left,maxval)
            res += goodnodes(node.right,maxval)
            return res
        return goodnodes(root,root.val)