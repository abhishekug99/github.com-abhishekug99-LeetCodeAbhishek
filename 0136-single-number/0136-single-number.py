class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        graph = {}
        for i in range(len(nums)):
            if nums[i] not in graph:
                graph[nums[i]] = 1
            else:
                graph[nums[i]] += 1
        return list(graph.keys())[list(graph.values()).index(1)]
