class Solution:
	def countDistinct(self, s: str) -> int:
		trie, res = dict(), 0
		for i in range(len(s)):
			cur = trie
			for j in range(i,len(s)):# for substring from i to j
				if s[j] not in cur: #if current substring has not appeared previously.
					cur[s[j]] = dict()
					res+=1
				cur = cur[s[j]]
		return res

# time n^2