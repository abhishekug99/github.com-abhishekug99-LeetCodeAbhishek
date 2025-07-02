# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(root, pathSum):
            if not root:
                return 0

            pathSum = pathSum*10 + root.val
            if not root.left and not root.right:
                return pathSum
            
            return dfs(root.left,pathSum)+dfs(root.right,pathSum)
        return dfs(root, 0)  
 


        