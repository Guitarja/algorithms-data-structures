class Solution:
    def findGameWinner(self, n: int) -> bool:
        sg = [None, 0, 1]
        for _ in range(98):
            sg.append((sg[-1] + 1) ^ (sg[-2] + 1))
        return sg[n] != 0

# This game is a special case of Hackenbush game.
# According to Colon principle, in this problem:

# SG(1) = 1 - 1 = 0
# SG(2) = 2 - 1 = 1
# SG(n) = (SG(n - 1) + 1) xor (SG(n - 2) + 1)