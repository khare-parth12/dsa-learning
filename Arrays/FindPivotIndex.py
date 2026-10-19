# Leetcode 724

class Solution(object):
    def pivotIndex(self, nums):
        n = len(nums)
        pref = [0] * n
        suff = [0] * n

        for i in range(1, n):
            pref[i] = pref[i-1] + nums[i-1]

        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] + nums[i+1]

        for i in range(n):
            if pref[i] == suff[i]: return i

        return -1