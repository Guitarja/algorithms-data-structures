class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        ret = max(nums) - min(nums) - 2 * k
        return 0 if ret < 0 else ret