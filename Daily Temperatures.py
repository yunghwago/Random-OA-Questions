class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0 for day in temperatures]
        currentDay = 0
        stack = [] #tuple = (temperature, index)
        for i, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                sTemp, sIndex = stack.pop()
                output[sIndex] = i - sIndex
            stack.append((temperature, i)) 
        return output
