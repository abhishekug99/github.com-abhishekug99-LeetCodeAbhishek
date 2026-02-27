class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        z = s.count('0')
        
        if z == 0:
            return 0
        
        if k > n:
            return -1
        
        if k == n:
            flipped = ''.join('1' if c == '0' else '0' for c in s)
            return 1 if flipped.count('0') == 0 else -1
        
        if k == 1:
            return z
        
        t = (z + k - 1) // k
        
        for ops in range(t, n + 1):
            
            total_flips = ops * k
            
            if total_flips < z:
                continue
            
            if (total_flips - z) % 2 != 0:
                continue
            
            if ops % 2 == 0:
                max_sum = z * (ops - 1) + (n - z) * ops
            else:
                max_sum = z * ops + (n - z) * (ops - 1)
            
            if total_flips <= max_sum:
                return ops
        
        return -1