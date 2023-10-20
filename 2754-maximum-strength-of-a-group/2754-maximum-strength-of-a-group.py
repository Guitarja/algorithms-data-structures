class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1:
            return nums[0]
        res = 1
        neg_count = 0
        largest = float('-inf')
        largest_negative = float('-inf')
        for num in nums:
            largest = max(num, largest)
            if num:
                res *= num
            if num < 0:
                largest_negative = max(largest_negative, num)
                neg_count += 1
        if largest == 0 and (neg_count == 1 or neg_count == 0):
            return 0
        return res if res > 0 else res//largest_negative