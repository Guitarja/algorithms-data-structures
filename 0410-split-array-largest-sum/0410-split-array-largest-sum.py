class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def valid(nums,m,mid):
            count, curr_sum = 0, 0
            for num in nums:
                curr_sum += num
                if curr_sum > mid:
                    count += 1
                    curr_sum = num
            return (count+1) <= m
                
        lo, hi, ans = max(nums), sum(nums), -1
        while lo <= hi:
            mid = (lo + hi) //2
            # print(mid)
            # will eventually find the least number euqals to a summation
            if valid(nums,m,mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        
        return ans