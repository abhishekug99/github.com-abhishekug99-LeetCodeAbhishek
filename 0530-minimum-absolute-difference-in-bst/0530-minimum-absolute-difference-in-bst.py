# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def postOrderTravelsal(node, value):
            if not node:
                return 
            
            postOrderTravelsal(node.left, value)
            value.append(node.val)
            postOrderTravelsal(node.right, value)
            
        value = []
        postOrderTravelsal(root, value)
        value.sort()
        # print(value)
        minDiff = float('inf')
        for i in range(1,len(value)):
            minDiff = min(minDiff, abs(value[i]-value[i-1]))
        return minDiff

        