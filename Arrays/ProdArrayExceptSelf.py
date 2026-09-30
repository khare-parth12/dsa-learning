# Leetcode 238

class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        i = 0
        pref = [1] * n
        suff = [1] * n

        for i in range(1, n):
            pref[i] = pref[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]

        ans = []
        for i in range(n):
            ans.append(pref[i] * suff[i])

        return ans