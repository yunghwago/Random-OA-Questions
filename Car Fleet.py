class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [] #tuple = (position, speed)
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(reverse = True)

        stack = [] #time taken to reach end per car
        for distance, speed in cars:
            stack.append((target-distance)/speed)
            #if car in the back gets to the destination faster than car in the front they collide
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
