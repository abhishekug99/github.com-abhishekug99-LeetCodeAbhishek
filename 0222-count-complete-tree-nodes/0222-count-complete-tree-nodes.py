# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res =[]
        def counter(root)->int:
            if not root:
                return 
            res.append(root.val)
            counter(root.left) 
            counter(root.right)
        counter(root)
        return len(res)

        

        