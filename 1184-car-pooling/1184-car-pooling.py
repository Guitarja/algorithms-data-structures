class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        for time, passenger in sorted([item for numPassengersi, fromi, toi in trips
                                      for item in [[fromi, numPassengersi], [toi, -numPassengersi]]]
                                      ,key =lambda x: (x[0],x[1])):
            capacity -= passenger
            if capacity < 0:
                return False
        return True
    
    '''Explanation
Save all time points and the change on current capacity
Sort all the changes on the key of time points.
Track the current capacity and return false if negative
Complexity
Time O(NlogN)
Space O(N)

'''