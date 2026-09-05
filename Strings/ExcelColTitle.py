class Solution(object):
    def convertToTitle(self, columnNumber):
        if columnNumber<=26: return chr(columnNumber-1 + ord("A"))

        res = ""
        while columnNumber>0:
            columnNumber -= 1
            currCol = chr((columnNumber%26) + ord("A"))
            res = currCol + res
            columnNumber = columnNumber // 26

        return res