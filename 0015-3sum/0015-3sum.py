class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i,val in enumerate(nums):
            if i > 0 and val == nums[i-1]: 
                continue
            l,r = i+1,len(nums)-1
            while l<r:
              threeSum = val + nums[l] +nums[r]
              if threeSum>0:
                r-=1
              elif threeSum < 0:
                l+=1
              else:
                res.append([val,nums[l],nums[r]])
                l+=1
                while nums[l] == nums[l-1] and  l<r:
                    l+=1
        return res
            
        #     if -(numsSorted[i]+numsSorted[j]) in numsSorted and -(numsSorted[i]+numsSorted[j]) not in visited:
        #         trip.append(numsSorted[i])
        #         trip.append(numsSorted[j])
        #         trip.append(-(numsSorted[i]+numsSorted[j]))
        #         res.append(trip)
        #     visited.add(-(numsSorted[i]+numsSorted[j]))
        #     j+=1

        # return res
    


         