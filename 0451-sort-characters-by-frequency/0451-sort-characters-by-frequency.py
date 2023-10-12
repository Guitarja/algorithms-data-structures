class Solution:
    def frequencySort(self, s: str) -> str:
        string_builder = []
        count_dict = collections.Counter(s)
        fre_dict = {k:v for k, v in sorted(count_dict.items(), key = lambda item: (item[1],item[0]), reverse = True)}
        for letter, freq in fre_dict.items():
            string_builder.append(letter * freq)
        return "".join(string_builder)

# Time Complexity : O(n log⁡ n) OR O(n+klogk).

# Putting the characterss into the HashMap has a cost of O(n), because each of the nnn characterss must be put in, and putting each in is an O(1) operation.

# Sorting the HashMap keys has a cost of O(klogk), because there are kkk keys, and this is the standard cost for sorting. If only using nnn, then it's O(nlogn). For the previous question, the sort was carried out on nnn items, not kkk, so was possibly a lot worse.

# Traversing over the sorted keys and building the String has a cost of O(n), as nnn characters must be inserted.

# Therefore, if we're only considering nnn, then the final cost is O(nlogn).

# Considering kkk as well gives us O(n+klogk), because we don't know which is largest out of n and k log⁡k. We do, however, know that in total this is less than or equal to O(nlogn).

# Space Complexity : O(n).

# The HashMap uses O(k) space.

# However, the StringBuilder at the end dominates the space complexity, pushing it up to O(n), as every character from the input String must go into it. Like was said above, it's impossible to do better with the space complexity here.