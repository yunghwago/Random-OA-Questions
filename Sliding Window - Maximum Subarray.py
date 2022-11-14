class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        anchor = 0
        currSum = 0
        maxSum = nums[0]
        for i, num in enumerate(nums):
            currSum += num
            maxSum = max(currSum, maxSum)    
            if currSum < 0:
                anchor = i
                currSum = 0
        return maxSum
