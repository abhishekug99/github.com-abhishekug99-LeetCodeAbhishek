class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                parent[pb] = pa

        for i in range(n):
            for j in range(n):
                if lcp[i][j] > 0:
                    union(i, j)

        # Step 2: assign smallest letters
        comp_char = {}
        next_char = ord('a')
        word = [''] * n

        for i in range(n):
            root = find(i)
            if root not in comp_char:
                if next_char > ord('z'):
                    return ""
                comp_char[root] = chr(next_char)
                next_char += 1
            word[i] = comp_char[root]

        word = ''.join(word)

        dp = [[0]*n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word[i] == word[j]:
                    if i+1 < n and j+1 < n:
                        dp[i][j] = 1 + dp[i+1][j+1]
                    else:
                        dp[i][j] = 1
                else:
                    dp[i][j] = 0

        if dp == lcp:
            return word
        return ""