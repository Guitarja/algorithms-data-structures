class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        p = 1
        for i in range(1,n):
            # here i represent number of alive people
            # p is f(i,'cac')
            p=(k+p-1)%(i+1)+1
            # p is f(i+1, 'cac')
        return p
# https://leetcode.com/problems/find-the-winner-of-the-circular-game/solutions/1152585/o-n-o-klg-n-with-table-explanation/

'''
simulation:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = list(range(n))
        i = 0 
        while len(nums) > 1: 
            i = (i + k-1) % len(nums)
            nums.pop(i)
        return nums[0] + 1
'''