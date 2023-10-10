class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        # Create dictionary using each friend as keys and a list of people they are closer to than the person they are paired with as values. This can be done using index.

# Then use nested for loop to find when people are on each other's list.
        count = 0
        p_dict = dict()
        for a, b in pairs:
            p_dict[a] = preferences[a][:preferences[a].index(b)]
            p_dict[b] = preferences[b][:preferences[b].index(a)]

        for i in p_dict:
            for x in p_dict[i]:
                if i in p_dict[x]:
                    count += 1
                    break
        
        return count