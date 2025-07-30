# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #most optimised
        if not root:
            return 
        if root == q or root == p:
            return root
        nodeL = self.lowestCommonAncestor(root.left,p,q)
        nodeR = self.lowestCommonAncestor(root.right,p,q)
        if nodeL and nodeR:
            return root
        if  not nodeL and not nodeR:
            return
        if nodeL:
            return nodeL
        else: 
            return nodeR


        
        # space O(1)
        # pathP = []
        # pathQ = []

        # def findPath(node, target, path):
        #     if not node:
        #         return False
        #     path.append(node)
        #     if node == target:
        #         return True
        #     if findPath(node.left, target, path) or findPath(node.right, target, path):
        #         return True
        #     path.pop()
        #     return False

        # findPath(root, p, pathP)
        # findPath(root, q, pathQ)
        # # print(pathP)
        # # print(pathQ)
        
        # i=0
        # while i < len(pathP) and i < len(pathQ) and pathP[i] == pathQ[i]:
        #     i += 1
        # return pathQ[i-1] if i>0 else None
        


        