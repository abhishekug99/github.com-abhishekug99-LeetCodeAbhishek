class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set()
        
        def dfs(r):
            visit.add(r)
            for key in rooms[r]:
                if key not in visit:
                    dfs(key)


            
        # dfs(grid, r+1, visit)
            # res.append(dfs(grid, r-1, c, visit))
            # res.append(dfs(grid, r, c+1, visit))
            # res.append(dfs(grid, r, c-1, visit))
        dfs(0)
        return len(visit) == len(rooms)
    