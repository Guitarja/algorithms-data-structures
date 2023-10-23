class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        
        # Product matrix.
        ans = [[0] * len(mat2[0]) for _ in range(len(mat1))]
        
        for row_index, row_elements in enumerate(mat1):
            for element_index, row_element in enumerate(row_elements):
                # If current element of mat1 is non-zero then iterate over all columns of mat2.
                if row_element:
                    for col_index, col_element in enumerate(mat2[element_index]):
                        ans[row_index][col_index] += row_element * col_element
        
        return ans

# Let m and k represent the number of rows and columns in mat1, respectively. Likewise, let k and n represent the number of rows and columns in mat2, respectively.

# Time complexity: O(m⋅k⋅n)

# We iterate over all m⋅k elements of the matrix mat1mat1mat1.
# For each element of matrix mat1mat1mat1, we iterate over all n columns of the matrix mat2mat2mat2.
# Thus, it leads to a time complexity of m⋅k⋅n
# Space complexity: O(1)

# We use a matrix ansansans of size m×n to output the multiplication result which is not included in auxiliary space.