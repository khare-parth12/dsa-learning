# Leetcode 283

class Solution:
    def MoveZeroes(self, nums):
        left, right = 0, 0
        n = len(nums)

        while left<n:
            if nums[left] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                right += 1

            left += 1