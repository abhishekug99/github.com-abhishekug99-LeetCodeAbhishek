# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        #with helper funct
        def toBST(l, r):
            if l>r:
                return
            mid = (l+r)//2
            root = TreeNode(nums[mid])
            root.left = toBST(l,mid-1)
            root.right = toBST(mid+1,r)
            return root
        return toBST(0, len(nums)-1)
        #accepted works well
        # if not nums:
        #     return 
        # mid = len(nums)//2
        # root = TreeNode(nums[mid])
        # root.left = self.sortedArrayToBST(nums[:mid])
        # root.right = self.sortedArrayToBST(nums[mid+1:])

        # return root
        
    
        