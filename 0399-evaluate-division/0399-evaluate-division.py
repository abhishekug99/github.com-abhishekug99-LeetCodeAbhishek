class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for (a,b), val in zip(equations, values):
            graph[a].append((b,val))
            graph[b].append((a,1/val))
        # print(graph)

        def dfs(curr, target, visited, productTrack):
            if curr == target:
                return productTrack
            visited.add(curr)
            for nbr, val in graph[curr]:
                if nbr not in visited:
                    res = dfs(nbr, target,visited, productTrack*val)
                    if res!=-1:
                        return res
            return -1    
        res = []
        for a,b in queries:
            if a not in graph or b not in graph:
                res.append(-1.0)
            elif a==b:
                res.append(1)
            else:
                visited = set()
                res.append(dfs(a,b,visited,1.0))
        return res


        # res = []
        # visit = set()
        # varSet = set()
        # equationAns = defaultdict()
        # for i in range(len(equations)):
        #     varSet.add(equations[i][0])
        #     varSet.add(equations[i][1])
        # print(varSet)

        # def getQueryVal(query):
        #     if query[0] not in varSet or query[1] not in varSet:
        #         return -1.0
        #     if query in equestions():
        #         valIdx = equations.index(query)
        #         val = values[valIdx]
        #         return val
        #     if query[0] == query[1]:
        #         return 1.0
        #     if [query[1],query[0]] in equations:
        #         valIdx = equations.index([query[1],query[0]])
        #         val = values[valIdx]
        #         return 1/val
        #     if query not in equestions and query[0] in varSet and query[1] in varSet:
        #         x=0
        #         y=0
        #         for q in range(len(equations)):
        #             if query[0] in q:
        #                 x = values[q]
        #             if query[1] in q:
        #                 y = values[q]
        #         return x*y
        
        # for query in queries:
        #     val = getQueryVal(query)
        #     res.append(val)
        # return res



        
        