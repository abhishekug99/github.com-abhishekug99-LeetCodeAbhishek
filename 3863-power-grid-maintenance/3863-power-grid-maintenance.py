class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # (c+ E+ q+clogc)
        pointConnections = defaultdict(list)
        for a,b in connections:
            pointConnections[a].append(b)
            pointConnections[b].append(a)

        online = set() #
        stationGrp = {}
        minHeaps = defaultdict(list)

        def dfs(station, groupId):
            if station in online:
                return
            online.add(station)
            stationGrp[station] = groupId
            heappush(minHeaps[groupId], station)
            
            for nbr in pointConnections[station]:
                dfs(nbr, groupId)

        for s in range(1, c+1):
            dfs(s,s)

        res = []
        for qType, qStation in queries:
            if qType == 1:
                if qStation in online:
                    res.append(qStation)
                    continue
                groupId = stationGrp[qStation]
                minHeap = minHeaps[groupId]
                while minHeap and minHeap[0] not in online:
                    heappop(minHeap)
                if minHeap:
                    res.append(minHeap[0])
                else:
                    res.append(-1)
            else:
                online.discard(qStation)
        
        return res
