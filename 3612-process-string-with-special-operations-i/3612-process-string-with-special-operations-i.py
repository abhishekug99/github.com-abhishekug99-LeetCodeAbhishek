class Solution:
    def processStr(self, s: str) -> str:
        res = []
        for c in s:
            if c.isalpha() and c.islower():
                res.append(c)

            elif c == '#':
                res.extend(res)

            elif c == '%':
                res.reverse()

            elif c == '*':
                if res:
                    res.pop()

        return ''.join(res)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna