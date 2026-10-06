# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        def insert(node):
            if not node:
                return 
            heapq.heappush(res,node.val)
            insert(node.left)
            insert(node.right)
        insert(root)
        while k > 1:
            heapq.heappop(res)
            k -=1
        return heapq.heappop(res)