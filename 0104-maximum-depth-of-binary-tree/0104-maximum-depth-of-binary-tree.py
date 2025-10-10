# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        lvl = 0 
        while len(queue)>0:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            lvl+=1
        return lvl

        # if not root:
        #     return 0
        # ldepth = self.maxDepth(root.left)
        # rdepth = self.maxDepth(root.right)
        # print(rdepth)
        # return max(ldepth,rdepth)+1