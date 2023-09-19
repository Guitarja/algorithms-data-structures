class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        X, Y = tuple(map(sum, grid)), tuple(map(sum, zip(*grid)))
        print (X,Y)
        return sum(X[i] + Y[j] > 2 for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j])