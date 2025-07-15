# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    
        stack = [None]
        def validate(node)-> bool:
            if not node:
                return True
            
            if not validate(node.left):
                return False
            if stack[0] is not None and node.val <= stack[0]:
                return False
            stack[0] = node.val

            return validate(node.right)
        
        return validate(root)

        

        