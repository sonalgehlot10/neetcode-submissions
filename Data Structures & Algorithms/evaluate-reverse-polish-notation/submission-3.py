class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        notations = {'+', '-', '*', '/'}
        stack = []
        for t in tokens:
            if t not in notations:
                stack.append(t)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if t == '+':
                    stack.append(a + b)
                elif t == '-':
                    stack.append(a - b)
                elif t == '*':
                    stack.append(a * b)
                elif t == '/':
                    stack.append(a / b)

        return int(stack[-1])

# Time: O(n)
# Space: O(n)