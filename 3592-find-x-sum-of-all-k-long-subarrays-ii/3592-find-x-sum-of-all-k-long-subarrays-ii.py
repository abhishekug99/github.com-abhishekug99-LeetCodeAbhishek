from typing import List
import heapq

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        if k > n:
            return []
        # Frequency map in the current window
        cnt = {}

        # Heaps and membership for the top-X set
        top_heap = []          # (count, value)  -> worst of top at heap[0]
        rest_heap = []         # (-count, -value)-> best of rest at heap[0]
        top_members = set()    # values currently considered in top-X
        score = 0              # sum(v * cnt[v] for v in top_members)

        def add_to_top(v):
            nonlocal score
            top_members.add(v)
            heapq.heappush(top_heap, (cnt[v], v))
            score += v * cnt[v]

        def remove_from_top(v):
            """Move v out of top-members; caller will push it into rest if needed."""
            nonlocal score
            if v in top_members:
                score -= v * cnt.get(v, 0)
                top_members.remove(v)

        def add_to_rest(v):
            heapq.heappush(rest_heap, (-cnt[v], -v))

        def clean_top():
            """Pop stale entries from top_heap (lazy deletion)."""
            while top_heap:
                c, v = top_heap[0]
                # stale if v not considered in top, or count changed
                if v not in top_members or cnt.get(v, 0) != c:
                    heapq.heappop(top_heap)
                else:
                    break

        def clean_rest():
            """Pop stale entries from rest_heap (lazy deletion)."""
            while rest_heap:
                nc, nv = rest_heap[0]
                c, v = -nc, -nv
                # stale if v moved into top, or count changed, or vanished
                if v in top_members or cnt.get(v, 0) != c:
                    heapq.heappop(rest_heap)
                else:
                    break

        def worst_top():
            """Return (count, value) of the current worst in top, or None."""
            clean_top()
            if not top_heap:
                return None
            return top_heap[0]

        def best_rest():
            """Return (count, value) of the current best in rest, or None."""
            clean_rest()
            if not rest_heap:
                return None
            nc, nv = rest_heap[0]
            return (-nc, -nv)

        def target_size():
            """Desired size of top_members = min(x, #distinct)."""
            return min(x, len(cnt))

        def move_best_rest_to_top():
            """Promote the best from rest to top."""
            clean_rest()
            if not rest_heap:
                return False
            nc, nv = heapq.heappop(rest_heap)
            c, v = -nc, -nv
            # validate again (it can become stale between clean and pop)
            if cnt.get(v, 0) != c or v in top_members or c == 0:
                return False
            add_to_top(v)
            return True

        def move_worst_top_to_rest():
            """Demote the worst from top to rest."""
            clean_top()
            if not top_heap:
                return False
            c, v = heapq.heappop(top_heap)
            # validate
            if v not in top_members or cnt.get(v, 0) != c or c == 0:
                return False
            # move out of top and into rest
            remove_from_top(v)
            add_to_rest(v)
            return True

        def rebalance():
            """
            Ensure:
              - |top_members| == target_size()
              - If best(rest) outranks worst(top), swap until stable.
            """
            # First, bring size to target
            t = target_size()
            while len(top_members) < t:
                if not move_best_rest_to_top():
                    break
            while len(top_members) > t:
                if not move_worst_top_to_rest():
                    break

            # Then, swap while improving
            while True:
                wt = worst_top()
                br = best_rest()
                if wt is None or br is None:
                    break
                tc, tv = wt
                rc, rv = br
                # Promote if (rc, rv) better than (tc, tv) in (count desc, value desc)
                if (rc > tc) or (rc == tc and rv > tv):
                    # demote worst top
                    heapq.heappop(top_heap)  # pop the stale worst
                    remove_from_top(tv)
                    add_to_rest(tv)
                    # promote best rest
                    heapq.heappop(rest_heap)
                    add_to_top(rv)
                    # keep looping to ensure global consistency
                else:
                    break

        # Initialize first window
        for v in nums[:k]:
            cnt[v] = cnt.get(v, 0) + 1
        # Put everything in rest, then promote the top x
        for v in cnt:
            add_to_rest(v)
        rebalance()
        res = [score]

        # Slide the window
        for i in range(k, n):
            out_v = nums[i - k]
            in_v  = nums[i]

            # Decrement out_v
            if out_v in cnt:
                old = cnt[out_v]
                new = old - 1
                if out_v in top_members:
                    # adjust score for the change in count
                    # delta = out_v * (new - old) = -out_v
                    # generalized for clarity:
                    delta = out_v * (new - old)
                    # score is always valid for current top_members
                    # (even if heaps have stale entries)
                    nonlocal_score = score  # keep linter calm in some environments
                    score += delta  # type: ignore
                if new == 0:
                    # remove entirely
                    del cnt[out_v]
                    if out_v in top_members:
                        # already subtracted above; now drop membership
                        top_members.remove(out_v)
                    # no heap push for zero count
                else:
                    cnt[out_v] = new
                    # push updated record to whichever set it currently belongs to
                    if out_v in top_members:
                        heapq.heappush(top_heap, (new, out_v))
                    else:
                        heapq.heappush(rest_heap, (-new, -out_v))

            # Increment in_v
            old = cnt.get(in_v, 0)
            new = old + 1
            if in_v in top_members:
                delta = in_v * (new - old)
                score += delta
            cnt[in_v] = new
            if in_v in top_members:
                heapq.heappush(top_heap, (new, in_v))
            else:
                heapq.heappush(rest_heap, (-new, -in_v))

            # Rebalance after both updates
            rebalance()
            res.append(score)

        return res



#works well n*klog(k) time but not accepted
# class Solution:
#     def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        
#         res = []
#         for i in range(len(nums)-k+1):
#             cnts = Counter(nums[i:i+k])
#             sortedSub = sorted(cnts.items(), key=lambda x: (x[1], x[0]), reverse=True)
#             print(sortedSub)
#             topX = sortedSub[:x]
#             curSum = 0
#             for key,v in topX:
#                     curSum+= key*v
            
#             res.append(curSum)
#         return res