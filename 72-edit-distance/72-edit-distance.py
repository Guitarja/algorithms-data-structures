class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def minD (word1: str, word2: str, i: int, j: int, memo: dict):
            if i == len(word1) and j == len(word2):
                return 0
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i
            if (i, j) not in memo:
                if word1[i] == word2[j]:
                    ans = minD(word1, word2, i + 1, j + 1, memo)
                else:
                    insert = 1 + minD(word1, word2, i, j + 1, memo)
                    delete = 1 + minD(word1, word2, i + 1, j, memo)
                    replace = 1 + minD(word1, word2, i + 1, j + 1, memo)

                    ans = min(insert, delete, replace)
                memo[(i, j)] = ans
            return memo[(i, j)]
        memo = dict()
        return minD(word1, word2, 0, 0, memo)
    # detailed solution from recursive to dp: https://leetcode.com/problems/edit-distance/discuss/159295/Python-solutions-and-intuition