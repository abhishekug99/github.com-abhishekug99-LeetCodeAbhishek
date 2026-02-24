# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        binaryStr =''
        res = 0
        def dfs(root,binaryStr): 
            if not root:
                return
            binaryStr += str(root.val)
            dfs(root.left, binaryStr)
            dfs(root.right, binaryStr)
            if not root.right and not root.left:
                nonlocal res
                res += int(binaryStr,2)
            return res
        
        return dfs(root, binaryStr)