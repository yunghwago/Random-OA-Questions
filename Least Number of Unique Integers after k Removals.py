class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        output = 0
        counter = Counter(arr) # get count of every number in arr
        #sort counter by occurence of each number
        counter = sorted(counter.items(), key = lambda x: x[1])
        print(counter)
        
        # For each iteration of k, decrement by 1 from the occurrence value
        # in each tuple.
        # If the occurrence is 0, move to the next tuple and continuing
        # subtracting 1 from occurrence
        currentIndex = 0
        for i in range(k):
            counter[currentIndex] = (counter[currentIndex][0], counter[currentIndex][1]-1)
            if counter[currentIndex][1] == 0:
                currentIndex += 1
        #print(counter)
        
        for number, count in counter:
            if count != 0:
                output += 1
        return output
Console
