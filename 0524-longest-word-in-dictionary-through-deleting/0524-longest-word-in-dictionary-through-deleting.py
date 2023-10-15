class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_subseq(x, y) -> bool:
            j = 0
            i = 0
            while i < len(x) and j < len(y):
                if x[i] == y[j]:
                    j += 1
                i += 1
            return j == len(y)
        
        ret = ""
        for word in dictionary:
            if is_subseq(s, word):
                if len(word) > len(ret) or (len(word) == len(ret) and word < ret):
                    ret = word
        
        return ret

# time n*x n is number of strings in dict and x is average stringh length
# space x, ret varuable is used, or 1 as x is auxiliary 