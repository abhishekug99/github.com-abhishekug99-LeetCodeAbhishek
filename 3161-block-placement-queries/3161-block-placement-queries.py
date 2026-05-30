from sortedcontainers import SortedList

class SegTree:
    def __init__(self, n):
        self.n = n
        self.seg = [0] * (4 * n)

    def update(self, idx, val, node, l, r):
        if l == r:
            self.seg[node] = val
            return

        mid = (l + r) // 2

        if idx <= mid:
            self.update(idx, val, node * 2, l, mid)
        else:
            self.update(idx, val, node * 2 + 1, mid + 1, r)

        self.seg[node] = max(
            self.seg[node * 2],
            self.seg[node * 2 + 1]
        )

    def query(self, ql, qr, node, l, r):
        if qr < l or r < ql:
            return 0

        if ql <= l and r <= qr:
            return self.seg[node]

        mid = (l + r) // 2

        return max(
            self.query(ql, qr, node * 2, l, mid),
            self.query(ql, qr, node * 2 + 1, mid + 1, r)
        )


class Solution:
    def getResults(self, queries):

        positions = {0}

        for q in queries:
            positions.add(q[1])

        coords = sorted(positions)

        idx = {x: i for i, x in enumerate(coords)}

        # all obstacles existing at the end
        obstacles = SortedList([0])

        for q in queries:
            if q[0] == 1:
                obstacles.add(q[1])

        m = len(coords)

        seg = SegTree(m)

        # initialize gaps
        for i in range(1, len(obstacles)):
            cur = obstacles[i]
            prev = obstacles[i - 1]

            seg.update(
                idx[cur],
                cur - prev,
                1,
                0,
                m - 1
            )

        ans = []

        for q in reversed(queries):

            if q[0] == 2:

                x, sz = q[1], q[2]

                pos = obstacles.bisect_right(x) - 1

                last_obs = obstacles[pos]

                compressed = idx[last_obs]

                best = seg.query(
                    0,
                    compressed,
                    1,
                    0,
                    m - 1
                )

                best = max(best, x - last_obs)

                ans.append(best >= sz)

            else:

                x = q[1]

                p = obstacles.bisect_left(x)

                prev_obs = obstacles[p - 1]

                nxt_obs = (
                    obstacles[p + 1]
                    if p + 1 < len(obstacles)
                    else None
                )

                obstacles.remove(x)

                if nxt_obs is not None:
                    seg.update(
                        idx[nxt_obs],
                        nxt_obs - prev_obs,
                        1,
                        0,
                        m - 1
                    )

                seg.update(
                    idx[x],
                    0,
                    1,
                    0,
                    m - 1
                )

        return ans[::-1]