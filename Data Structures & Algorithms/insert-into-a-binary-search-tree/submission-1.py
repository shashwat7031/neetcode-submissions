# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        newnode  = TreeNode(val,None,None)
        if root == None:
            return newnode
        curr = root
        while True:
            if val > curr.val:
                if curr.right is None:
                    curr.right = newnode
                    break
                curr = curr.right
                
            if val < curr.val:
                if curr.left is None:
                    curr.left = newnode
                    break
                curr = curr.left
        return root
