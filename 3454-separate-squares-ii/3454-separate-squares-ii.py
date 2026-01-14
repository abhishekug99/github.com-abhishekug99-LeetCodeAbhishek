from typing import List
import bisect

class Solution:
    #not my solution
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []
        xs = []

        # Build y-events and collect x endpoints
        for x, y, l in squares:
            x1, x2 = x, x + l
            y1, y2 = y, y + l
            events.append((y1, 1, x1, x2))   # add
            events.append((y2, -1, x1, x2))  # remove
            xs.append(x1)
            xs.append(x2)

        if not events:
            return 0.0

        xs = sorted(set(xs))
        # Segment tree is built over x-interval segments between xs[i] and xs[i+1]
        # There are len(xs)-1 segments.
        nseg = len(xs) - 1
        if nseg <= 0:
            return 0.0

        # Segment tree arrays
        # cover[idx] = how many active intervals cover this node fully
        # length[idx] = total covered length in this node
        cover = [0] * (4 * nseg)
        length = [0.0] * (4 * nseg)

        def pull(idx: int, l: int, r: int) -> None:
            """Recompute length[idx] from cover and children."""
            if cover[idx] > 0:
                # fully covered
                length[idx] = xs[r + 1] - xs[l]
            elif l == r:
                length[idx] = 0.0
            else:
                length[idx] = length[idx * 2] + length[idx * 2 + 1]

        def update(idx: int, l: int, r: int, ql: int, qr: int, delta: int) -> None:
            if ql <= l and r <= qr:
                cover[idx] += delta
                pull(idx, l, r)
                return
            mid = (l + r) // 2
            if ql <= mid:
                update(idx * 2, l, mid, ql, qr, delta)
            if qr > mid:
                update(idx * 2 + 1, mid + 1, r, ql, qr, delta)
            pull(idx, l, r)

        # Sort events by y
        events.sort()

        # First pass: compute total union area
        total_area = 0.0
        prev_y = events[0][0]
        i = 0
        cur_cover_len = 0.0

        while i < len(events):
            y = events[i][0]
            dy = y - prev_y
            if dy != 0:
                total_area += cur_cover_len * dy
                prev_y = y

            # apply all events at this y
            while i < len(events) and events[i][0] == y:
                _, typ, x1, x2 = events[i]
                lidx = bisect.bisect_left(xs, x1)
                ridx = bisect.bisect_left(xs, x2) - 1  # inclusive segment index
                if lidx <= ridx:
                    update(1, 0, nseg - 1, lidx, ridx, typ)
                i += 1

            cur_cover_len = length[1]

        target = total_area / 2.0

        # Second pass: find Y where area reaches target
        cover = [0] * (4 * nseg)
        length = [0.0] * (4 * nseg)
        cur_cover_len = 0.0
        area_so_far = 0.0
        prev_y = events[0][0]
        i = 0

        while i < len(events):
            y = events[i][0]
            dy = y - prev_y

            if dy != 0:
                strip_area = cur_cover_len * dy
                if area_so_far + strip_area >= target:
                    # answer lies within (prev_y, y)
                    if cur_cover_len == 0:
                        # If there's no coverage, area doesn't grow in this strip.
                        # But then we wouldn't reach target here; still keep safe.
                        return float(prev_y)
                    return float(prev_y + (target - area_so_far) / cur_cover_len)

                area_so_far += strip_area
                prev_y = y

            while i < len(events) and events[i][0] == y:
                _, typ, x1, x2 = events[i]
                lidx = bisect.bisect_left(xs, x1)
                ridx = bisect.bisect_left(xs, x2) - 1
                if lidx <= ridx:
                    update(1, 0, nseg - 1, lidx, ridx, typ)
                i += 1

            cur_cover_len = length[1]

        # If target is exactly total area (edge case), return max y
        return float(prev_y)
