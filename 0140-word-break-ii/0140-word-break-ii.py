class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = collections.defaultdict(list)

        def _word_break(s):
            if not s:
                return [[]]
            if s in memo:
                return memo[s]
            
            for end_index in range(1, len(s) + 1):
                word = s[:end_index]
                if word in word_set:
                    for subsentence in _word_break(s[end_index:]):
                        memo[s].append([word]+subsentence)
            return memo[s]
        
        _word_break(s) 

        return [" ".join(words) for words in memo[s]]

# Let N be the length of the input string and W be the number of words in the dictionary.

# Time Complexity: O(N^2+2N+W)
# Space Complexity: O(2^N⋅N+W)