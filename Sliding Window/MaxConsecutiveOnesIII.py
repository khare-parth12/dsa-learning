# Leetcode 1004

class Solution(object):
    def longestOnes(self, nums, k):
        left = 0
        v = [0] * 2
        ans = 0

        for right in range(len(nums)):
            v[nums[right]] += 1

            while (left < len(nums)) and v[0] > k:
                v[nums[left]] -= 1
                left += 1

            ans = max(ans, right-left+1)

        return ans

            