class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        cumu = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                # i不变在每一遍遍历
                cumu[j, A[j] - A[i]] = cumu.get((i, A[j] - A[i]), 1) + 1
        #print(cumu.items())
        return max(cumu.values())
    # Time complexity n^2
    # Space complexity n^2