class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # build graph
        graph = collections.defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        seen = [False] * n
        queue = collections.deque([source])

        while queue:
            curr_node = queue.popleft()
            if curr_node == destination:
                return True
            
            for next_node in graph[curr_node]:
                if not seen[next_node]:
                    seen[next_node] = True
                    queue.append(next_node)
        
        return False

# Complexity Analysis
# Let n be the number of nodes and m be the number of edges.

# Time complexity: O(n + m)

# In a typical BFS search, the time complexity is O(V + E) where V is the number of vertices and E is the number of edges. There are nnn nodes and mmm edges in this problem.
# We build adjacent list of all m edges in graph which takes O(m)
# Each node is added to the queue and popped from queue once, it takes O(n) to handle all nodes.
# The time complexity is O(n + m)

# Space complexity: O(n + m)
# We used a hash map neighbors to store all edges, which requires O(m) space for mmm edges.
# We use seen, either a hash set or an array to record the visited nodes, which takes O(n) space.
# There may be up to n nodes stored in queue and O(n) space is required.
# Therefore, the space complexity is O(n + m)