class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j : i] in wordDict and dp[j] == 1:
                    dp[i] = 1
        print(dp)            
        return dp[-1]

'''
Complexity Analysis

Given nnn as the length of s, m as the length of wordDict, and k as the average length of the words in wordDict,

Time complexity: O(n⋅m⋅k)

There are nnn states of dp(i). Because of memoization, we only calculate each state once. To calculate a state, we iterate over mmm words, and for each word perform some substring operations which costs O(k). Therefore, calculating a state costs O(m⋅k), and we need to calculate O(n) states.

Space complexity: O(n)

The data structure we use for memoization and the recursion call stack can use up to O(n) space.
'''