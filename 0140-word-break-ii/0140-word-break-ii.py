class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.helper(s, wordDict, {})
    
    def helper(self, s, wordDict, memo):
        if s in memo:
            return memo[s]
        if not s:
            return []
        
        res = []
        
        for word in wordDict:
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                res.append(word)
            else:
                rest = self.helper(s[len(word):], wordDict, memo)
                for item in rest:
                    res.append(word + ' ' + item)
        memo[s] = res
        return memo[s]
# Time complexity: O(n^3). Size of recursion tree can go up to n^2. The creation of the 'res' List takes n time.

