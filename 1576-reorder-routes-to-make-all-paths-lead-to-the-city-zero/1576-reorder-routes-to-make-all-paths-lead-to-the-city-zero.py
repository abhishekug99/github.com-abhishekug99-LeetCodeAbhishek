class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append((b,1))
            graph[b].append((a,0))
        # print(graph)
        
        visit = set()
        def dfs(node):
            visit.add(node)
            cnt = 0
            for nbr, needsReverse in graph[node]:
                if nbr not in visit:
                    cnt+= needsReverse #handle tuples with 0
                    cnt+=dfs(nbr)
            return cnt
        return dfs(0)
        
        
        # visit = set()
        # leadToZero = int()
        # def dfs(r, paths):
        #     cnt = 0
        #     leadToZero = int()
        #     if 0 in paths[r] and paths[r][1]==0:
        #         leadToZero = r
        #     if 0 in paths[r] and paths[r][0]==0:
        #         leadToZero = paths[r][1]
        #         cnt+=1
        #     if paths[r] and paths[r][1] == leadToZero:
        #         leadToZero = paths[r][0]
        #     else:
        #         leadToZero = paths[r][1]
            
        #     return cnt

        # final = 0
        # for r in range(len(connections)):
        #     final+=dfs(r, connections)

        # return final


            