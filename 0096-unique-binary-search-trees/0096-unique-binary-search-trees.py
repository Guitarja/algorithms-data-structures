class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[0] = 1 #base case, if tree is empty
        dp[1] = 1 #if only one node
        
        for i in range(2, n + 1):
            # number of nodes from 2 to n
            for j in range(1, i + 1):
                # root picked from 0 to i
                dp[i] += dp[j-1] * dp[i-j]
        
        return dp[-1]

# F(i,n)=G(i−1)⋅G(n−i)

# G(n)=∑i-n G(i−1)⋅G(n−i)

# Complexity Analysis

# Time complexity : n^2
# Space complexity : O(N)