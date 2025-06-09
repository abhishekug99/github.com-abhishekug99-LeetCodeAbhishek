# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def isEqual(lRoot,rRoot):
            if lRoot == None and rRoot == None:
                return True
            if lRoot ==None or rRoot == None:
                return False
            if lRoot.val != rRoot.val:
                return False
            return isEqual(lRoot.left,rRoot.right) and isEqual(lRoot.right,rRoot.left)
        
        if not root: return True
        
        return isEqual(root.left,root.right)


        