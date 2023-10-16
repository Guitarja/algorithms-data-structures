class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        maxi, mini = -math.inf, math.inf
        
        for a, b in zip(nums, nums[1:]):
            maxi = max(min(a, b), maxi)
            mini = min(max(a, b), mini)
        change = max(0, (maxi - mini) * 2)
        
        # solving the boundary situation
        for a, b in zip(nums, nums[1:]):
            tmp1 = - abs(a - b) + abs(nums[0] - b)
            tmp2 = - abs(a - b) + abs(nums[-1] - a)
            change = max([tmp1, tmp2, change])
			
        original_value = sum(abs(a - b) for a, b in zip(nums, nums[1:]))
        return  original_value + change

# https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/solutions/489882/o-n-solution-with-explanation/