import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in '+-*/':
                val1 = stack.pop()
                val2 = stack.pop()
                if token == '+':
                    stack.append(val1 + val2)
                if token == '-':
                    stack.append(val2 - val1)
                if token == '*':
                    stack.append(val2 * val1)
                if token == '/':
                    v = val2 / val1
                    if v >= 0:
                        stack.append(math.floor(val2 / val1))
                    else:
                        stack.append(math.ceil(val2 / val1))

            else:
                stack.append(int(token))
        return stack.pop()
                