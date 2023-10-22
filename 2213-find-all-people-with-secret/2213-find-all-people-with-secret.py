class UnionFind:
    def __init__(self) -> None:
        self.parents = {}
        self.ranks = {}
    
    def insert(self, x):
        if x not in self.parents:
            self.parents[x] = x
            self.ranks[x] = 0
    
    def find_parent(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find_parent(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        self.insert(x)
        self.insert(y)
        parent_x = self.find_parent(x)
        parent_y = self.find_parent(y)
        if parent_x == parent_y:
            return
        if self.ranks[parent_x] > self.ranks[parent_y]:
            self.parents[parent_y] = x
        else:
            self.parents[parent_x] = y
            if self.ranks[parent_x] == self.ranks[parent_y]:
                self.ranks[parent_y] += 1  
    
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        time2meets = defaultdict(list)
        for x, y, t in meetings:
            time2meets[t].append((x, y))
        time2meets = sorted(time2meets.items())
 
        curr_know = set([0, firstPerson])

        for time, meets in time2meets:
            uf = UnionFind()
            for x, y in meets:
                uf.union(x, y)
            
            groups = defaultdict(set)
            for idx in uf.parents:
                groups[uf.find_parent(idx)].add(idx)
            
            for group in groups.values():
                if group & curr_know:
                    curr_know.update(group)

        return list(curr_know)

# Complexity Analysis:

# Let N be the number of peoples, M be the number of meetings.

# Time Complexity:

# Sorting the timestamp of meetings takes at most O(M log M) time (or if you use bucket sort it will take O(T) where T = 10 ** 5 ).
# Merging all meetings takes O(M) times:
# Suppose there are K people attending a meeting at a certain timestamp:
# The union part takes O(K) times if we implement DSU with path compression and union by rank.
# Finding the group members takes O(K) times.
# Updating the group members takes O(K) times.
# Since sum(K) = M * 2, this part takes O(M) times.
# Total time complexity is O(M log M), irrelevant to N if we use hash table to maintain parents and ranks in DSU.
# Space Complexity: O(M + N)