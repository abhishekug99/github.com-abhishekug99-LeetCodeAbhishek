class Solution:
    def minJumps(self, arr: List[int]) -> int:
        if len(arr)==1:
            return 0
        if arr[0]==arr[-1]:
            return 1
        
        n = len(arr)
        graph = defaultdict(list)
        for i,v in enumerate(arr):
            graph[v].append(i)
        
        q = deque([0])
        visited = set([0])
        level=0
        while q:
            for _ in range(len(q)):
                i = q.popleft()

                if i == n-1:
                    return level
            
                for nxt in (i + 1, i - 1):
                    if 0 <= nxt < n and nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)
                #for same value
                for nxt in graph[arr[i]]:
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)
                #necessary for not getting at duplicate vals again
                graph[arr[i]].clear()
            level+=1
        
        return 0

        return 0