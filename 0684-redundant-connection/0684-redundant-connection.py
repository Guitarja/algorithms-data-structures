class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges)))

        def find(x):
            if parent[x] == x:
                return x 
            return find(parent[x])

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            print(rootX,rootY,parent)
            if rootX == rootY:
                return False
            parent[rootY] = rootX
            return True

        for x, y in edges:
            if not union(x - 1, y - 1): 
                return [x, y]

        raise ValueError("Illegal input.")