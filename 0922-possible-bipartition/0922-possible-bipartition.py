class UnionFind:
    def __init__(self, size) -> None:
        self.parent = list(range(size))
        self.rank = [0] * size
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x == parent_y:
            return
        
        if self.rank[parent_x] < self.rank[parent_y]:
            self.parent[parent_x] = parent_y
        elif self.rank[parent_x] > self.rank[parent_y]:
            self.parent[parent_y] = parent_x
        else:
            self.parent[parent_x] = parent_y
            self.rank[parent_y] += 1

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for a, b in dislikes:
            adj[a].append(b)
            adj[b].append(a)
        
        dsu = UnionFind(n + 1)
        for node in range(1, n + 1):
            for nei in adj[node]:
                if dsu.find(nei) == dsu.find(node):
                    return False
                dsu.union(adj[node][0], nei)
        return True

# Let E be the size of dislikes and N be the number of people.

# Time complexity: O(N+E) because of path comnpression
# Space O(N+E), parent and rank each for N and E space for graph