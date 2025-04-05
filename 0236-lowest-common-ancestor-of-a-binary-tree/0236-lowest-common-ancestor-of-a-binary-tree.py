# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pathP = []
        pathQ = []

        def findPath(node, target, path):
            if not node:
                return False
            path.append(node)
            if node == target:
                return True
            if findPath(node.left, target, path) or findPath(node.right, target, path):
                return True
            path.pop()
            return False

        findPath(root, p, pathP)
        findPath(root, q, pathQ)
        # print(pathP)
        # print(pathQ)
        
        i=0
        while i < len(pathP) and i < len(pathQ) and pathP[i] == pathQ[i]:
            i += 1
        return pathQ[i-1] if i>0 else None

        
        # ance = []
        # # dece = []
        # def Ance(root):
        #     if not root:
        #         return True
        #     if root.val == p.val:
        #         return True
        #     if Ance(root.left) or Ance(root.right):
        #         ance.append(root.val)
        #         return True
        #     return False
        # def Dece(root):
        #     if not root:
        #         return []
        #     dece = [root.val]
        #     dece.extend(Dece(root.left))
        #     dece.extend(Dece(root.right))
        #     return dece
        
        # Ance(root)
        # dece=Dece(p)
        


        