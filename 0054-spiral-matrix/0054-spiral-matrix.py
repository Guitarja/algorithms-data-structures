class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0]) # Initial possible number of steps
        direction = 1 # Start off going right
        i, j = 0, -1
        output = []
        while m*n > 0:
            for _ in range(n): # Move horizaontally
                j += direction
                output.append(matrix[i][j])
            m -= 1
            for _ in range(m): # Move vertically
                i += direction
                output.append(matrix[i][j])
            n -= 1
            direction *= -1 # Flip direction
        return output