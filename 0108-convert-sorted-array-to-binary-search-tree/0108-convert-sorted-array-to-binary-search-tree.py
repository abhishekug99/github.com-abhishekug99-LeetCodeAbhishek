# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return 
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root
        
        # root  = 0
        # if 0 in nums:
        #     root = 0
        # else:
        #     root = nums[0]
        
        # newNode = TreeNode(root)
        # for num in nums:
        #     cur = newNode
        #     if num > cur.val:
        #         cur.right = TreeNode(num)
        #         cur = cur.right
        #     if num < cur.val:
        #         cur.left = TreeNode(num)
        #         cur = cur.left
            
        # return newNode

        