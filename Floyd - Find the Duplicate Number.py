class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True: #while slow != fast doesnt work here because they start at the same index
        #so this is basically a python Do While loop
            slow = nums[slow]
            fast = nums[nums[fast]] # here we are treating fast like a pointer
            """
            explanation
            given the array [1,3,4,2,2]
            slow and fast print 4
            nums[slow] is just the actual value 4
            while fast nums[nums[fast]] turns into fast[2], at array index either 3 or 4
            and redirects back to 4
            if you imagine the numbers pointing to their indices, instead of the numbers being
            entries in an array, then its like we have a cyclical linked list
            """
            if slow == fast:
                break
        
        """
        so the previous while loop will return some point that is some distance away from the cycle.
        this distance is equidistant to the distance between the start of the array and the cycle.
        why this is the case? honestly i have no idea it is not intuitive at all.
        """
        #find the point between where slow left off and the start
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        return slow
