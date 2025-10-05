# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n==0:
            return []
        
        def build(start, end):
            if start> end:
                return [None]
            allTrees = []

            for root in range(start,end+1):
                #possible left and right trees
                lTree = build(start, root-1)
                rTree = build(root+1, end)

                for l in lTree:
                    for r in rTree:
                        node = TreeNode(root)
                        node.left = l
                        node.right = r
                        allTrees.append(node)
            return allTrees

        return build(1,n)    

        
