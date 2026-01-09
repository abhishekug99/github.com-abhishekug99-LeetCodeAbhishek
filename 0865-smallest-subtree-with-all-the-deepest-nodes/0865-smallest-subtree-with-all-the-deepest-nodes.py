# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        q = deque([root])
        parent = {root:None}
        deepest = []
        while q:
            size = len(q)
            deepest = []
            for _ in range(size):
                node = q.popleft()
                deepest.append(node)
                if node.left:
                    parent[node.left]=node
                    q.append(node.left)
                if node.right:
                    parent[node.right]=node
                    q.append(node.right)
        deepestSet = set(deepest)
        while len(deepestSet)>1:
            deepestSet = set(parent[node] for node in deepestSet)
        
        return deepestSet.pop()
        
                    

