class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cnts = Counter(moves)
        f=False
        if len(cnts)==1:
            return False
        if cnts['R'] == cnts['L']:
            f=True
        if cnts['U'] == cnts['D']:
            f = True
        if cnts['R'] == cnts['L'] and cnts['U'] == cnts['D']:
            f =  True
        else:
            f = False
        return f
        



