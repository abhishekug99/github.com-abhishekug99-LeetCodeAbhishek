class Solution:
    def longestBalanced(self, s: str) -> int:
        N = len(s)
        a = [[0, 0, 0]]
        for c in s:
            a.append(a[-1][:])
            a[-1]["abc".index(c)] += 1

        ans = 0
        d = {}
        for i, (a, b, c) in enumerate(a):
            for key in [
                ("abc", a - b, a - c),
                ("ab", a - b, c),
                ("bc", b - c, a),
                ("ca", c - a, b),
                ("a", b, c),
                ("b", c, a),
                ("c", a, b),
            ]:
                ans = max(ans, i - d.get(key, i))
                d.setdefault(key, i)

        return ans