from sortedcontainers import SortedDict

class Leaderboard:

    def __init__(self):
        self.scores = {}
        self.sortedScores = SortedDict()

    def addScore(self, playerId: int, score: int) -> None:

        # The scores dictionary simply contains the mapping from the
        # playerId to their score. The sortedScores contain a BST with 
        # key as the score and value as the number of players that have
        # that score.     
        if playerId not in self.scores:
            self.scores[playerId] = score
            self.sortedScores[-score] = self.sortedScores.get(-score, 0) + 1
        else:
            preScore = self.scores[playerId]
            val = self.sortedScores.get(-preScore)
            if val == 1:
                del self.sortedScores[-preScore]
            else:
                self.sortedScores[-preScore] = val - 1    
            
            newScore = preScore + score
            self.scores[playerId] = newScore
            self.sortedScores[-newScore] = self.sortedScores.get(-newScore, 0) + 1
        
    def top(self, K: int) -> int:
        count, total = 0, 0

        for key, value in self.sortedScores.items():
            # times = self.sortedScores.get(key)
            for _ in range(value): 
                total += -key
                count += 1
                
                # Found top-K scores, break.
                if count == K:
                    break
                
            # Found top-K scores, break.
            if count == K:
                break
        
        return total

    def reset(self, playerId: int) -> None:
        preScore = self.scores[playerId]
        if self.sortedScores[-preScore] == 1:
            del self.sortedScores[-preScore]
        else:
            self.sortedScores[-preScore] -= 1
        del self.scores[playerId]

# Time Complexity:

# add LogN
# reset LogN
# top K
# Space Complexity
# N to 2N