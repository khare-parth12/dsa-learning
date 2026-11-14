# Leetcode 227

class Solution(object):
    def calculate(self, s):
        s += '+'
        stack = []
        n = 0
        op = '+'

        for c in s:
            if c == ' ':
                continue

            if c.isdigit():
                n = n * 10 + int(c)
                continue

            if op == '+':
                stack.append(n)
            elif op == '-':
                stack.append(-n)
            elif op == '*':
                stack.append(stack.pop()*n)
            elif op == '/':
                stack.append(int(float(stack.pop())/n))

            op = c
            n = 0

        return sum(stack)     