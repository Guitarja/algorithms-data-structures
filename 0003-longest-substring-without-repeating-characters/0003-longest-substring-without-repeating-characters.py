class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # mp stores the current index of a character
        mp = {}

        i = 0 # last repeat char index
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)

            ans = max(ans, j - i + 1)
            mp[s[j]] = j + 1

        return ans

# time n
# space min(n, n) We need O(k) space for checking a substring has no duplicate characters(mp here), where k is the size of the Set. The size of the Set is upper bounded by the size of the string n and the size of the charset/alphabet m.