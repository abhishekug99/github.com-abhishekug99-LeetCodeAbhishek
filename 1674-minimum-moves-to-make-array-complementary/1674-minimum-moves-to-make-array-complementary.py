class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0]*(2*limit+2 )

        for i in range(n//2):
            x = nums[i]
            y = nums[n-1-i]
            a,b = min(x,y), max(x,y)
            s = x+y
            low = a+1
            high = b + limit
            diff[2]+=2
            diff[low] -=1
            diff[high+1]+=1
            diff[s]-=1
            diff[s+1]+=1
        print(diff)
        res = float('inf')
        curr=0
        for S in range(2, 2*limit+1):
            curr+=diff[S]
            res = min(res, curr)
        
        return res