# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        rootVal = preorder[0]
        root = TreeNode(rootVal)

        i = inorder.index(rootVal)

        root.left = self.buildTree(preorder[1:1+i], inorder[:i])
        root.right = self.buildTree(preorder[1+i:], inorder[i+1:])

        return root


        
         
        