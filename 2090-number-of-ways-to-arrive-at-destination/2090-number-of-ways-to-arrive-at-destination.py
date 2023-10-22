class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        for u, v, time in roads:
            graph[u].append([time, v])
            graph[v].append([time, u])
        
        def dijkstra(src):
            dist = [math.inf] * n
            min_heap = [(0, src)]
            ways = [0] * n
            ways[src] = 1
            dist[src] = 0
            while min_heap:
                curr_dist, u = heapq.heappop(min_heap)
                if curr_dist > dist[u]:
                    continue
                for time, v in graph[u]:
                    if dist[v] > time + curr_dist:
                        dist[v] = time + curr_dist
                        ways[v] = ways[u]
                        heapq.heappush(min_heap, (time + curr_dist, v))
                    elif dist[v] == time + curr_dist:
                        ways[v] = (ways[u] + ways[v]) % 1_000_000_007
            return ways[n-1]
        
        return dijkstra(0)

# Complexity

# Time: O(M * logN + N), where M <= N*(N-1)/2 is number of roads, N <= 200 is number of intersections. line 15,16 reduced O(N) time by prune unuseful nodes
# Space: O(N + M)