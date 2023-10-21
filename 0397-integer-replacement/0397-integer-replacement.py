class Solution:
    def integerReplacement(self, n: int) -> int:
        memo = {1:0}
        return self.recRep(n, memo)
        
    def recRep(self, n, memo):
        if n in memo:
            return memo[n]
        if n % 2:
            memo[n] = 1 + min(self.recRep(n+1, memo), self.recRep(n-1, memo))
            return memo[n]
        else:
            memo[n] = 1 + self.recRep(n/2, memo)
            return memo[n]
 
# Time Complexity: O(n)  the time complexity depends on how many unique values of n are encountered during the recursive calls.
# Space Complexity: O(n)