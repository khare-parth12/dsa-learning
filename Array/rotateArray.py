class Solution:
    def rev(self, nums):
        l, r = 0, len(nums)-1

        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1

    def rotatearray(self, nums, k):
        pass