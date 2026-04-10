class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = defaultdict(list)

        for i, x in enumerate(nums):
            pos[x].append(i)

        res = float('inf')

        for li in pos.values():
            if len(li) >= 3:
                for i in range(len(li) - 2):
                    dist = 2 * (li[i+2] - li[i])
                    res = min(res, dist)

        return res if res != float('inf') else -1
