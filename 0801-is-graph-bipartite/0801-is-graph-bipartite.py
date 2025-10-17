class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        adjlist = defaultdict(list)
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                adjlist[i].append(graph[i][j])
        n = len(graph)
        color = [-1]*n
        def dfs(node,c):
            color[node] = c
            for nbr in graph[node]:
                if color[nbr] ==-1:
                    if not dfs(nbr, 1-c):
                        return False
                elif color[nbr] == color[node]:
                    return False
            return True

        for i in range(n):
            if color[i]==-1:
                if not dfs(i,0):
                    return False
        return True 

        # print(adjlist)

