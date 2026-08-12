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
                    stack.append(int(val2 / val1))

            else:
                stack.append(int(token))
        return stack.pop()
                