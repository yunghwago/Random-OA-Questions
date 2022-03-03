class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        implement a 2D binary search
        1. figure out what row we need to search
        2. run binary search on that
        """
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS-1
        while top <= bot:
            middle = (top+bot)//2
            if target < matrix[middle][0]:
                bot = middle -1
            elif target > matrix[middle][-1]:
                top = middle + 1
            else: #run binary search
                break

        #value cant be found in any of the rows
        if not (top<=bot):
            return False
        
        left, right = 0, COLS-1
        while left <= right:
            mid = (left+right)//2
            if target > matrix[middle][mid]:
                left = mid + 1
            elif target < matrix[middle][mid]:
                right = mid -1
            else:
                return True
        return False
