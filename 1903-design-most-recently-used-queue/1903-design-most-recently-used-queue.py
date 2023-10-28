class Fenwick: 
    def __init__(self, n: int): 
        self.nums = [0]*(n+1)
        
    def sum(self, k: int) -> int: 
        ans = 0
        while k: 
            ans += self.nums[k]
            k -= k & -k
        return ans 
    
    def add(self, k: int, x: int) -> int: 
        k += 1
        while k < len(self.nums): 
            self.nums[k] += x
            k += k & -k 


class MRUQueue:

    def __init__(self, n: int):
        self.size = n 
        self.tree = Fenwick(n+2000) # buffer for 2000 calls
        self.vals = [0]*(n+2000)
        for i in range(n):
            self.tree.add(i, 1)
            self.vals[i] = i+1

    def fetch(self, k: int) -> int:
        lo, hi = 0, self.size
        while lo < hi: 
            mid = lo + hi >> 1 
            if self.tree.sum(mid) < k: lo = mid + 1
            else: hi = mid 
        self.tree.add(lo-1, -1)
        self.tree.add(self.size, 1)
        self.vals[self.size] = self.vals[lo-1]
        self.size += 1
        return self.vals[lo-1]

'''
    Things to note:
    1. We need a fast way to find the kth element, brute force way is O(N), so
    it should be better than that.
    2. Elements need to put at the back efficiently

    
    SOLUTION 1: BINARY INDEXED TREE
    
    TC: O(log(T) * log(T))
    SC: O(T)

    where T = n + 2000 + 1, n = initial size of array

    To find out the kth element, we can use cummulative sum of elements. In the
    cummulative sum, each element contributes 1, i's not their value which is used
    for the sum, rather their frequency.
    Idea is to use binary search in the range of elements and for the nums[mid], 
    check if it's cummulative sum till that point is k.

    Once we move the element to the back, we need to update the cummulative sum as well.
    So we can use either a segment tree or binary indexed tree for this.
    Here in this solution a Binary Indexed tree is used. Initially we update the sum
    for 1..n. Then for each fetch, when we move the element to back, we do 2 update calls.
    One update(kth_idx, -1) which effectively removes contribution of kth element
    and the other update(last_idx, 1), adds 1 to signify a new element has been added at the
    back.
'''