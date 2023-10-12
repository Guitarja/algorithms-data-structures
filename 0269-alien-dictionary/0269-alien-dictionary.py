from collections import defaultdict, Counter, deque

class Solution:

    def alienOrder(self, words: List[str]) -> str:
        
        # Step 0: create data structures + the in_degree of each unique letter to 0.
        adj_list = defaultdict(set)
        in_degree = Counter({c : 0 for word in words for c in word})
                
        # Step 1: We need to populate adj_list and in_degree.
        # For each pair of adjacent words...
        for first_word, second_word in zip(words, words[1:]):
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        in_degree[d] += 1
                    break
            else: # Check that second word isn't a prefix of first word.
                if len(second_word) < len(first_word): return ""
        
        # Step 2: We need to repeatedly pick off nodes with an indegree of 0.
        output = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            c = queue.popleft()
            output.append(c)
            for d in adj_list[c]:
                in_degree[d] -= 1
                if in_degree[d] == 0:
                    queue.append(d)
                    
        # If not all letters are in output, that means there was a cycle and so
        # no valid ordering. Return "" as per the problem description.
        if len(output) < len(in_degree):
            return ""
        # Otherwise, convert the ordering we found into a string and return it.
        return "".join(output)
# Let N be the total number of strings in the input list.

# Let C be the total length of all the words in the input list, added together.

# Let U be the total number of unique letters in the alien alphabet

# time 
# 1，If U^2 is smaller than NNN, then min(U^2, N) = U^2. By definition, we've just said that U^2 is smaller than N, which is in turn smaller than C, and so U^2  is definitely less than C. This leaves us with O(C).

# 2，If U^2 is larger than N, then min(U^2, N) = N. Because C>N, we're left with O(C).

# So in all cases, we know that C>min(U^2, N). This gives us a final time complexity of O(C).

# space O(1) or O(U + min(U^2, N))