# Leetcode 209

class Solution(object):
    def minSubArrayLen(self, target, nums):
        min_len = float('inf')
        total = 0
        l = 0

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                if r-l+1 < min_len:
                    min_len = r-l+1
                total -= nums[l]
                l += 1

        return min_len if min_len != float('inf') else 0
