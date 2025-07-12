class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        graph = {}
        for i, val in enumerate(nums):
            if val in graph.keys() and abs(i - graph[val]) <=k:
                return True
            graph[val] = i
                    
        return False    


        # n = len(nums)
        # while i<n:
        #     for j in range(i+1, n):
        #         if nums[i] == nums[j] and abs(i-j)<=k:
        #             return True
        #     i+=1
        # return False