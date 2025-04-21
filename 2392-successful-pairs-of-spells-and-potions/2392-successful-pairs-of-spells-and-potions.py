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
            # x = len(potions[ans:])
            # if x:
            #     res.append(x)
            # else:
            #     res.append(0)
        return res
        
        # works but take so much time for sorting at every iteration, not good for too big data , test case 49
        # for i in range(len(spells)):
        #     # cnt = 0
        #     potionsSpells = sorted(list(map(lambda x:x*spells[i], potions))) #takes too much time sorts every iteration
        #     l,r = 0, len(potionsSpells)-1
        #     ans = len(potionsSpells)
        #     while l<=r:
        #         mid  = (l+r)//2
        #         if success>potionsSpells[mid]:
        #             l = mid+1
        #         elif success<=potionsSpells[mid]:
        #             ans = mid
        #             r=mid-1
                    
        #     x = len(potionsSpells[ans:])
        #     if x:
        #         res.append(x)
        #     else: 
            
        #         res.append(0)

        # return res

        # print(potionsSpells)