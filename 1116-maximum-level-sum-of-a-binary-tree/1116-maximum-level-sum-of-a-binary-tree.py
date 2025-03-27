# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #BFS-more optimised
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = 1
        maxSum = float('-inf')
        maxLevel  = 1

        queue = deque([(root,1)])

        while queue:
            levelSum = 0
            for _ in range(len(queue)):
                node, lvl = queue.popleft()
                levelSum+=node.val

                if node.left:
                    queue.append((node.left,lvl+1))
                if node.right:
                    queue.append((node.right, lvl+1))
            if levelSum > maxSum:
                maxSum = levelSum
                maxLevel = level
            level+=1
        return maxLevel

        
       #DFS
        # def maxLevelSum(self, root: Optional[TreeNode]) -> int:
 
        #     res = {}
            
        #     def levels(root, depth):
        #         if not root:
        #             return 
        #         if depth not in res:
        #             res[depth] = 0
        #         res[depth]+=root.val

        #         levels(root.left, depth+1)
        #         levels(root.right, depth+1)
                
        #     # curr = 0

        #     levels(root, 1)
        #     print(res)
        #     return max(res, key=res.get)

        