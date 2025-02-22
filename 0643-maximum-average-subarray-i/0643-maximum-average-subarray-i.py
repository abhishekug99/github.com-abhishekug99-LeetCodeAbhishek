class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSum = sum(nums[:k])
        maxSum = currSum

        for i in range(k, len(nums)):
            currSum += nums[i] - nums[i-k]
            maxSum = max(currSum,maxSum)
        return maxSum/k

        # correct sol but EOL at 122 rest all passed O(nk) is th reason
        # graph = {}
        # lst =[]
        # if len(nums)==1:
        #     return nums[0]
        # for i in range(len(nums) - k + 1):
        #     graph[i]  = sum(nums[i:i+k])
        # for val in graph.values():
        #     avg = val/k
        #     lst.append(avg) 

        # return max(lst)

        


        
        
        return maxAvg