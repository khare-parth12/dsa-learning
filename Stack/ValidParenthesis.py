# Leetcode 20

class Solution(object):
    def isValid(self, s):
        stack = []
        dummyS = list(s)
        Dict = {")":"(", "}":"{", "]":"["}

        for p in dummyS:
            if p in Dict.values():
                stack.append(p)
            elif stack and Dict[p] == stack[-1]:
                stack.pop()
            else:
                return False

        return not stack