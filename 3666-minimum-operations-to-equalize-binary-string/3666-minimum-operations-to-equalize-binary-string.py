class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        z = s.count('0')
        
        if z == 0:
            return 0
        
        if k > n:
            return -1
        
        if k == n:
            f = ''.join('1' if c == '0' else '0' for c in s)
            return 1 if f.count('0') == 0 else -1
        
        if k == 1:
            return z
        
        t = (z + k - 1) // k
        
        for ops in range(t, n + 1):
            
            totalflips = ops * k
            
            if totalflips < z:
                continue
            
            if (totalflips - z) % 2 != 0:
                continue
            
            if ops % 2 == 0:
                maxSum = z * (ops - 1) + (n - z) * ops
            else:
                maxSum = z * ops + (n - z) * (ops - 1)
            
            if totalflips <= maxSum:
                return ops
        
        return -1