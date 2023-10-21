class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def binary_search_left(A, x):
            left, right = 0, len(A)-1
            while left <= right:
                mid = (left + right )//2
                if x > A[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        neg = binary_search_left(nums, 0)
        pos = len(nums) - binary_search_left(nums, 1)

        return max(neg, pos)