class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #limit of open parenthesises = n
        #limit of closed parenthesises = n
        #add a closed parenthesis if numClosed < numOpen
        #valid IIF open == closed == n
        
        stack = [] #current generation of parenthesis
        output = [] #all the variations of parenthesis
        numOpen = 0
        numClosed = 0
        
        def backtrack(numOpen, numClosed):
            if numOpen == numClosed == n:
                output.append("".join(stack))
                return
            if numOpen < n:
                stack.append("(")
                backtrack(numOpen + 1, numClosed)
                stack.pop() #undo decision aka backtrack
            if numClosed < numOpen:
                stack.append(")")
                backtrack(numOpen, numClosed + 1)
                stack.pop()
        backtrack(numOpen, numClosed)
        return output        
