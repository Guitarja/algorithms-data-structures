class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)

        memo = {}

        def solve(i, j):
            if i > n1 - 1 or j > n2 - 1:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if nums1[i] == nums2[j]:
                memo[(i, j)] = 1 + solve(i + 1, j + 1)
            else:
                memo[(i, j)] = max(solve(i + 1, j), solve(i, j + 1))
            return memo[(i, j)]

        return solve(0, 0)