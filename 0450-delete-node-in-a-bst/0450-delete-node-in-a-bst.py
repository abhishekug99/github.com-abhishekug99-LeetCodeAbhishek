# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def minValue(root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr

        if not root:
            return None #as root can't be null in thi case
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        if key == root.val:
        # else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = minValue(root.right) #nds the smallest node in the right subtree of root.
                root.val = minNode.val # Instead of deleting the node directly, we copy the value of minNode (smallest node in the right subtree) into root.val.
                root.right = self.deleteNode(root.right, minNode.val) # Since we copied minNode.val into root.val, we need to remove minNode from the right subtree. We call deleteNode recursively to delete minNode from root.right.
        return root


         