import heapq
from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            return False  # cycle
        if self.rank[pa] < self.rank[pb]:
            pa, pb = pb, pa
        self.parent[pb] = pa
        if self.rank[pa] == self.rank[pb]:
            self.rank[pa] += 1
        return True


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        def can(x: int) -> bool:
            dsu = DSU(n)
            used_edges = 0
            upgrades_used = 0

            for u, v, s, must in edges:
                if must == 1:
                    if s < x:
                        return False  
                    if not dsu.union(u, v):
                        return False 
                    used_edges += 1


            free_edges = []
            upgrade_edges = []

            for u, v, s, must in edges:
                if must == 0:
                    if s >= x:
                        free_edges.append((u, v))
                    elif 2 * s >= x:
                        upgrade_edges.append((u, v))

            for u, v in free_edges:
                if dsu.union(u, v):
                    used_edges += 1
                    if used_edges == n - 1:
                        return True

            for u, v in upgrade_edges:
                if dsu.union(u, v):
                    used_edges += 1
                    upgrades_used += 1
                    if upgrades_used > k:
                        return False
                    if used_edges == n - 1:
                        return True

            return used_edges == n - 1 and upgrades_used <= k

        if n == 1:
            return 0

        max_strength = 0
        for _, _, s, _ in edges:
            max_strength = max(max_strength, 2 * s)

        left, right = 0, max_strength
        ans = -1

        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans


# class SpammingTree:
#     def __init__(self):
#         # self.u= None
#         # self.v=None
#         self.tree = defaultdict(list)
#     def addNodes(self, u, v):
#         # if u in self.tree.keys():
#         self.tree[u].append(v)

            
#     def isCycle(self, u, v):
#         visited = set()
#         def dfs(node):
#             if node == u:
#                 return True
#             visited.add(node)

#             for nei in self.tree[node]:
#                 if nei not in visited:
#                     if dfs(nei):
#                         return True
#             return False

#         return dfs(v)

# class Solution:
#     def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
#         res = []
#         if not k:
#             return -1

#         st = SpammingTree()

#         for edge in edges:
#             ui,vi,p,m = edge
                        
#             if not st.isCycle(ui,vi):    
#                 st.addNodes(ui,vi)    
#                 if m==0 and k>0:
#                     heapq.heappush(res, (p*2))
#                     k-=1
#                 elif m == 1 and k>0:
#                     heapq.heappush(res, p)
            
#             st.addNodes(ui,vi)
            
#         print(res)
#         print(st.tree)

#         return heapq.heappop(res) if res else -1
