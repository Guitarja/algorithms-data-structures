class NumMatrix:

    def __init__(self, matrix):
        self.rows = len(matrix)
        if self.rows == 0:
            return
        self.cols = len(matrix[0])
        self.bit = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]
        self.buildBIT(matrix)

    def lsb(self, n):
        # the line below allows us to directly capture the right most non-zero bit of a number
        return n & (-n)

    def updateBIT(self, r, c, val):
        # keep adding lsb(i) to i, lsb(j) to j and add val to bit[i][j]
        # Using two nested for loops, one for the rows and one for the columns
        i = r
        while i < self.rows + 1:
            j = c
            while j < self.cols + 1:
                self.bit[i][j] += val
                j += self.lsb(j)
            i += self.lsb(i)
        # for i in range(r, self.rows + 1, self.lsb(i)):
        #     for j in range(c, self.cols + 1, self.lsb(j)):
        #         self.bit[i][j] += val

    def queryBIT(self, r, c):
        sum_val = 0
        # keep subtracting lsb(i) to i, lsb(j) to j and obtain the final sum as the sum of non-overlapping sub-rectangles
        # Using two nested for loops, one for the rows and one for the columns
        i = r
        while i > 0:
            j = c
            while j > 0:
                sum_val += self.bit[i][j]
                j -= self.lsb(j)
            i -= self.lsb(i)

        # for i in range(r, 0, -self.lsb(i)):
        #     for j in range(c, 0, -self.lsb(j)):
        #         sum_val += self.bit[i][j]
        return sum_val

    def buildBIT(self, matrix):
        for i in range(1, self.rows + 1):
            for j in range(1, self.cols + 1):
                # call update function on each of the entries present in the matrix
                val = matrix[i - 1][j - 1]
                self.updateBIT(i, j, val)

    def update(self, row, col, val):
        old_val = self.sumRegion(row, col, row, col)
        # handling 1-based indexing
        row += 1
        col += 1
        diff = val - old_val
        self.updateBIT(row, col, diff)

    def sumRegion(self, row1, col1, row2, col2):
        # handling 1-based indexing
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1
        a = self.queryBIT(row2, col2)
        b = self.queryBIT(row1 - 1, col1 - 1)
        c = self.queryBIT(row2, col1 - 1)
        d = self.queryBIT(row1 - 1, col2)
        return (a + b) - (c + d)

'''
Time Complexity

Update (2D) - O(log⁡N⋅log⁡M)

Query (2D) - O(log⁡N⋅log⁡M)

Build (2D) - O(N⋅M⋅log⁡N⋅log⁡M)

Here N denotes the number of rows and M denotes the number of columns.

Space Complexity

O(NM)  Since we'll need an extra bit matrix to store the non-overlapping partial sums
'''

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)