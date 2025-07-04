# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        queue = deque()
        def bfs(root):
            if root:
                queue.append(root)
            level = 0
            while len(queue)>0:
                print(level)
                tmp = []
                res.append(tmp)
                for i in range(len(queue)):
                    cur = queue.popleft()
                    tmp.append(cur.val)
                    if cur.left:
                        queue.append(cur.left)
                        
                    if cur.right:
                        queue.append(cur.right)                     
                
                if level%2 == 1:
                    tmp.reverse()
                level+=1
                

        bfs(root)
        return res




        