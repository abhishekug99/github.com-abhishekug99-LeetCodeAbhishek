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

        
        
        # res = []
        
        # def levels(root, depth):
        #     curr =0
        #     if not root:
        #         return 
        #     if root.left or root.right:
        #         curr += root.val
        #         print(curr)
        #         res.append(curr)
        #     levels(root.left, depth+1)
        #     levels(root.right, depth+1)
            
        #     # curr = 0

        # levels(root, 1)
        # print(res)
        # return res.index(max(res)) + 1

        