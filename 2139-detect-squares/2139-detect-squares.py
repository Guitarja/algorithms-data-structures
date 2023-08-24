class DetectSquares:
    '''
    To compute count(p1):
    We try all points p3 which together with p1 form the diagonal of non-empty square, it means abs(p1.x-p3.x) == abs(p1.y-p3.y) && abs(p1.x-p3.x) > 0
    Since we have 2 points p1 and p3, we can form a square by computing the positions of 2 remain points p2, p4.
    p2 = (p1.x, p3.y)
    p4 = (p3.x, p1.y)
    '''
    def __init__(self):
        self.cntPoints = Counter()

    def add(self, point: List[int]) -> None:
        self.cntPoints[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        ans = 0
        x1, y1 = point
        for (x3, y3), cnt in self.cntPoints.items():
            if abs(x1 - x3) == 0 or abs(x1 - x3) != abs(y1 - y3):
                continue  # Skip empty square or invalid square point!
            ans += cnt * self.cntPoints[(x1, y3)] * self.cntPoints[(x3, y1)]
        return ans

# Complexity

# Time:
# add: O(1)
# count: O(T), where T <= 5000 is total number of points after calling add.
# Space: O(T) in Python, O(1000^2) in C++/Java

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)