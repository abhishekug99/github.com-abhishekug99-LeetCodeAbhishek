# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        prefixSum = defaultdict(int)
        prefixSum[0]=1

        def dfs(node,sumTillNow):
            if not node:
                return 0
            sumTillNow +=node.val
            # If sumTillNow - targetSum exists in prefixSum, 
            # that means there exists a previous sum from which subtracting targetSum leads to sumTillNow.
            cnt = prefixSum[sumTillNow - targetSum]
            prefixSum[sumTillNow] += 1
            # print(prefixSum)

            cnt+=dfs(node.left,sumTillNow)
            cnt+=dfs(node.right,sumTillNow)

            prefixSum[sumTillNow] -= 1
            return cnt

        return dfs(root,0)


        #works O(nlagn) and worst case O(n^2)
        # def dfs(root, sumTillNow):
        #     cnt=0
        #     if not root:
        #         return 0
        #     sumTillNow += root.val
        #     if  sumTillNow == targetSum:
        #         cnt+=1
        #     # if  sumTillNow > targetSum:
        #     #     sumTillNow-=root.val
            
        #     cnt += dfs(root.left, sumTillNow)
        #     cnt += dfs(root.right, sumTillNow)
        #     return cnt

        # if not root:
        #     return 0
    
        # return dfs(root, 0) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
        

        