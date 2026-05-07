class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        preMax = [0] * n
        preMax[0] = nums[0]

        for i in range(1, n):
            preMax[i] = max(preMax[i - 1], nums[i])

        ans = [0] * n
        sufMin = float("inf")

        for i in range(n - 1, -1, -1):
            if i + 1 < n and preMax[i] > sufMin:
                ans[i] = ans[i + 1]
            else:
                ans[i] = preMax[i]

            sufMin = min(sufMin, nums[i])

        return ans
        # n = len(nums)
        # dsu = DSU(n)

        # stack = []
        # for i in range(n):
        #     while stack and nums[stack[-1]] > nums[i]:
        #         top = stack.pop()
        #         dsu.union(top, i)
        #         if stack:
        #             dsu.union(top, stack[-1])  
        #     stack.append(i)

        # stack = []
        # for i in range(n - 1, -1, -1):
        #     while stack and nums[stack[-1]] < nums[i]:
        #         dsu.union(stack.pop(), i)
        #     stack.append(i)

        # comp_max = {}
        # for i in range(n):
        #     root = dsu.find(i)
        #     comp_max[root] = max(comp_max.get(root, 0), nums[i])

        # return [comp_max[dsu.find(i)] for i in range(n)]