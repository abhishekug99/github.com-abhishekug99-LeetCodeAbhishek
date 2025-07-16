# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        avgs = []
        queue = deque()
        def bfs(root):
            if root:
                queue.append(root)
            level = 0
            while len(queue)>0:
                tmp = []
                for i in range(len(queue)):
                    cur = queue.popleft()
                    tmp.append(cur.val)
                    if cur.left:
                        queue.append(cur.left)
                    if cur.right:
                        queue.append(cur.right)
                avg = sum(tmp)/len(tmp)
                avgs.append(avg)
        bfs(root)
        return avgs