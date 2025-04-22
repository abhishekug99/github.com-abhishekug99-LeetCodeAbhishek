class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # bruteforce TLE, but correct
        # if len(piles)==h:
        #     return max(piles)
        # k=1
        # while True:
        #     time=0
        #     for i in range(len(piles)):
        #         time+=ceil(piles[i]/k) 
            
        #     if time<=h:
        #         return k
        #     k+=1
        # return k

        #Binary search
        l,r = 1, max(piles) #our k must be in min to max of numbers in the list, not exctly match but its there
        res = r
        while l<=r:
            time = 0
            k = (l+r)//2 #assume k is in middle first if bigger than h go left else go right
            for pile in piles:
                time +=ceil(pile/k)
            
            if time<=h:
                res = min(res,k)
                r = k-1 #search in left portion
            else:
                l = k+1
            
        return res



        

        