# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        treeMap = {}
        for i, val in enumerate(inorder):
            treeMap[val] = i
        postIdx = [len(postorder) - 1]

        def insert(l,r):
            if l>r:
                return None

            rootVal = postorder[postIdx[0]]
            postIdx[0] -= 1

            root = TreeNode(rootVal)
            rootIdx = treeMap[rootVal]

            root.right = insert(rootIdx+1, r)
            root.left = insert(l, rootIdx-1)
            

            return root
        
        
        return insert(0,len(inorder)-1)

        