class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def dp(num):
            if num <= 3:
                return num
            
            ans = num
            for i in range(2, num):
                ans = max(ans, i * dp(num - i))
            
            return ans

        if n <= 3:
            return n - 1
        
        return dp(n)

# time n^2 There are O(n) possible states of num that dp can be called with. Due to memoization, we only calculate each state once. To calculate a state, we iterate from 2 until num, which costs up to O(n). Thus, we have a time complexity of O(n^2)
# space O(n) The recursion call stack can grow up to O(n). Also, we require O(n) space to memoize the function.