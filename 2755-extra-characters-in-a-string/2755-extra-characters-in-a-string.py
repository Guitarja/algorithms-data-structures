class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n, dictionary_set = len(s), set(dictionary)
        @cache
        def dp(start):
            if start == n:
                return 0
            # To count this character as a left over character 
            # move to index 'start + 1'
            ans = dp(start + 1) + 1
            for end in range(start, n):
                curr = s[start: end + 1]
                if curr in dictionary_set:
                    ans = min(ans, dp(end + 1))
            return ans
            
        return dp(0)

# Let N be the total characters in the string.
# Let M be the average length of the strings in dictionary.
# Let K be the length of the dictionary.

# time complexity: N^3
# space complexity: N+M*K