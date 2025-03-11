class Solution:
    # def uniqueOccurrences(self, arr: List[int]) -> bool:
    #     graph = {}
    #     cnt = 1
    #     for val in arr:
    #         if val in graph:
    #             graph[val] += cnt
    #         else:
    #             graph[val] = cnt
        
    #     if len(graph.values()) == len(set(graph.values())):
    #         return True
    #     else:
    #         return False
    


    #altenate method with counter most efficient
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cnter = Counter(arr)
        if len(cnter.values()) == len(set(cnter.values())):
            return True
        else:
            return False

        