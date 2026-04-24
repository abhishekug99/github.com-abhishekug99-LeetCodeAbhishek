class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        L = 0
        R = 0
        U = 0
        i = 0
        while i < len(moves):
            if moves[i] == 'L':
                L += 1
            elif moves[i] == 'R':
                R += 1
            else:
                U += 1
            i += 1

        pos = R - L

        if pos >= 0:
            pos += U
        else:
            pos -= U
        if pos < 0:
            return -pos
        return pos
        
        # l = moves.count('L')
        # r = moves.count('R')
        # u = moves.count('_')
        
        # return abs(r - l) + u