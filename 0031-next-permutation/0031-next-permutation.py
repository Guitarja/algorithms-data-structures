class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # https://leetcode.com/problems/next-permutation/discuss/14054/Python-solution-with-comments.
        
        i = j = len(nums) - 1
        # finding the first decressing element
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()
            return
        # finding the number just lagter than i - 1
        k = i - 1
        while nums[j] <= nums[k]:
             j -= 1
        nums[k], nums[j] = nums[j], nums[k]
        # reverse the second part
        l, r = k + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
# time n
# space 1