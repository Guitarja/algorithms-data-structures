class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        r, c = len(words), len(words[0])
        for i in range(r):
            for j in range(len(words[i])):
                if j >= r or i >= len(words[j]) or words[i][j] != words[j][i]: #too short, too long or not equal
                    return False
        
        return True
