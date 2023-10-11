class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.que = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False
        else:
            self.dict[val] = len(self.que)
            self.que.append(val)
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.dict:
            return False
        else:
            pos = self.dict[val]
            last_val = self.que[-1]
            self.dict[last_val] = pos
            self.que[pos] = last_val
            self.que.pop()
            del self.dict[val]
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.que)
        
# Time complexity. GetRandom is always O(1)
# Insert and Delete both have O(1)average time complexity,
# and O(N) in the worst-case scenario
# when the operation exceeds the capacity of currently allocated array/hashmap and invokes space reallocation.

# Space complexity: O(N)\mathcal{O}(N)O(N), to store N elements.

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()