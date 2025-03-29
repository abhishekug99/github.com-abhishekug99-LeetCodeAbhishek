# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = {}

        def dfs(root, sumTillNow):
            cnt=0
            if not root:
                return 0
            sumTillNow += root.val
            if  sumTillNow == targetSum:
                cnt+=1
            # if  sumTillNow > targetSum:
            #     sumTillNow-=root.val
            
            cnt += dfs(root.left, sumTillNow)
            cnt += dfs(root.right, sumTillNow)
            return cnt
        if not root:
            return 0
        return dfs(root, 0) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum) 
        

        