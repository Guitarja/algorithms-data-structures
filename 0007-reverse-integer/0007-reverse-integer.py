class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -1 * self.reve(-x)
        return self.reve(x)
    
    def reve(self, i):
        res = 0
        while i != 0:
            digit = i % 10
            res = res * 10 + digit
            i = int(i / 10)
        return 0 if res > pow(2, 31) - 1 or res < -pow(2, 31) else res