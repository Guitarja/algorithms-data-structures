class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        memo =[[0] * (len(satisfaction) + 1) for j in (range(len(satisfaction) + 1))]
        def find_max(satisfaction, memo, index, time):
            if index == len(satisfaction):
                return 0
            if memo[index][time]:
                return memo[index][time]
            memo[index][time] = max(satisfaction[index]*time + find_max(satisfaction, memo, index+1, time+1), find_max(satisfaction, memo, index+1, time))
            return memo[index][time]
        return find_max(satisfaction, memo, 0, 1)