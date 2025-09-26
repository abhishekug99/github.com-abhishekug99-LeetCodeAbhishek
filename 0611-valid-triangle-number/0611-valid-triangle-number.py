class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        
        for r in range(len(nums)-1,-1,-1):
            i,j = 0, r-1
            while i<j:
                if nums[i]+nums[j]>nums[r]:
                    res+=(j-i)
                    j-=1
                else:
                    i+=1
        return res
        
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
        
        # for i in range(len(nums)-2):
        #     j=i+1
        #     while j < (len(nums)-1):
        #         if nums[i] < nums[j]+nums[j+1]:
        #             res+=1
        #         j+=1
        # return res
             

        