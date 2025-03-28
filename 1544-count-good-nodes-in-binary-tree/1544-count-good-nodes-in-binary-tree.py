# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        def dfs(root, maxTillNow):
            cnt = 0
            if not root:
                return 0
            
            if root.val >=maxTillNow:
                cnt += 1
            else:
                cnt = 0
            maximum = max(root.val,maxTillNow)
            return cnt + dfs(root.left,maximum) + dfs(root.right,maximum)
            

            
        res = dfs(root, root.val)
        return res
