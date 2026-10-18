# Leetcode 1287

class Solution(object):
    def findSpecialInteger(self, arr):
        if len(arr) == 1: return arr[0]

        freq = {}
        n = len(arr)

        for i in range(n):
            freq[arr[i]] = 1 if arr[i] not in freq.keys() else freq.get(arr[i]) + 1

            if freq[arr[i]] > (n/4):
                return arr[i]
