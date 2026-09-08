class Solution(object):
    def findMaxAverage(self, nums, k):
        if (len(nums)==k): return sum(nums)/k
        val = sum(nums[:k])
        maxSum = val

        for right in range(k, len(nums)):
            val += nums[right]
            val -= nums[right - k]

            maxSum = max(maxSum, val)
            

        return maxSum/k