# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return []
        queue = deque([(root,1)])
        while len(queue)>0:
            track = []
            for i in range(len(queue)):
                curr, lvl = queue.popleft()
                track.append(curr.val)
                if curr.left:
                    queue.append((curr.left, lvl+1))
                if curr.right:
                    queue.append((curr.right, lvl+1))
            res.append(track)
     
        return res
        
        
        # res = []
        # if not root:
        #     return []
        # queue = deque()
        # if root:
        #     queue.append(root)
        # level = 0
        # while len(queue)>0:
        #     track = []
        #     for i in range(len(queue)):
        #         curr = queue.popleft()
        #         track.append(curr.val)
        #         if curr.left:
        #             queue.append(curr.left)
        #         if curr.right:
        #             queue.append(curr.right)
        #     res.append(track)
        #     level+=1
        # return res

        