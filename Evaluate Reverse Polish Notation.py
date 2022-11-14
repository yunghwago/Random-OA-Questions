class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = "+-*/"
        for token in tokens:
            if token in operations: # perform an operation
                operation = token
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                if operation == "+":
                    newVal = val1 + val2
                    stack.append(newVal)
                elif operation == "-":
                    newVal = val2 - val1
                    stack.append(newVal)
                elif operation == "*":
                    newVal = val2 * val1
                    stack.append(newVal)
                elif operation == "/":
                    newVal = val2/val1
                    stack.append(newVal)
            else:
                stack.append(token)
        return int(stack[0])
