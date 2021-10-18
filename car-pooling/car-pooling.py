class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        for time, passenger in sorted((item for numPassengersi, fromi, toi in trips
                                      for item in [[fromi, numPassengersi], [toi, -numPassengersi]])
                                      ):
            capacity -= passenger
            if capacity < 0:
                return False
        return True