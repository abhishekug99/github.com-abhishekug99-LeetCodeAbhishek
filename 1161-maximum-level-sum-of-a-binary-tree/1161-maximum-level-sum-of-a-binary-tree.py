# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
    
        level = 1
        maxlevel =  1
        maxSum = float('-inf')
        queue = deque([(root,1)])

        while queue:
            levelTotal = 0
            for _ in range(len(queue)):
                node, lev = queue.popleft()
                levelTotal+=node.val
                if node.left:
                    queue.append((node.left, lev+1))
                if node.right:
                    queue.append((node.right, lev+1))
            if levelTotal>maxSum:
                maxSum = levelTotal
                maxlevel = level
            level+=1
        return maxlevel
        




