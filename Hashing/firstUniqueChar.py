from collections import Counter

class Solution:
    def firstUniChar(self, s):
        freq = Counter(list(s))

        minIdx = -1
        for c, f in freq.items():
            if f == 1 and minIdx == -1:
                minIdx = s.find(c)
                
            if f == 1 and minIdx != -1:
                minIdx = min(minIdx, s.find(c))
        
        return minIdx