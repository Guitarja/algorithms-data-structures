class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i**2 for i in range(int(math.sqrt(n)+1))]

        dp = [inf] * (n+1)
        dp[0] = 0

        for i in range(1, n+1):
            for sqaure in square_nums:
                if i < sqaure:
                    break
                dp[i] = min(dp[i], dp[i-sqaure] + 1)
        return dp[-1]

#Complexity

# Time complexity: O(n⋅sqrt(n)). In main step, we have a nested loop, where the outer loop is of nnn iterations and in the inner loop it takes at maximum sqrt(n)iterations.

# Space Complexity: O(n). We keep all the intermediate sub-solutions in the array dp[].