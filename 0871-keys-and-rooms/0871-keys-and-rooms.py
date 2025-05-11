class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set()
        
        def dfs(r):
            visit.add(r)
            for key in rooms[r]:
                if key not in visit:
                    dfs(key)

        dfs(0)
        print(len(visit))
        return len(visit) == len(rooms)
    