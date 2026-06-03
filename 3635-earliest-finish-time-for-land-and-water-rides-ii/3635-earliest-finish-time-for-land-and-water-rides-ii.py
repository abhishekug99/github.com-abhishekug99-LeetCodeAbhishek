from typing import List
from bisect import bisect_right

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        def preprocess(starts, durations):
            rides = sorted(zip(starts, durations))
            starts = [s for s, _ in rides]
            n = len(rides)

            prefix_min_dur = [0] * n
            prefix_min_dur[0] = rides[0][1]

            for i in range(1, n):
                prefix_min_dur[i] = min(
                    prefix_min_dur[i - 1],
                    rides[i][1]
                )

            suffix_min_open_finish = [0] * n
            suffix_min_open_finish[-1] = (
                rides[-1][0] + rides[-1][1]
            )

            for i in range(n - 2, -1, -1):
                suffix_min_open_finish[i] = min(
                    suffix_min_open_finish[i + 1],
                    rides[i][0] + rides[i][1]
                )

            return (
                starts,
                prefix_min_dur,
                suffix_min_open_finish,
            )

        water_data = preprocess(
            waterStartTime,
            waterDuration
        )

        land_data = preprocess(
            landStartTime,
            landDuration
        )

        def best_second_ride(finish_time, data):
            starts, prefix_min_dur, suffix_min_open_finish = data
            n = len(starts)

            pos = bisect_right(starts, finish_time) - 1

            ans = float("inf")

            # rides already open
            if pos >= 0:
                ans = min(
                    ans,
                    finish_time + prefix_min_dur[pos]
                )

            # rides opening later
            if pos + 1 < n:
                ans = min(
                    ans,
                    suffix_min_open_finish[pos + 1]
                )

            return ans

        ans = float("inf")

        # Land -> Water
        for ls, ld in zip(landStartTime, landDuration):
            land_finish = ls + ld
            ans = min(
                ans,
                best_second_ride(land_finish, water_data)
            )

        # Water -> Land
        for ws, wd in zip(waterStartTime, waterDuration):
            water_finish = ws + wd
            ans = min(
                ans,
                best_second_ride(water_finish, land_data)
            )

        return ans