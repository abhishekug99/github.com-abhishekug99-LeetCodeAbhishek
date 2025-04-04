# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # similar but more optimised one
        self.logestOne = 0
        def dfs(root,pathDir,depth):
            if not root:
                return 0
            self.logestOne = max(self.logestOne, depth)

            if pathDir == 'right':
                dfs(root.right, 'left', depth+1)
                dfs(root.left, 'right', 1)
            if pathDir == 'left':
                dfs(root.left, 'right', depth+1)
                dfs(root.right, 'left', 1)
        
        dfs(root.right,'left',1)
        dfs(root.left,'right',1)
        return self.logestOne

        
        #works fine for all test cases
        # maxLen = 0
        # def dfs(root, isRight, lenghtCnt):
        #     nonlocal maxLen
        #     if not root:
        #         return 0
            
        #     maxLen = max(maxLen, lenghtCnt)

        #     if isRight:
        #         dfs(root.left, False, lenghtCnt+1)
        #         dfs(root.right,True,1)
        #     else:
        #         dfs(root.right, True, lenghtCnt+1)
        #         dfs(root.left,False,1)
        #     return maxLen        
        
        # dfs(root.left, False, 1)
        # dfs(root.right, True, 1)
        # return maxLen
        