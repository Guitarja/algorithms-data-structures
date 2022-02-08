class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first = 0):
            if first == n:
                ans.append(nums[:])
            
            for i in range(first, n):
                # place the i-th integer first in current permutation
                nums[i], nums[first] = nums[first], nums[i]
                
                backtrack(first + 1)
                
                nums[first], nums[i] = nums[i], nums[first]
        ans = []
        n = len(nums)
        backtrack()
        return ans