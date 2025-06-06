# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        curP = p
        curQ = q

    #recurrsion O(n) and O(1) time and space
        if not p and not q:
            return True  
        elif (p and not q) or (not p and q):
            return False
        elif p and q and p.val != q.val:
            return False
        lTree = self.isSameTree(p.left, q.left)
        rTree = self.isSameTree(p.right, q.right)

        return lTree and rTree

    # most optimised moris travesal O(n) and O(1) time and space
    #     while curP and curQ:
    #     # If both have no left children
    #         if not curP.left and not curQ.left:
    #             if curP.val != curQ.val:
    #                 return False
    #             curP = curP.right
    #             curQ = curQ.right
    #         elif curP.left and curQ.left:
    #             # Find the inorder predecessor for both
    #             predP = curP.left
    #             predQ = curQ.left

    #             while predP.right and predP.right != curP:
    #                 predP = predP.right
    #             while predQ.right and predQ.right != curQ:
    #                 predQ = predQ.right

    #             # If threading not yet created
    #             if not predP.right and not predQ.right:
    #                 predP.right = curP
    #                 predQ.right = curQ
    #                 curP = curP.left
    #                 curQ = curQ.left
    #             # If threading already exists
    #             elif predP.right == curP and predQ.right == curQ:
    #                 predP.right = None
    #                 predQ.right = None
    #                 if curP.val != curQ.val:
    #                     return False
    #                 curP = curP.right
    #                 curQ = curQ.right
    #             else:
    #                 # Tree structure differs
    #                 return False
    #         else:
    #             # One has left child, other doesn't → structure mismatch
    #             return False

    # # If both have been fully traversed, both should be None
    #     return curP is None and curQ is None
        


        #write but few minor erros
        # if not p and not q:
        #     return True
        
        # if not p or not q:
        #     return False
        
        # while curP and curQ:
        #     if curP.val!=curQ.val:
        #         return False
        #     if (curP.left and curQ.left) and curP.left.val!=curQ.left.val:
        #         return False
        #     elif (curP.left and  not curQ.left) or (not curP.left and curQ.left):
        #         return False
        #     if curP.left: curP = curP.left
        #     if curQ.left: curQ = curQ.left
        
        #     if (curP.right and  not curQ.right) or (not curP.right and curQ.right):
        #         return False
        #     elif (curP.right and curQ.right) and curP.right.val!=curQ.right.val:
        #         return False
                
        #     if curP.right: curP = curP.right
        #     if curQ.right: curQ = curQ.right

        # return True
