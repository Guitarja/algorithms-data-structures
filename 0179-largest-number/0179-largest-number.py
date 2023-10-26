class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num

# the number 9534303, while the correct answer can be achieved by transposing
# the 3 and the 30. Therefore, for each pairwise comparison during the
# sort, we compare the numbers achieved by concatenating the pair in both
# orders.