class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[py] = px


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        dsu = DSU(n)

        
        for a, b in allowedSwaps:
            dsu.union(a, b)

        groups = defaultdict(list)
        for i in range(n):
            root = dsu.find(i)
            groups[root].append(i)

        hamming = 0
        for indices in groups.values():
            count = Counter(source[i] for i in indices)

            for i in indices:
                if count[target[i]] > 0:
                    count[target[i]] -= 1  
                else:
                    hamming += 1

        return hamming