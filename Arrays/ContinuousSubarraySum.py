# Leetcode 523

class Solution:
    def checkSubarraySum(self, nums, k):
        n = len(nums)
        rem = 0
        rem_cache = {0:-1}

        for i in range(n):
            rem += nums[i]
            rem %= k

            if rem not in rem_cache:
                rem_cache[rem] = i
            elif i - rem_cache[rem] >= 2:
                return True

        return False