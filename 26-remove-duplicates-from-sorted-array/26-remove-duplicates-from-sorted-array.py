class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        anchor = 0
        for i in range(1, len(nums), 1):
            if nums[i] != nums[anchor]:
                anchor += 1
                nums[anchor] = nums[i]
                
        
        return anchor + 1