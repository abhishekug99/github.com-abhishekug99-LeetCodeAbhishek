from typing import List
from collections import defaultdict, deque

class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        max_val = max(nums)

        # Sieve
        is_prime = [True] * (max_val + 1)
        if max_val >= 0:
            is_prime[0] = False
        if max_val >= 1:
            is_prime[1] = False

        for i in range(2, int(max_val ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, max_val + 1, i):
                    is_prime[j] = False

        # value -> indices
        value_indices = defaultdict(list)
        for i, x in enumerate(nums):
            value_indices[x].append(i)

        # only primes present in nums can be used for teleport
        prime_sources = set(x for x in nums if is_prime[x])

        div_map = {}

        for p in prime_sources:
            div_map[p] = []
            for multiple in range(p, max_val + 1, p):
                if multiple in value_indices:
                    div_map[p].extend(value_indices[multiple])

        # BFS
        q = deque([0])
        visited = [False] * n
        visited[0] = True
        steps = 0
        used_prime = set()

        while q:
            for _ in range(len(q)):
                i = q.popleft()

                if i == n - 1:
                    return steps

                # move left
                if i - 1 >= 0 and not visited[i - 1]:
                    visited[i - 1] = True
                    q.append(i - 1)

                # move right
                if i + 1 < n and not visited[i + 1]:
                    visited[i + 1] = True
                    q.append(i + 1)

                # teleport
                val = nums[i]
                if is_prime[val] and val not in used_prime:
                    used_prime.add(val)

                    for nxt in div_map[val]:
                        if not visited[nxt]:
                            visited[nxt] = True
                            q.append(nxt)

                    # free memory
                    div_map[val] = []

            steps += 1

        return -1