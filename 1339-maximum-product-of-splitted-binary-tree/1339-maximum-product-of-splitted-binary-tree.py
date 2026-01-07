# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 10**9 + 7
        sumSet = []
        
        def dfsSum(node):
            if not node:
                return 0
            s = node.val + dfsSum(node.left) + dfsSum(node.right)
            sumSet.append(s)
            return s

        total = dfsSum(root)
        res = 0
        
        for s in sumSet:
            res = max(res, s*(total - s))
        
        return res%MOD
        



        