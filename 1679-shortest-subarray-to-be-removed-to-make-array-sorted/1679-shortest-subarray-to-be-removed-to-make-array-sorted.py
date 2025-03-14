class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        if arr == sorted(arr):
            return 0
        # if arr == sorted(arr, reverse=True):
        #     return len(arr)-1
        
        n = len(arr)
        left = 0
        while left<n-1 and arr[left]<=arr[left+1]:
            left+=1
        
        right = n-1
        while right>0 and arr[right]>=arr[right-1]:
            right-=1
        
        res = min(n-left-1, right)
        i,j=0,right
        while i<=left and j<n:
            if arr[i]<=arr[j]:
                res = min(res,j-i-1)
                i+=1
            else:
                j+=1
        return res
        