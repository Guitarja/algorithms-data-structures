from sortedcontainers import SortedList

class MRUQueue:

    def __init__(self, n: int):
        self.sl = SortedList((i-1, i) for i in range(1, n+1))
    
    def fetch(self, k: int) -> int:
	    # 1. Find the kth item
        _, item = self.sl[k-1]
        # 2. Find the helper element of the last item in the SortedList
        lastItemHelper, _ = self.sl[-1]
		# 3. Remove the kth item
        del self.sl[k-1]
		# 4. Place the removed item last in the SortedList
        self.sl.add((lastItemHelper+1, item))
        return item


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)

# O(log(n)) fetch and O(n*log(n)) constructor