class Solution:
    def isValid(self, s: str) -> bool:
        b = []

        c = {'}':'{', ']':'[', ')': '('}

        for x in s:
            if x in '({[':
                b.append(x)
            else:
                if not b:
                    return False
                if b[-1] != c[x]:
                    return False
                b.pop()

        return not b