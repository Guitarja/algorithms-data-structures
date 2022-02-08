import numpy as np
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # https://leetcode.com/problems/rotate-image/discuss/18872/A-common-method-to-rotate-the-image
        
        matrix[:] = np.rot90(matrix, 3)