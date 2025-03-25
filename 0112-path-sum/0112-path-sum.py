# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        #decrementin approach
        # if not root:
        #     return False
        # targetSum-=root.val
        # if not root.left and not root.right:
        #     return targetSum==0

        # return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)

        #Making to the sum approach DFS apprach:
        # def dfs(root, currSum):
        #     if not root:
        #         return False
        #     currSum += root.val
        #     if not root.left and not root.right:
        #         return currSum == targetSum
        #     return dfs(root.left, currSum) or dfs(root.right, currSum)
        # return dfs(root,0) 

        #BACKTRACKING
        path = []
        def backTrack(root,currSum):
            if not root:
                return False
            path.append(root.val)
            currSum += root.val
            if not root.left and not root.right and currSum == targetSum:
                return True
            
            if backTrack(root.left, currSum) or backTrack(root.right, currSum):
                return True
            path.pop()
            return False
        
        return backTrack(root,0)

