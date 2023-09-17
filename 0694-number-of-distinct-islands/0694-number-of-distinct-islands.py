class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        def dfs(row, col, direction):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return
            if (row, col) in seen or not grid[row][col]:
                return
            seen.add((row, col))
            path_signature.append(direction)
            dfs(row + 1, col, "D")
            dfs(row - 1, col, "U")
            dfs(row, col + 1, "R")
            dfs(row, col - 1, "L")
            # appending a 0 to the string to dfs call exit to avoid error
            path_signature.append("0")

        seen = set()
        unique_islands = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                path_signature = []
                dfs(row, col, '0')
                if path_signature:
                    unique_islands.add(tuple(path_signature))
        
        return len(unique_islands)
        