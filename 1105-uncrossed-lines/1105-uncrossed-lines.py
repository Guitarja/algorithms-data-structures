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

# Time complexity: O(n1⋅n2)
# Initializing the memo array takes O(n1⋅n2)time.
# It will take O(n1⋅n2) because there are O(n1⋅n2)states to iterate over. The recursive function may be called multiple times for a given state, but due to memoization, each state is only computed once.

# Space complexity: O(n1⋅n2)