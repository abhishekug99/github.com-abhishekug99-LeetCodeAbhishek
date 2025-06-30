# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        
        cur = root
        while cur:
            if cur.left:
                tmp = cur.right
                cur.right = cur.left #moving left to right
                cur.left = None

                prev = cur.right #go to right of new right subtree
                while prev.right:
                    prev = prev.right
                prev.right = tmp
            cur = cur.right



        #good but fe issues
        # while cur:
        #     if cur.left:
        #         if cur.right:
        #             tmp = cur.right
        #             cur.right = None
        #             cur.left.left = tmp
        #         tmp = cur.right
        #         cur.right = cur.left
        #         cur.left = None
        #         cur.right.right = tmp        
        #     cur = cur.right
            # cur = cur.left
            
            

        