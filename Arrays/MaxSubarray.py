# Leetcode 53

class Solution(object):
    def maxSubArray(self, nums):
        if len(nums) == 1: return nums[0]

        currSum = 0
        maxSum = float('-inf')
        for i in range(len(nums)):
            currSum += nums[i]
            maxSum = max(maxSum, currSum)

            if currSum < 0:
                currSum = 0

        return maxSum