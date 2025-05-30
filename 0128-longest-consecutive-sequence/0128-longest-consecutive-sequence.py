class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        cnter = {}
        for num in nums:
            cnter[num] = True
            # cnter[num] = cnter.get(num, 0) + 1
    
        maxCnt = 0

        # below loop just check over the nbrs and not the sequence
        # cnt = 0
        # for key in cnter:
        #     if (key+1) in cnter or (key-1) in cnter :
        #         cnt+=1
        #     maxCnt = max(cnt,maxCnt)
        # return maxCnt

        # here we are getting number and get valid sequence
        for num in cnter:
            if num-1 not in cnter:
                curr = num
                lenght = 1
                while curr+1 in cnter:
                    curr+=1
                    lenght+=1
                maxCnt = max(lenght,maxCnt)
        return maxCnt 