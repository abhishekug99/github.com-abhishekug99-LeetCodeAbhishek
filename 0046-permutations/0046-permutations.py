class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]
        prs = self.permute(nums[1:])
        # print(prs)
        res=[]
        for p in prs:
            print(p)
            for i in range(len(p)+1):
                pCopy = p[:]
                pCopy.insert(i, nums[0])
                res.append(pCopy)
        return res


     
        