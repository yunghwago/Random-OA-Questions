class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scores = []
        for operation in ops:
            if operation == "C":
                scores.remove(scores[-1])
            elif operation == "D":
                scores.append(2 * int(scores[-1]))
            elif operation == "+":
                scores.append(int(scores[-1]) + int(scores[-2]))
            else:
                scores.append(int(operation))
        output = 0
        for score in scores:
            output += score
        return output
