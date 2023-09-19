class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        start = sum(cell  << (i * n + j) for i, row in enumerate(mat) for j, cell in enumerate(row))
        print("{0:b}".format(start))
        dq = collections.deque([(start, 0)])
        seen = {start}
        while dq:
            cur, step = dq.popleft()
            if not cur:
                return step
            for i in range(m):
                for j in range(n):
                    next = cur
                    for r, c in (i, j), (i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j):
                        if m > r >= 0 <= c < n:
                            #print("{0:b}".format(1^(1 << (r * n + c))),r,c)
                            next ^= 1 << (r * n + c) # exclusive or,  If the bits are the same, the result is 0. If the bits are different, the result is 1.
                            #print("{0:b}".format(next), r, c)
                    if next not in seen:
                        seen.add(next)
                        dq.append((next, step + 1))
        return -1
    # https://leetcode.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix/discuss/446342/JavaPython-3-Convert-matrix-to-int%3A-BFS-and-DFS-codes-w-explanation-comments-and-analysis.