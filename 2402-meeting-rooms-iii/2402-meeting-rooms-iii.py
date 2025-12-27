class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x:x[0])
        freeRoom = [i for i in range(n)]
        used = [] # (end, roomnum)
        cnts = [0]*n #schedued meetings

        for s,e in meetings:
            while used and s>=used[0][0]:
                _, room = heapq.heappop(used)
                heapq.heappush(freeRoom, room)
            if not freeRoom:
                endTime, room = heapq.heappop(used)
                e = endTime+(e-s)
                heapq.heappush(freeRoom, room)
            room = heapq.heappop(freeRoom)
            heapq.heappush(used,(e,room))
            cnts[room]+=1
        return cnts.index(max(cnts))
