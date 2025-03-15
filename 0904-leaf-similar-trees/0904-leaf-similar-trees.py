# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        r1leaf=[]
        r2leaf=[]
    
        def getLeaf(node: Optional[TreeNode], leaves: List[int]):
            if not node: return
            if not node.left and not node. right:
                leaves.append(node.val)
                return 
            getLeaf(node.left, leaves)
            getLeaf(node.right, leaves)
        
        getLeaf(root1,r1leaf)
        getLeaf(root2,r2leaf)
        if r1leaf == r2leaf:
            return True
        else: return False


        
        