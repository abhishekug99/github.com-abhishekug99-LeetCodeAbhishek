class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        res = []
        n = len(code)
        valids ={"electronics":[], "grocery":[], "pharmacy":[], "restaurant":[]}
        for i in range(len(code)):
            if code[i] and re.fullmatch(r"[\w]+", code[i]) and businessLine[i] in valids and isActive[i]==True:
                valids[businessLine[i]].append(code[i])
            else:
                continue

        for key in ["electronics", "grocery", "pharmacy", "restaurant"]:
            if valids[key]:
                valids[key].sort()
                res.extend(valids[key])
        return res