class Solution:
    def maxSubarray(self, nums):
        sum = nums[0]
        maxSum = nums[0]
        for num in nums:
            sum = max(num, sum+num)
            maxSum = max(maxSum, sum)

        return maxSum