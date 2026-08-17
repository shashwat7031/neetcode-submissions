# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def num(node,maxVal):
            if node is None:
                return 0 
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal,node.val)
            res += num(node.left,maxVal)
            res += num(node.right,maxVal)
            return res
        return num(root,root.val)
        