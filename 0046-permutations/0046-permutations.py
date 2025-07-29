class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # O(n!*n^2)
        # if len(nums)==0:
        #     return [[]]
        # prs = self.permute(nums[1:])
        # # print(prs)
        # res=[]
        # for p in prs:
        #     # print(p)
        #     for i in range(len(p)+1):
        #         pCopy = p[:]
        #         pCopy.insert(i, nums[0])
        #         res.append(pCopy)
        # return res
#withouth recursion

        prs = [[]]
        for n in nums:
            newP=[]
            for p in prs:
                for i in range(len(p)+1):
                    pCopy = p[:]
                    pCopy.insert(i,n)
                    newP.append(pCopy)
            print(newP)
            prs = newP
        return prs

     
        