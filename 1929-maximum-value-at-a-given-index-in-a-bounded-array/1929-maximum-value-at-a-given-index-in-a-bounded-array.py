class Solution:
    def getSum(self, index: int, value: int, n: int) -> int:
        count = 0
        
        # On index's left:
        # If value > index, there are index + 1 numbers in the arithmetic sequence:
        # [value - index, ..., value - 1, value].
        # Otherwise, there are value numbers in the arithmetic sequence:
        # [1, 2, ..., value - 1, value], plus a sequence of length (index - value + 1) of 1s. 
        if value > index:
            count += (value + value - index) * (index + 1) // 2
        else:
            count += (value + 1) * value // 2 + index - value + 1
        
        # On index's right:
        # If value >= n - index, there are n - index numbers in the arithmetic sequence:
        # [value, value - 1, ..., value - n + 1 + index].
        # Otherwise, there are value numbers in the arithmetic sequence:
        # [value, value - 1, ..., 1], plus a sequence of length (n - index - value) of 1s. 
        if value >= n - index:
            count += (value + value - n + 1 + index) * (n - index) // 2
        else:
            count += (value + 1) * value // 2 + n - index - value
        
        return count - value
    
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left, right = 1, maxSum
        while left <= right:
            mid = left + (right - left) // 2
            if self.getSum(index, mid, n) <= maxSum:
                left = mid + 1
            else:
                right = mid - 1
        
        return left - 1

# Time complexity: O(log⁡(maxSum))

# We set the searching space as [1, maxSum], thus it takes O(log⁡(maxSum))steps to finish the binary search.

# At each step, we made some calculations that take O(1) time.

# Space complexity: O(1)

# Both the binary search and the getSum function take O(1) space.