class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        ones = 0
        for i in range(32 + 1):
            ones += n & 1
            n = n >> 1
        
        return ones == 1
# idea is that a power of two in binary form has and only has one "1".
# 1=(00000001) 
# 2=(00000010)22 = (0000 0010)_22=(00000010) 
# 4=(00000100)24 = (0000 0100)_24=(00000100) 
# 8=(00001000)28 = (0000 1000)_28=(00001000)
