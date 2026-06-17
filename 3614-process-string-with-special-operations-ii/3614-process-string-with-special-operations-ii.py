class Solution:
    def processStr(self, s: str, k: int) -> str:
        lengths = []

        cur_len = 0

        for ch in s:
            lengths.append(cur_len)

            if ch.isalpha() and ch.islower():
                cur_len += 1

            elif ch == '#':
                cur_len *= 2

            elif ch == '%':
                pass

            elif ch == '*':
                if cur_len:
                    cur_len -= 1

        if k >= cur_len:
            return '.'

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            cur_before = lengths[i]

            if ch.isalpha() and ch.islower():
                if k == cur_before:
                    return ch

            elif ch == '#':
                if k >= cur_before:
                    k -= cur_before

            elif ch == '%':
                k = cur_len - 1 - k

            elif ch == '*':
                pass

            cur_len = cur_before

        return '.'
        # res = []
        # for c in s:
        #     if c.isalpha() and c.islower():
        #         res.append(c)

        #     elif c == '#':
        #         res.extend(res)

        #     elif c == '%':
        #         res.reverse()

        #     elif c == '*':
        #         if res:
        #             res.pop()

        # if k<len(res):
        #     return res[k]
        # else:
        #     return '.'

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna