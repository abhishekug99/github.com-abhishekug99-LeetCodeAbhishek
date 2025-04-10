class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # time O(e+v)
        # space O(v+e)
        #DFS
        # graph = defaultdict(list) #map a->list of [b,a/b]
        # for (a,b), val in zip(equations, values):
        #     graph[a].append((b,val)) #straight given weights
        #     graph[b].append((a,1/val)) #reverse weights, inverses of equations
        # # print(graph)

        # def dfs(curr, target, visited, productTrack):
        #     if curr == target:
        #         return productTrack
        #     visited.add(curr)
        #     for nbr, val in graph[curr]:
        #         if nbr not in visited:
        #             res = dfs(nbr, target,visited, productTrack*val)
        #             if res!=-1:
        #                 return res
        #     return -1    
        # res = []
        # for a,b in queries:
        #     if a not in graph or b not in graph:
        #         res.append(-1.0)
        #     elif a==b:
        #         res.append(1)
        #     else:
        #         visited = set()
        #         res.append(dfs(a,b,visited,1.0))
        # return res

        #implementaion with BFS
        adj = defaultdict(list)
        for i, eq in enumerate(equations):
            a,b = eq
            adj[a].append((b,values[i]))
            adj[b].append((a,1/values[i]))
        
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            queue = deque()
            visit = set()
            queue.append([src, 1]) #to go layer by layer, so to keep track of simulatniously multiplication
            visit.add(src)
            while queue:
                node,weight= queue.popleft()
                if node == target:
                    return weight

                for nbr, weightInAdj in adj[node]:
                    if nbr not in visit: #if not visited traverse the bfs
                        queue.append([nbr,weight * weightInAdj])
                        visit.add(nbr)

            return -1
        
        return [bfs(q[0],q[1])for q in queries]












        #does not work but basic logic for understanding
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



        
        