# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root

        # if not root:
        #     return
        # queue = deque()
        # def dfs(root):
        #     if root:
        #         queue.append(root)
        #     level = 0
        #     while len(queue)>0:
        #         for i in range(len(queue)):
        #             cur = queue.popleft()
        #             if cur.left:
        #                 # queue.append(cur.left)
        #                 tmpl = cur.left
        #             if cur.right:
        #                 # queue.append(cur.right)
        #                 tmpr = cur.right
        #             tmp = tmpl
        #             tmpl = tmpr
        #             tmpr = tmp
        #             queue.append(tmpl)
        #             queue.append(tmpr)
        #     print(queue)
        # dfs(root)

        #             if level == 1:
        #                 l = queue.popleft()
        #                 r = queue.popleft()
        #                 tmp = l
        #                 l = r
        #                 r = tmp
        #                 queue.append(l)
        #                 queue.append(r)
        #         level+=1
        # dfs(root)
        # return root
        
                

        