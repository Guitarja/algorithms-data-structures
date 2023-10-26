class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(dict)
        for s, d, w in flights:
            graph[s][d] = w
        pq = [(0, src, K+1)]
        vis = [0] * n
        while pq:
            w, x, k = heapq.heappop(pq)
            if x == dst:
                return w
            if vis[x] >= k:
                continue
            vis[x] = k
            for y, dw in graph[x].items():
                heapq.heappush(pq, (w+dw, y, k-1))
        return -1
# maintain a n-size heap and time complexity is O((m + n)logn). m is number of edges and n is number of nodes. And it can be improved to O(m + nlogn) with a Fibonacci heap where a delete min costs logn but an update cost costs constant time.