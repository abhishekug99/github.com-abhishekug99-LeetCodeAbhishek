class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        #start with city 0
        # recursively check nbrs
        # count out goinf edges

        edges = {(a,b) for a,b in connections}
        nbrs = { city:[] for city in range(n)}
        visit = set() #keep track of visit
        changes =0
        for a,b in connections: # to fill nbrs hash map
            nbrs[a].append(b)
            nbrs[b].append(a)
        def dfs(city ):
            nonlocal edges,nbrs,visit, changes
            for nbr in nbrs[city]:
                if nbr in visit:
                    continue
                #check if nbr reaches the city
                if (nbr,city) not in edges:
                    changes+=1
                visit.add(nbr)
                dfs(nbr)
        
        visit.add(0)
        dfs(0)
        return changes




        # graph = defaultdict(list)
        # for a, b in connections:
        #     graph[a].append((b,1))
        #     graph[b].append((a,0))
        # # print(graph)
        
        # visit = set()
        # def dfs(node):
        #     visit.add(node)
        #     cnt = 0
        #     for nbr, needsReverse in graph[node]:
        #         if nbr not in visit:
        #             cnt+= needsReverse
        #             cnt+=dfs(nbr)
        #     return cnt
        # return dfs(0)
    


            