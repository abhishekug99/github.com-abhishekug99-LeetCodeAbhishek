# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
    
        def helper(node):
            if not node:
                return
            helper(node.left)
            res.append(node.val)
            helper(node.right)
        
        helper(root)
        return res
        
        
        #below-> every time you give recursive call it willl start with empty list and that is why it will not give the one list
        # res=[]
        # if not root:
        #     return
        # self.inorderTraversal(root.left)
        # res.append(root.val)
        # self.inorderTraversal(root.right)

        # return res