class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0) # here to make sure stack pop off
        stack = [-1] # a tric here for first interation
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            
            stack.append(i)
        
        heights.pop()
        return ans
    '''The stack maintain the indexes of buildings with ascending height. Before adding a new building pop the building who is taller than the new one. The building popped out represent the height of a rectangle with the new building as the right boundary and the current stack top as the left boundary. Calculate its area and update ans of maximum area. Boundary is handled using dummy buildings.'''