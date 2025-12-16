from typing import List
from collections import defaultdict
import math

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        tree = [[] for _ in range(n)]
        for b, e in hierarchy:
            tree[b - 1].append(e - 1)  
        def merge(A, B):
            # knapsack merge: A and B are max-profit arrays
            merged = [-math.inf] * (budget + 1)
            for i in range(budget + 1):
                if A[i] == -math.inf:
                    continue
                for j in range(budget - i + 1):
                    if B[j] == -math.inf:
                        continue
                    merged[i + j] = max(merged[i + j], A[i] + B[j])
            return merged

        def dfs(u: int):
            """
            returns (dp0, dp1)
            dp0[b] = max profit in u-subtree with budget b if parent NOT bought
            dp1[b] = max profit in u-subtree with budget b if parent IS bought
            """
            # children-only contributions
            # if u not bought -> children see "parent not bought"
            children_no = [0] + [-math.inf] * budget
            # if u bought -> children see "parent bought"
            children_yes = [0] + [-math.inf] * budget

            for v in tree[u]:
                v0, v1 = dfs(v)
                children_no = merge(children_no, v0)   # u not bought => child parent not bought
                children_yes = merge(children_yes, v1) # u bought     => child parent bought

            # Start with "don't buy u" for both states:
            dp0 = children_no[:]  # parent not bought, u not bought
            dp1 = children_no[:]  # parent bought, u not bought (still no child discount)

            # Option: buy u (then children must use children_yes)
            full = present[u]
            half = present[u] // 2

            # parent NOT bought => u pays full
            if full <= budget:
                profit_full = future[u] - full
                for b in range(full, budget + 1):
                    if children_yes[b - full] != -math.inf:
                        dp0[b] = max(dp0[b], children_yes[b - full] + profit_full)

            # parent IS bought => u pays half
            if half <= budget:
                profit_half = future[u] - half
                for b in range(half, budget + 1):
                    if children_yes[b - half] != -math.inf:
                        dp1[b] = max(dp1[b], children_yes[b - half] + profit_half)

            return dp0, dp1

        # Employee 1 (index 0) is CEO, so no parent => no discount at root
        root0, _ = dfs(0)
        return max(root0)
