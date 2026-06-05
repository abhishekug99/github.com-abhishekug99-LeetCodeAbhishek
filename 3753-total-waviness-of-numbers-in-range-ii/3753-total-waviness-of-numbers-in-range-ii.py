class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def count_upto(x):
            if x <= 0:
                return 0

            s = str(x)
            n = len(s)

            @cache
            def dp(pos, prev1, prev2, length, tight):
                if pos == n:
                    return (1, 0)  

                limit = int(s[pos]) if tight else 9

                total_cnt = 0
                total_wavy = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    # still leading zeros
                    if length == 0 and d == 0:
                        cnt, wav = dp(pos + 1, 10, 10, 0, ntight)
                        total_cnt += cnt
                        total_wavy += wav
                        continue

                    if length == 0:
                        cnt, wav = dp(pos + 1, d, 10, 1, ntight)

                    elif length == 1:
                        cnt, wav = dp(pos + 1, d, prev1, 2, ntight)

                    else:
                        add = 1 if (
                            (prev1 > prev2 and prev1 > d)
                            or
                            (prev1 < prev2 and prev1 < d)
                        ) else 0

                        cnt, wav = dp(pos + 1, d, prev1, 2, ntight)

                        wav += add * cnt

                    total_cnt += cnt
                    total_wavy += wav

                return (total_cnt, total_wavy)

            return dp(0, 10, 10, 0, True)[1]

        return count_upto(num2) - count_upto(num1 - 1)