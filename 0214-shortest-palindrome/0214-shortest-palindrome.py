class Solution:
    def shortestPalindrome(self, s: str) -> str:
        sr = s[::-1]
        for i in range(len(s)+1):
            if s.startswith(sr[i:]):
                return sr[:i] + s
        
        return 0
# time I think is less than n^2
# space n