class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        #optimal 
        potions.sort() #sort only once 
        

        for i in range(len(spells)):
            l,r = 0, len(potions)-1
            ans = len(potions)
            while l<=r:
                mid = (l+r)//2
                if success>(spells[i]*potions[mid]):
                    l = mid+1
                elif success<=(spells[i]*potions[mid]):
                    ans = mid
                    r = mid-1
            res.append(len(potions)-ans)
        return res