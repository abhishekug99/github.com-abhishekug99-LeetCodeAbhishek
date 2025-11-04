class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        
        # maxCnts = max(cnts , key = cnts.get)
        # print(maxCnts)
        res = []
        for i in range(len(nums)-k+1):
            cnts = Counter(nums[i:i+k])
            sortedSub = sorted(cnts.items(), key=lambda x: (x[1], x[0]), reverse=True)
            print(sortedSub)
            topX = sortedSub[:x]
            curSum = 0
            for key,v in topX:
                    curSum+= key*v
            
            res.append(curSum)
        return res
            
                 