class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        empMngrMap = defaultdict(list)
        res = 0
        for i in range(n):
            empMngrMap[manager[i]].append(i)
        
        #BFS
        q = deque([(headID, 0)]) #(id, time to inform)
        while q:
            idx, time = q.popleft()
            res = max(res, time)
            for emp in empMngrMap[idx]:
                q.append((emp, time + informTime[idx]))
        return res
        
        
        

        