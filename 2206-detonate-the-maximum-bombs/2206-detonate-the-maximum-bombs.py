# if (x+r >= bombs[j][0] >= x-r) or (  y+r >= bombs[j][1] <= y-r): #majors ib square and not in circularway

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        if len(bombs) ==1:
            return 1

        graph = {}
        for i in range(len(bombs)):
            graph[i] = []

        detonated = set()
        for i in range(len(bombs)):
            x = bombs[i][0]
            y = bombs[i][1]
            r = bombs[i][2]
            possibleExpolosions = []
            j=i+1
            for j in range(len(bombs)):
                if j ==i:
                    continue
                dx = bombs[j][0]-x
                dy = bombs[j][1]-y
                if dx**2 + dy**2 <= r**2:
                    graph[i].append(j)
                    # possibleExpolosions.append(j)
                    # detonated.add(((bombs[j][0],bombs[j][1])))
                 
       
            # graph[(x,y)] = possibleExpolosions
        def dfs(start, visited):
            visited.add(start)
            for nbr in graph[start]:
                if nbr not in visited:
                    dfs(nbr, visited)
        
        totalDetonations = 0
        for i in range(len(bombs)):
            visited = set()
            dfs(i, visited)
            totalDetonations = max(totalDetonations, len(visited))
        
        return totalDetonations