class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        cnter = {}
        for num in nums:
            cnter[num] = True
    
        maxCnt = 0
        for num in cnter:
            if num-1 not in cnter:
                curr = num
                lenght = 1
                while curr+1 in cnter:
                    curr+=1
                    lenght+=1
                maxCnt = max(lenght,maxCnt)
        return maxCnt 