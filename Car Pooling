class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x:x[1])
        startingPoints = defaultdict(int) 
        #key = startingPoints, value = total passengers picked up
        endingPoints = defaultdict(int) 
        #key = ending points, value = total passengers dropped off
        
        for trip in trips:
            startingPoints[trip[1]] += trip[0]
            endingPoints[trip[2]] += trip[0]
        
        currentPassengers = 0
        for i in range((trips[-1][2])+1):
            if i in startingPoints:
                currentPassengers += startingPoints[i]
            if i in endingPoints:
                currentPassengers -= endingPoints[i]
            if currentPassengers > capacity:
                return False
        return True
