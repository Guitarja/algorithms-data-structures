class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        ones = 0
        for i in range(32 + 1):
            ones += n & 1
            n = n >> 1
        
        return ones == 1
