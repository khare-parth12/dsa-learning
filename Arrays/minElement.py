# 3300. Minimum Element After Replacement With Digit Sum
class Solution():
    def sumOfDigits(self, num):
        sum = 0
        while num>0:
            sum += num%10
            num = num//10

        return sum

    def minElement(self, nums):
        for i in range(len(nums)):
            nums[i] = self.sumOfDigits(nums[i])

        minNum = nums[0]
        for num in nums:
            minNum = min(minNum, num)

        return minNum